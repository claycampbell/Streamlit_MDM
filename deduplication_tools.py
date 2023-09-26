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
        'MSFT': ['Microsoft Corp.', 290, 'Tech'],
        'GOOGL': ['Alphabet Inc.', 2800, 'Tech'],
        'GOOGLE': ['Alphabet Inc.', 2801, 'Tech'],
        'AMZN': ['Amazon.com Inc.', 3400, 'E-commerce'],
        'AMZON': ['Amazon.com Inc.', 3401, 'E-commerce']
    }

    df = pd.DataFrame.from_dict(data, orient='index', columns=['Company Name', 'Current Price', 'Sector'])
    
    # Step 1: Selection of Dataset
    # Here, I'm using a single dataset for demonstration. In a real-world application, you would provide options.
    st.write(df)

    # Step 2: Deduplication Criteria
    st.subheader("Deduplication Criteria")
    columns_to_check = st.multiselect("Select columns to identify duplicates", list(df.columns), default=list(df.columns))

    # Identify duplicates based on the selected columns
    mask = df.duplicated(subset=columns_to_check, keep=False)
    if mask.any(): # This is where we ensure we don't evaluate a Series directly in boolean context
        duplicate_df = df[mask]
        
        # Step 3: Display Duplicate Records
        st.subheader("Duplicate Records")
        st.write(duplicate_df)

        # Step 4: Actions on Duplicates
        st.subheader("Actions")
        if st.button("Merge Duplicates"):
            # Logic to merge duplicates; for now, a simple message
            st.success("Duplicates Merged!")

        if st.button("Delete Duplicates"):
            # Logic to delete duplicates; for now, a simple message
            st.success("Duplicates Deleted!")

        # Step 5: Visualization
        st.subheader("Visualization")
        dup_count = duplicate_df['Company Name'].value_counts()
        fig = px.bar(x=dup_count.index, y=dup_count.values, title="Companies with most duplicates", labels={'x': 'Company Name', 'y': 'Number of duplicates'})
        st.plotly_chart(fig)
    else:
        st.write("No duplicates found based on the selected criteria.")