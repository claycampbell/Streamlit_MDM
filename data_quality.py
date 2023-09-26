import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def display_data_quality(data):
    st.header("Data Quality Monitoring")

    # Check if dataset is already selected
    if 'selected_dataset' not in st.session_state:
        st.session_state.selected_dataset = list(data.keys())[0]  # Default to the first dataset

    datasets = list(data.keys())
    st.session_state.selected_dataset = st.selectbox("Select Dataset for Quality Metrics", datasets, index=datasets.index(st.session_state.selected_dataset))
    df = data[st.session_state.selected_dataset]


    metrics = {
        "Completeness": np.random.uniform(80, 100),
        "Uniqueness": np.random.uniform(80, 100),
        "Timeliness": np.random.uniform(80, 100),
        "Validity": np.random.uniform(80, 100),
        "Consistency": np.random.uniform(80, 100),
    }
    
    # create columns for metrics
    cols = st.columns(len(metrics))
    
    for col, (metric, value) in zip(cols, metrics.items()):
        col.metric(label=metric, value=f"{value:.2f}%", delta=f"{np.random.uniform(-5, 5):.2f}%")

    # 2. Anomalies & Outliers Detection:
    st.subheader("Anomalies & Outliers Detection")
    df_sample = df.sample(100, replace=True)

    # Clean and convert columns to numeric
    df_sample[df.columns[0]] = pd.to_numeric(df_sample[df.columns[0]], errors='coerce')
    df_sample[df.columns[1]] = pd.to_numeric(df_sample[df.columns[1]], errors='coerce')

    scatter_fig = px.scatter(
        df_sample,
        x=df.columns[0],
        y=df.columns[1],
        title="Anomaly Detection (Sample)",
        labels={df.columns[0]: df.columns[0], df.columns[1]: df.columns[1]},
    )
    st.plotly_chart(scatter_fig)

    # 3. Missing Values Analysis:
    st.subheader("Missing Values Analysis")
    missing_values = df.isnull().sum()
    missing_values = missing_values[missing_values > 0].reset_index()
    missing_values.columns = ['Column', 'MissingCount']
    
    missing_chart = px.bar(
        missing_values,
        x='Column',
        y='MissingCount',
        title="Missing Values by Column",
        labels={'Column': 'Columns', 'MissingCount': 'Missing Values Count'},
    )
    st.plotly_chart(missing_chart)

    # 4. Duplicity Analysis:
    st.subheader("Duplicity Analysis")
    duplicate_count = df.duplicated().sum()
    st.write(f"Number of duplicate records: {duplicate_count}")

    # 5. Trend Analysis:
    st.subheader("Data Quality Trend Analysis")
    # For demo, just plotting a random line chart
    fig = px.line(df, x=df.columns[0], y=df.columns[1], title="Data Quality Over Time (Demo)")
    st.plotly_chart(fig)

    # 6. Data Source Reliability:
    st.subheader("Data Source Reliability")
    sources = ["CRM Database", "Sales Logs", "User Activity Stream", "ERP System", "Stock Exchange Feed"]
    reliability_scores = np.random.uniform(80, 100, size=len(sources))
    fig = px.bar(x=sources, y=reliability_scores, title="Reliability of Data Sources")
    st.plotly_chart(fig)
    import datetime
   
    # 7. Interactive Filters:
    st.subheader("Filters")
    df[df.columns[0]] = pd.to_datetime(df[df.columns[0]]).dt.date

    date_range = st.date_input("Select Date Range", [df[df.columns[0]].min(), df[df.columns[0]].max()])
    start_date, end_date = date_range
    date_difference = (end_date - start_date).days
    st.write(type(start_date))
    st.write(type(end_date))