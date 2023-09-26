import pandas as pd
import plotly.express as px
import streamlit as st
from ydata_profiling import ProfileReport
import streamlit.components.v1 as components
import warnings
import matplotlib.cbook

warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)

def display(st, data):
    st.header("Data Profiling")

    # Dropdown to select dataset for profiling
    dataset_name = st.selectbox("Choose a dataset to profile", list(data.keys()))
    df = data[dataset_name]

    # Generate the report
    report = ProfileReport(df)
    
    # Save the report as HTML and display it in Streamlit
    report.to_file("ydata_report.html")
    with open("ydata_report.html", 'r', encoding='utf-8') as f:
        html = f.read()
    components.html(html, width=1000, height=600)
    # Data distribution for numerical columns
    col1, col2 = st.columns(2)

    with col1:
        # Uniqueness
        st.subheader("Unique Values")
        unique_counts = df.nunique()
        st.write(pd.DataFrame({"Unique Count": unique_counts}))

    with col2:
        # Null value analysis
        st.subheader("Missing Values Analysis")
        missing_counts = df.isnull().sum()
        missing_percentage = (df.isnull().sum() / df.shape[0]) * 100
        st.write(pd.DataFrame({"Missing Count": missing_counts, "Missing %": missing_percentage}))

    # Basic Statistics
    st.subheader("Basic Statistics")
    st.write(df.describe())

    # Data distribution for numerical columns
    st.subheader("Data Distribution")
    col_to_view = st.selectbox("Select a column to view its distribution", df.columns)
    if df[col_to_view].dtype == "object":
        fig = px.bar(df[col_to_view].value_counts(), title=f"Frequency Distribution for {col_to_view}")
    else:
        fig = px.histogram(df, x=col_to_view, title=f"Distribution for {col_to_view}")
    st.plotly_chart(fig)

        
   