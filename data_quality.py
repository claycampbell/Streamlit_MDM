import streamlit as st
import pandas as pd
from collections import Counter
import plotly.express as px
from utilities import sfconnection, read_conf_file, queryresult
import re

# Ensure this is imported or defined in your script
# from snowflake_connection import get_snowflake_connection

def load_data_from_snowflake(ctx):
    cur = ctx.cursor()
    try:
        cur.execute("SELECT * FROM CLAUSES_CONTENT")
        rows = cur.fetchall()

        if not rows:
            st.error("No data was returned from the query.")
            return pd.DataFrame()

        if cur.description:
            columns = [x[0] for x in cur.description]
            df = pd.DataFrame(rows, columns=columns)
        else:
            st.error("Cursor description is empty, cannot set DataFrame column names.")
            return pd.DataFrame(rows)

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return pd.DataFrame()
    finally:
        cur.close()
    return df

def display_data_quality(df):
    st.header("Data Quality Monitoring")

    # Completeness
    #completeness = 100 * (1 - df.isnull().mean())
    #st.write("### Completeness")
    #st.write(completeness)

    # Uniqueness
    uniqueness_clause = 100 * (1 - df['CLAUSE'].duplicated().mean())
    uniqueness_content = 100 * (1 - df['CONTENT'].duplicated().mean())
    st.write("### Uniqueness")
    st.metric(label="Uniqueness (Clause)", value=f"{uniqueness_clause:.2f}%")
    st.metric(label="Uniqueness (Content)", value=f"{uniqueness_content:.2f}%")

    # Validity
    expected_pattern = r'your_regex_pattern_here'
    validity = 100 * df['CONTENT'].apply(lambda x: bool(re.match(expected_pattern, x)) if x is not None else False).mean()
    st.write("### Validity")
    st.metric(label="Validity (Content matches pattern)", value=f"{validity:.2f}%")

    # Anomalies & Outliers Detection
    df['content_length'] = df['CONTENT'].apply(lambda x: len(x) if x is not None else 0)
    fig = px.box(df, y='content_length', title="Content Length Outliers")
    st.plotly_chart(fig)

    # Missing Values Analysis
    missing_values = df.isnull().sum().reset_index()
    missing_values.columns = ['Column', 'MissingCount']
    missing_chart = px.bar(missing_values, x='Column', y='MissingCount', title="Missing Values by Column")
    st.plotly_chart(missing_chart)

    # Duplicity Analysis
    duplicate_rows = df[df.duplicated(['CLAUSE', 'CONTENT'], keep='first') & df['CLAUSE'].notnull() & df['CONTENT'].notnull()]
    st.write(f"Duplicate rows: {len(duplicate_rows)}")

    # Text Frequency Analysis
    clause_counts = Counter(df['CLAUSE'].dropna())
    content_counts = Counter(df['CONTENT'].dropna())
    st.write("### Text Frequency Analysis")
    st.write("Most common clauses:", clause_counts.most_common(5))
    st.write("Most common contents:", content_counts.most_common(5))

    # Interactive Filters
    search_query = st.text_input("Search for clauses or content")
    if search_query:
        filtered_data = df[(df['CLAUSE'].notnull() & df['CLAUSE'].str.contains(search_query)) |
                           (df['CONTENT'].notnull() & df['CONTENT'].str.contains(search_query))]
        st.write(filtered_data)

if 'snowflake_ctx' in st.session_state:
    data = load_data_from_snowflake(st.session_state['snowflake_ctx'])
    display_data_quality(data)
else:
    st.error("Snowflake connection not established.")

data = load_data_from_snowflake(st.session_state.snowflake_ctx)
display_data_quality(data)
