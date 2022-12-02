import pandas as pd
import numpy as np
import math
from sklearn import *
import streamlit as st
import plotly as pltly
from scipy import stats as scpSta
def getMonthData(parqFrame):
    overall_set = parqFrame.sort_values(by='print_server_timestamp')
    months_dictionary = {'03': 'March', '04': 'April'}
    def get_Month(dateformat):
        return months_dictionary[dateformat.split('-')[1]]
    overall_set["month"] = overall_set["print_server_timestamp"].apply(func=get_Month)
    march_portion = overall_set[overall_set.month == "March"]
    april_portion = overall_set[overall_set.month == "April"]
    return (march_portion,april_portion)
def conversion_comparison(march_portion,april_portion):
    march_conv_percentage = sum(march_portion['conversion'].values) / len(march_portion['conversion'].values) *100.00
    april_conv_percentage = sum(april_portion['conversion'].values) / len(april_portion['conversion'].values) *100.00
    st.write("The March Conversion Percentage was: ",march_conv_percentage)
    st.write("The April Conversion Percentage was: ",april_conv_percentage)
    taxes = march_portion['taxonomy_level1'].unique().tolist()
    conv_level_by_tax_march = []
    conv_level_by_tax_april = []
    conv_level_by_tax_april_ct = []
    conv_level_by_tax_march_ct = []
    for tax in taxes:
        relevant_part_march = march_portion.loc[march_portion['taxonomy_level1'] == tax]
        relevant_part_april = april_portion.loc[april_portion['taxonomy_level1'] == tax]
        x = len(relevant_part_march['conversion'].values)
        y = len(relevant_part_april['conversion'].values)
        conv_level_by_tax_march_ct.append(sum(relevant_part_march['conversion'].values))
        conv_level_by_tax_april_ct.append(sum(relevant_part_april['conversion'].values))
        if x != 0:
            (conv_level_by_tax_march.append(sum(relevant_part_march['conversion'].values) * 100.00
                                            / x))
        else:
            conv_level_by_tax_march.append(0)
        if y != 0:
            (conv_level_by_tax_april.append(sum(relevant_part_april['conversion'].values) * 100.00
                                            / y))
        else:
            conv_level_by_tax_april.append(0)
    import plotly.graph_objs as go
    import plotly.express as px
    option = (st.selectbox("For which category would you like to see a comparison of Conversion Rate of Goods in Category by Month",
                          taxes))
    ind = taxes.index(option)
    mar_val = round(conv_level_by_tax_march[ind], 1)
    apr_val = round(conv_level_by_tax_april[ind], 1)
    barfig = go.Figure([go.Bar(x=['March', 'April'], y=[mar_val, apr_val])])
    (barfig.update_layout(font=dict(family='Arial', size=16, color='white'), xaxis=dict(title_text='Month'),
                          yaxis=dict(title_text='Rate as a Percentage'),
                          title=dict(text='Conversion Rate of Goods in Category by Month')))
    st.plotly_chart(barfig)
    opt = st.radio("Distribution of Goods Converted by Category", ['March', 'April'])
    if opt == 'March':
        st.write("Distribution of Goods Converted by Category -- March")
        st.write("________________________________________________________")
        trace = go.Pie(labels=taxes, values=conv_level_by_tax_march_ct)
        data = [trace]
        fig = go.Figure(data=data)
        st.plotly_chart(fig)
    else:
        st.write("Distribution of Goods Converted by Category -- April")
        st.write("________________________________________________________")
        trace = go.Pie(labels=taxes, values=conv_level_by_tax_april_ct)
        data = [trace]
        fig = go.Figure(data=data)
        st.plotly_chart(fig)
def shipping_level_comparison(march_portion,april_portion):
    march_prop_freely_shipped_level = (sum(march_portion['free_shipping'].values) *100.00/ len(
        march_portion['free_shipping'].values))
    april_prop_freely_shipped_level = (sum(april_portion['free_shipping'].values) *100.00/ len(
        april_portion['free_shipping'].values))
    st.write("The March percentage of items Freely Shipped was: ", march_prop_freely_shipped_level)
    st.write("The April percentage of items Freely Shipped was: ", april_prop_freely_shipped_level)
    taxes = march_portion['taxonomy_level1'].unique().tolist()
    ship_level_by_tax_march = []
    ship_level_by_tax_april = []
    ship_level_by_tax_april_ct = []
    ship_level_by_tax_march_ct = []
    for tax in taxes:
        relevant_part_march = march_portion.loc[march_portion['taxonomy_level1'] == tax]
        relevant_part_april = april_portion.loc[april_portion['taxonomy_level1'] == tax]
        x=len(relevant_part_march['free_shipping'].values)
        y=len(relevant_part_april['free_shipping'].values)
        ship_level_by_tax_march_ct.append(sum(relevant_part_march['free_shipping'].values))
        ship_level_by_tax_april_ct.append(sum(relevant_part_april['free_shipping'].values))
        if x != 0:
            (ship_level_by_tax_march.append(sum(relevant_part_march['free_shipping'].values) * 100.00
                                 / x))
        else: ship_level_by_tax_march.append(0)
        if y!=0:
            (ship_level_by_tax_april.append(sum(relevant_part_april['free_shipping'].values) * 100.00
                                 / y))
        else: ship_level_by_tax_april.append(0)
    import plotly.graph_objs as go
    import plotly.express as px
    option = st.selectbox("For which category would you like to see a comparison of Percentage Freely Shipped by Month",taxes)
    ind = taxes.index(option)
    mar_val = round(ship_level_by_tax_march[ind],1)
    apr_val = round(ship_level_by_tax_april[ind],1)
    barfig = go.Figure([go.Bar(x=['March','April'], y=[mar_val,apr_val])])
    (barfig.update_layout(font=dict(family='Arial', size=16, color='white'),xaxis=dict(title_text='Month'),
                         yaxis=dict(title_text='Percentage'),
                         title=dict(text='Percentage of Goods in Category Freely Shipped by Month')))
    st.plotly_chart(barfig)
    opt = st.radio("Distribution of Freely Shipped Goods by Category",['March','April'])
    if opt == 'March':
        st.write("Distribution of Freely Shipped Goods by Category -- March")
        st.write("________________________________________________________")
        trace = go.Pie(labels=taxes, values=ship_level_by_tax_march_ct)
        data = [trace]
        fig = go.Figure(data=data)
        st.plotly_chart(fig)
    else:
        st.write("Distribution of Freely Shipped Goods by Category -- April")
        st.write("________________________________________________________")
        trace = go.Pie(labels=taxes, values=ship_level_by_tax_april_ct)
        data = [trace]
        fig = go.Figure(data=data)
        st.plotly_chart(fig)
def price_comparison(march_portion,april_portion):
    march_price_level = (sum(march_portion['price'].values) * 100.00 / len(
        march_portion['price'].values))
    april_price_level = (sum(april_portion['price'].values) * 100.00 / len(
        april_portion['price'].values))
    st.write("The general average price for all goods in March was: ", march_price_level)
    st.write("The general average price for all goods in April was: ", april_price_level)
    taxes = march_portion['taxonomy_level1'].unique().tolist()
    price_level_by_tax_march = []
    price_level_by_tax_april = []
    for tax in taxes:
        relevant_part_march = march_portion.loc[march_portion['taxonomy_level1'] == tax]
        relevant_part_april = april_portion.loc[april_portion['taxonomy_level1'] == tax]
        x = len(relevant_part_march['price'].values)
        y = len(relevant_part_april['price'].values)
        if x != 0:
            (price_level_by_tax_march.append(sum(relevant_part_march['price'].values) / x))
        else:
            price_level_by_tax_march.append(0)
        if y != 0:
            (price_level_by_tax_april.append(sum(relevant_part_april['price'].values)
                                            / y))
        else:
            price_level_by_tax_april.append(0)
    import plotly.graph_objs as go
    import plotly.express as px
    option = st.selectbox("For which category would you like to see a comparison of Average Price Level by Month",
                          taxes)
    ind = taxes.index(option)
    mar_val = round(price_level_by_tax_march[ind], 1)
    apr_val = round(price_level_by_tax_april[ind], 1)
    barfig = go.Figure([go.Bar(x=['March', 'April'], y=[mar_val, apr_val])])
    (barfig.update_layout(font=dict(family='Arial', size=16, color='white'), xaxis=dict(title_text='Month'),
                          yaxis=dict(title_text='Average Price'),
                          title=dict(text='Average Price of Goods By Category')))
    st.plotly_chart(barfig)
    testForPriceDifferences = (scpSta.ttest_ind(price_level_by_tax_april,price_level_by_tax_march).pvalue)/2
    st.write("The P value for testing for changes in average prices of goods via comparison of common categories in March and April was: ", testForPriceDifferences," which is insignificant overall but individual categories can be seen to have major changes which is telling.")
    st.subheader("Top N Category Average Price Increases:")
    n = st.slider("Select the amount N of top price changing categories you'd like to see: ",min_value = 1,max_value=10,step=1)
    n = -1*n
    pct_change = [round(((i-v)/v * 100.00),1) for i,v in zip(price_level_by_tax_april,price_level_by_tax_march)]
    top_5_idx = np.argsort(pct_change)[n:].tolist()
    top_5_values = [pct_change[i] for i in top_5_idx]
    rel_cats = [taxes[i] for i in top_5_idx]
    percentage_change = pd.DataFrame(
        {'Category (Taxonomy Level 1)': rel_cats,
         'Percentage Increase': top_5_values
         })
    st.dataframe(percentage_change)
