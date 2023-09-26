import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import base64
# Sample financial data
@st.cache_data
def generate_data():
    dates = pd.date_range("20210101", periods=100)
    companies = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']
    df = pd.DataFrame({
        'Date': np.tile(dates, len(companies)),
        'Company': np.repeat(companies, len(dates)),
        'Open': np.random.rand(400) * 100,
        'Close': np.random.rand(400) * 100
    })
    return df

df = generate_data()

def interactive_data_exploration():
    st.header("Interactive Data Exploration")

    # Sample financial data
    data = {
        'Date': pd.date_range(start='1/1/2022', periods=100, freq='D'),
        'Stock Price': (pd.Series(1 + (0.01 * np.random.randn(100))).cumprod() * 100),
        'Volume': np.random.randint(5000, 20000, size=100)
    }

    # Select the type of chart
    chart_type = st.selectbox("Choose a chart type", ["Line", "Bar", "Scatter"])

    # Select the X and Y axis for the chart
    x_axis = st.selectbox("Choose X-axis data", df.columns)
    y_axis = st.selectbox("Choose Y-axis data", df.columns)

    # Create the chart
    if chart_type == "Line":
        fig = px.line(df, x=x_axis, y=y_axis)
    elif chart_type == "Bar":
        fig = px.bar(df, x=x_axis, y=y_axis)
    elif chart_type == "Scatter":
        fig = px.scatter(df, x=x_axis, y=y_axis)

    # Display the chart
    st.plotly_chart(fig)

    # Drill-down capabilities
    if st.button('Show Detailed Records'):
        number_of_records = st.slider("Select number of records", 1, len(df), 5)
        st.dataframe(df.head(number_of_records))
# Generate mock data
# Filtering Data
    min_open, max_open = st.slider('Filter data by Open Value', float(df['Open'].min()), float(df['Open'].max()), [float(df['Open'].min()), float(df['Open'].max())])
    filtered_data = df[(df['Open'] >= min_open) & (df['Open'] <= max_open)]

    # Histograms
    if st.checkbox('Show Histograms'):
        histogram_col = st.selectbox('Choose a column for histogram', ['Open', 'Close'])
        fig = px.histogram(filtered_data, x=histogram_col, color='Company', marginal="box", title=f"Histogram for {histogram_col}")
        st.plotly_chart(fig)

    # Data Aggregation
    if st.checkbox('Group data by Company'):
        grouped_data = filtered_data.groupby('Company').mean()
        st.write(grouped_data)

    # Search Bar
    search_term = st.text_input("Search data:")
    if search_term:
        search_results = df[df.apply(lambda row: row.astype(str).str.contains(search_term).any(), axis=1)]
        st.write(search_results)

    # Comparative Analysis
    if st.checkbox('Compare Columns'):
        col1, col2 = st.multiselect('Select two columns', ['Open', 'Close'], default=['Open', 'Close'])
        fig2 = px.scatter(filtered_data, x=col1, y=col2, color='Company', title=f"{col1} vs {col2}")
        st.plotly_chart(fig2)

    # Data Export
    if st.button('Download Data as CSV'):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
        href = f'<a href="data:file/csv;base64,{b64}">Download CSV File</a>'
        st.markdown(href, unsafe_allow_html=True)

    # Statistical Summaries
    if st.checkbox('Show Statistical Summary'):
        st.write(filtered_data.describe())


