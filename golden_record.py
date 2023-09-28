import streamlit as st
import plotly.express as px
import pandas as pd

def golden_record():
    st.title("Golden Record Visualization for Stock Data")

    # Golden Record Sample Data
    golden_record_data = {
        'AAPL': {
            'Company Name': 'Apple Inc.',
            'Current Price': 150,
            '52-Week High': 170,
            '52-Week Low': 120,
            'Market Cap': '2.4T',
            'P/E Ratio': 28.5
        },
        'MSFT': {
            'Company Name': 'Microsoft Corporation',
            'Current Price': 290,
            '52-Week High': 310,
            '52-Week Low': 250,
            'Market Cap': '2.0T',
            'P/E Ratio': 32.1
        },
        'GOOGL': {
            'Company Name': 'Alphabet Inc.',
            'Current Price': 2800,
            '52-Week High': 2900,
            '52-Week Low': 2400,
            'Market Cap': '1.8T',
            'P/E Ratio': 30.2
        },
        'AMZN': {
            'Company Name': 'Amazon.com Inc.',
            'Current Price': 3400,
            '52-Week High': 3500,
            '52-Week Low': 3200,
            'Market Cap': '1.7T',
            'P/E Ratio': 31.0
        }
    }

    # Source Data Sample
    source_data = {
        'Source A': {
            'AAPL': {
                'Company Name': 'Apple',
                'Current Price': 151,
                '52-Week High': 169,
                '52-Week Low': 121,
                'Market Cap': '2.3T',
                'P/E Ratio': 28.0
            },
            'MSFT': {
                'Company Name': 'Microsoft Corp.',
                'Current Price': 289,
                '52-Week High': 309,
                '52-Week Low': 251,
                'Market Cap': '1.9T',
                'P/E Ratio': 32.0
            },
            'GOOGL': {
                'Company Name': 'Alphabet',
                'Current Price': 2790,
                '52-Week High': 2880,
                '52-Week Low': 2410,
                'Market Cap': '1.7T',
                'P/E Ratio': 29.9
            },
            'AMZN': {
                'Company Name': 'Amazon',
                'Current Price': 3390,
                '52-Week High': 3490,
                '52-Week Low': 3190,
                'Market Cap': '1.6T',
                'P/E Ratio': 30.5
            }
        },
        'Source B': {
            'AAPL': {
                'Company Name': 'Apple Inc',
                'Current Price': 149,
                '52-Week High': 171,
                '52-Week Low': 119,
                'Market Cap': '2.5T',
                'P/E Ratio': 29.0
            },
            'MSFT': {
                'Company Name': 'Microsoft',
                'Current Price': 288,
                '52-Week High': 307,
                '52-Week Low': 248,
                'Market Cap': '1.8T',
                'P/E Ratio': 31.8
            },
            'GOOGL': {
                'Company Name': 'Alphabet Co.',
                'Current Price': 2785,
                '52-Week High': 2875,
                '52-Week Low': 2395,
                'Market Cap': '1.6T',
                'P/E Ratio': 29.8
            },
            'AMZN': {
                'Company Name': 'Amazon Inc',
                'Current Price': 3385,
                '52-Week High': 3485,
                '52-Week Low': 3185,
                'Market Cap': '1.5T',
                'P/E Ratio': 30.3
            }
        }
    }
    st.subheader("Survivorship Rules")
    preference_order = st.selectbox("Select the source you trust more", list(source_data.keys()), index=0)

    # Let the user select which stock to visualize and compare
    selected_stock = st.selectbox("Select a stock to visualize", list(golden_record_data.keys()))

    # Update Golden Record based on preference
    for key in golden_record_data[selected_stock].keys():
        if golden_record_data[selected_stock][key] != source_data[preference_order][selected_stock][key]:
            golden_record_data[selected_stock][key] = source_data[preference_order][selected_stock][key]

    # Display Updated Golden Record
    st.subheader(f"Golden Record for {selected_stock} (Updated based on Survivorship Rules)")
    for key, value in golden_record_data[selected_stock].items():
        st.write(f"{key}: {value}")

    # Source Contributions
    st.subheader("Source Contributions")
    source_to_compare = st.selectbox("Select a source to compare", list(source_data.keys()))
    comparison_data = source_data[source_to_compare]

    # Bar chart for visualization
    attributes = list(golden_record_data[selected_stock].keys())[2:]
    golden_values = [golden_record_data[selected_stock][attr] for attr in attributes]
    source_values = [comparison_data[selected_stock][attr] for attr in attributes]

    df = pd.DataFrame({
        'Attributes': attributes,
        'Golden Record': golden_values,
        source_to_compare: source_values
    })

    fig = px.bar(df, x='Attributes', y=['Golden Record', source_to_compare], title=f"Comparison of {selected_stock} with Golden Record")
    st.plotly_chart(fig)

    # Detailed Comparison
    st.subheader(f"Detailed Comparison of {selected_stock} with Golden Record")
    for key, value in golden_record_data[selected_stock].items():
        if comparison_data[selected_stock][key] == value:
            st.write(f"{key}: {value}")
        else:
            st.write(f'{key}: {value} (Source {source_to_compare}: {comparison_data[selected_stock][key]})', unsafe_allow_html=True)