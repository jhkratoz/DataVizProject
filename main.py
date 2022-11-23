import streamlit as st
import pandas as pd
import os
import numpy as np
import time

from src.utils.constants import DATA_DESC, DATA_TYPES

def main():
    st.title("Inflation's impact on Digital Advertising")
    st.caption('Team-85: Justin Handsman, Jenni Ayash, Korou M, Kevin Fernandez, Landon Lowe')
    model_data = pd.read_parquet('src/data/data')
    data_doc, models, model_vis, survey_doc, survey_res = st.tabs(["Data Documentation", "Models", "Model Visualizations","Survey Documentation","Survey Results"])

    with data_doc:
        st.header("Sample Data")
        st.write(model_data.head(10))
        columns_df = pd.DataFrame(model_data.columns, columns=['Column Name'])
        columns_df['Data Type'] = [DATA_TYPES[x] for x in columns_df['Column Name']]
        columns_df['Description'] = [DATA_DESC[x] for x in columns_df['Column Name']]
        st.write(columns_df)

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
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

if __name__ == "__main__":
    main()