import streamlit as st
import pandas as pd
import os
import numpy as np
import time
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import math 
from sklearn.linear_model import LogisticRegression
import plotly.express as px

from src.utils.constants import DATA_DESC, DATA_TYPES

def main():
    st.title("Inflation's impact on Digital Advertising")
    st.caption('Team-85: Justin Handsman, Jenni Ayash, Korou M, Kevin Fernandez, Landon Lowe')
    model_data = pd.read_parquet('src/data/data')
    data_doc, models, model_vis, survey_doc, survey_res,month_comparisons = st.tabs(["Data Documentation", "Models", "Model Visualizations","Survey Documentation","Survey Results","Month Comparisons"])

    with data_doc:
        st.header("Sample Data")
        st.write(model_data.head(10))
        columns_df = pd.DataFrame(model_data.columns, columns=['Column Name'])
        columns_df['Data Type'] = [DATA_TYPES[x] for x in columns_df['Column Name']]
        columns_df['Description'] = [DATA_DESC[x] for x in columns_df['Column Name']]
        st.write(columns_df)
        
        md = model_data.copy()
        taxonomies = ['All'] + md['taxonomy_level1'].unique().tolist()
        option = st.selectbox('Product Category',taxonomies)
        if option != 'All':
            md = md.query(f"taxonomy_level1=='{option}'")
        md['boosted'] = md['boosted'].apply(lambda x: int(x))
        y = pd.get_dummies(md.platform, prefix='platform')
        x = pd.get_dummies(md.device_type, prefix='device_type')
        md = pd.concat([md,y,x], axis=1)
        fig = plt.figure(figsize=(10, 7))
        sns.heatmap(md.drop(columns=['boosted','taxonomy_level']).corr().round(2), annot=True, annot_kws={"size": 10}, linewidths=0.1, linecolor='black').set(title='Correlation Heatmap')
        st.pyplot(fig)

        fig = px.violin(md, y="price", x="taxonomy_level1", color="conversion", box=True)
        st.write(fig)

    with models:
        st.header("Logistic Regression Model")
        st.write('Data Cleaning/Manipulation: ')
        st.code('''def clean_data(df):
        df = df.query("taxonomy_level1 != 'Other categories")
        df['boosted'] = df['boosted'].apply(lambda x: int(x))
        y = pd.get_dummies(df.platform, prefix='platform')
        x = pd.get_dummies(df.device_type, prefix='device_type')
        df = pd.concat([df,y,x], axis=1)
        return df''')
        st.write('Model Generation: ')
        st.code('''def run_regression(df):
        df['price'] = df['price'].apply(lambda x: math.log(x))
        X = df[['boosted','free_shipping','is_pdp','original_price','price','print_position','platform_mobile','device_type_desktop','device_type_ios','device_type_mobile']]
        y = df['conversion']
        clf = LogisticRegression(random_state=0).fit(X, y)
        return clf
        ''' )
        st.write('Results: ')
        st.code('''def print_results(clf, X, y):
        return [clf.score(X,y), clf.coef_]
        ''')

        st.write('''Accuracy: 0.92''')
        st.write('''Coefficients''', {"boosted": 0.0, "free_shipping":-0.01, "original_price":0.00, "is_pdp":0.00, "price":-0.3, "print_position":-0.0, "platform_mobile":-0.69, "device_type_desktop":-0.07, "device_type_ios":0.28, "device_type_mobile":-1.02})
        st.caption("This is for the whole dataset, for meaningful results we need to break out by product category to get product category level insights.")
       

        
    with model_vis:
        st.header("Model Visualizations")
        md2 = model_data.copy()
        print(md2.columns)
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                device_types = ['All'] + md2['device_type'].unique().tolist()
                option = st.selectbox('Device Types',device_types)
                if option != 'All':
                    md2 = md2.query(f"device_type=='{option}'")
            with col2:
                platforms = ['All'] + md2['platform'].unique().tolist()
                option2 = st.selectbox('Platforms',platforms)
                if option2 != 'All':
                    md2 = md2.query(f"platform=='{option2}'")

        md2['boosted'] = md2['boosted'].apply(lambda x: int(x))
        y = pd.get_dummies(md2.platform, prefix='platform')
        x = pd.get_dummies(md2.device_type, prefix='device_type')
        md2 = pd.concat([md2,y,x], axis=1)
        md2['price'] = md2['price'].apply(lambda x: math.log(x))
        d = {}
        acc = []
        for i in md2['taxonomy_level1'].unique().tolist():
            try:
                df = md2.query(f"taxonomy_level1=='{i}'")
                df['price'] = df['price'].apply(lambda x: math.log(x))
                X = df[['boosted','free_shipping','is_pdp','price','print_position']]
                y = df['conversion']
                clf = LogisticRegression(random_state=0).fit(X, y)
                clf.score(X, y)
                coef = clf.coef_[0].tolist()[4]
                d[i] = coef
                acc = acc + [clf.score(X,y)]
            except:
                pass
        coef_df = pd.DataFrame({k: v*100 for k, v in sorted(d.items(), key=lambda item: item[1])}, index=['1']).T
        coef_df.reset_index(inplace=True)
        coef_df.columns=['Product Category','Price Coefficient']

        fig3 = plt.figure(figsize=(10, 7))
        sns.set(style="darkgrid")
        sns.barplot(data=coef_df, y='Product Category', x="Price Coefficient")
        st.pyplot(fig3)

        st.write('Average Accuracy: ', round(sum(acc)/len(acc),2), '%')
        st.write(coef_df)

    with survey_doc:
        st.header("Survey Documentation")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

    with survey_res:
        st.header("Survey Responses")
        st.image("Streamlit_Images/survey1.PNG", width=700)
        st.image("Streamlit_Images/survey2.PNG", width=700)
        st.image("Streamlit_Images/survey3.PNG", width=700)
        st.image("Streamlit_Images/survey4.PNG", width=700)
        st.image("Streamlit_Images/survey5.PNG", width=700)
        st.image("Streamlit_Images/survey6.PNG", width=700)
        st.image("Streamlit_Images/survey7.PNG", width=700)
        st.image("Streamlit_Images/survey8.PNG", width=700)
        st.image("Streamlit_Images/survey9.PNG", width=700)









if __name__ == "__main__":
    main()