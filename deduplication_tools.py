import streamlit as st
import pandas as pd
import plotly.express as px

def deduplication_tools():
    st.title("Deduplication Tools for Stock Data")

    # Sample Data for a financial company
    data = {
        'AAPL': ['Apple Inc.', 150, 'Tech'],
        'AAPLE': ['Apple Inc.', 151, 'Tech'],
        'MSFT': ['Microsoft Corp.', 290, 'Tech'],
        'GOOGL': ['Alphabet Inc.', 2800, 'Tech'],
        'GOOGLE': ['Alphabet Inc.', 2801, 'Tech'],
        'AMZN': ['Amazon.com Inc.', 3400, 'E-commerce'],
        'AMZON': ['Amazon.com Inc.', 3401, 'E-commerce']
    }

    df = pd.DataFrame.from_dict(data, orient='index', columns=['Company Name', 'Current Price', 'Sector'])
    
    st.write(df)

    # Deduplication Method
    st.subheader("Deduplication Method")
    dedup_method = st.radio("Choose deduplication method:", ["Deterministic", "Probabilistic"])
    
    # Deduplication Criteria
    st.subheader("Deduplication Criteria")
    columns_to_check = st.multiselect("Select columns to identify duplicates", list(df.columns), default=list(df.columns))

    # Identify duplicates
    if dedup_method == "Deterministic":
        mask = df.duplicated(subset=columns_to_check, keep=False)
    else:
        st.warning("Probabilistic deduplication is not implemented yet!")
        return

    if mask.any():
        duplicate_df = df[mask]
        st.subheader("Duplicate Records")
        st.write(duplicate_df)

        # Actions on Duplicates
        st.subheader("Actions")
        if st.button("Merge Duplicates"):
            st.success("Duplicates Merged!")

        if st.button("Delete Duplicates"):
            st.success("Duplicates Deleted!")

        # Visualization
        st.subheader("Visualization")
        dup_count = duplicate_df['Company Name'].value_counts()
        fig = px.bar(x=dup_count.index, y=dup_count.values, title="Companies with most duplicates", labels={'x': 'Company Name', 'y': 'Number of duplicates'})
        st.plotly_chart(fig)
    else:
        st.write("No duplicates found based on the selected criteria.")
