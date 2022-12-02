import streamlit as st
import pandas as pd
import os
import numpy as np
import time
import seaborn as sns
import matplotlib.pyplot as plt

from src.utils.constants import DATA_DESC, DATA_TYPES
from MonthStuff.Months import *

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

    with models:
        st.header("Logistic Regression Model")
        st.image("Streamlit_Images/model1.PNG", width=1000)

    with model_vis:
        st.header("Model Visualizations")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
        chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

        st.line_chart(chart_data)

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

    with month_comparisons:
        st.header("Month Comparisons (April VS March)")
        s=st.selectbox('Pick the category of interest to compare', ['ShippingLevel', 'Conversion','Price'])
        march, april = getMonthData(model_data)
        if(s=='ShippingLevel'):
            st.subheader("Shipping Level Comparisons")
            shipping_level_comparison(march, april)
        elif(s=='Conversion'):
            st.subheader("Conversion Level Comparisons")
            conversion_comparison(march, april)
        elif(s=='Price'):
            st.subheader("Average Price Level Comparisons")
            price_comparison(march,april)



if __name__ == "__main__":
    main()