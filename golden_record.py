import streamlit as st
import plotly.express as px
import pandas as pd
def golden_record():
    st.title("Golden Record Visualization for Stock Data")

    # Sample Data
    golden_record = {
        'Ticker Symbol': 'AAPL',
        'Company Name': 'Apple Inc.',
        'Current Price': '$150',
        '52-Week High': '$170',
        '52-Week Low': '$120',
        'Market Cap': '$2.4T',
        'P/E Ratio': '28.5'
    }

    source_data = {
        'Source A': {
            'Ticker Symbol': 'AAPL',
            'Company Name': 'Apple',
            'Current Price': '$151',
            '52-Week High': '$169',
            '52-Week Low': '$121',
            'Market Cap': '$2.3T',
            'P/E Ratio': '28.0'
        },
        'Source B': {
            'Ticker Symbol': 'AAPL',
            'Company Name': 'Apple Inc',
            'Current Price': '$150',
            '52-Week High': '$171',
            '52-Week Low': '$119',
            'Market Cap': '$2.5T',
            'P/E Ratio': '29.0'
        }
    }

    # Display Golden Record
    st.subheader("Golden Record")
    for key, value in golden_record.items():
        st.write(f"{key}: {value}")

   # Source Contributions
    st.subheader("Source Contributions")
    source_to_compare = st.selectbox("Select a source to compare", list(source_data.keys()))
    comparison_data = source_data[source_to_compare]

    # Create a bar chart to visualize the differences
    attributes = list(golden_record.keys())[2:]  # Exclude Ticker and Company Name for visualization
    golden_values = [golden_record[attr] for attr in attributes]
    source_values = [comparison_data[attr] for attr in attributes]

    df = pd.DataFrame({
        'Attributes': attributes,
        'Golden Record': golden_values,
        source_to_compare: source_values
    })

    fig = px.bar(df, x='Attributes', y=['Golden Record', source_to_compare], title="Comparison with Golden Record")
    st.plotly_chart(fig)

    # Highlight differences in a comparison view
    st.subheader("Detailed Comparison with Golden Record")
    for key, value in golden_record.items():
        if isinstance(value, str):
            st.write(f"{key}: {value}")
        elif comparison_data[key] == value:
            st.write(f"{key}: {value}")
        else:
            st.write(f'{key}: {value} (Source {source_to_compare}: {comparison_data[key]})', unsafe_allow_html=True)


