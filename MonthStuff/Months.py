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
def conversion_comparison(march,april):
    march_conv_percentage = sum(march['conversion'].values) / len(march['conversion'].values) *100.00
    april_conv_percentage = sum(april['conversion'].values) / len(april['conversion'].values) *100.00
    st.write("The March Conversion Percentage was: ",march_conv_percentage)
    st.write("The April Conversion Percentage was: ",april_conv_percentage)
def shipping_level_comparison(march_portion,april_portion):
    march_prop_freely_shipped_level = (sum(march_portion['free_shipping'].values) *100.00/ len(
        march_portion['free_shipping'].values))
    april_prop_freely_shipped_level = (sum(april_portion['free_shipping'].values) *100.00/ len(
        april_portion['free_shipping'].values))
    st.write("The March percentage of items Freely Shipped was: ", march_prop_freely_shipped_level)
    st.write("The April percentage of items Freely Shipped was: ", april_prop_freely_shipped_level)
    #went from 37.5% free shipping to 41.83% free shipping
def price_comparison(march_portion,april_portion):
    march_ave_pri_by_cat = (march_portion[["month", "price", "taxonomy_level1"]].groupby(by=['taxonomy_level1'], as_index=False)[
        'price'].mean())
    april_ave_pri_by_cat = (april_portion[["month", "price", "taxonomy_level1"]].groupby(by=['taxonomy_level1'], as_index=False)[
        'price'].mean())
    cat_ids_in_march = set(march_ave_pri_by_cat['taxonomy_level1'].unique())
    cat_ids_in_april = set(april_ave_pri_by_cat['taxonomy_level1'].unique())
    cat_ids_in_common = list(cat_ids_in_march.intersection(cat_ids_in_april))
    march_ave_pri_common = ([march_ave_pri_by_cat.loc[(march_ave_pri_by_cat["taxonomy_level1"] == cat), "price"].item() for
                            cat in cat_ids_in_common])
    april_ave_pri_common = ([april_ave_pri_by_cat.loc[(april_ave_pri_by_cat["taxonomy_level1"] == cat), "price"].item() for
                            cat in cat_ids_in_common])
    diff_in_category_price = scpSta.ttest_ind(april_ave_pri_common,march_ave_pri_common)  # which is 2 sided so true one sided p val is
    actual_cat_pri_pvalue = diff_in_category_price.pvalue / 2
    st.write("The p value for comparison between common categories was: ", actual_cat_pri_pvalue," which is fairly insginificant probably due to short time period of measure. Effects of shock had not hit yet.")  # .013 << .05 which means thats the mean prices by category in april were significantly higher than those in march as expected
#logistictype
# #1
# #avePriceByCategoryMonthtoMonth
# #use NamedAggregates
#
#


