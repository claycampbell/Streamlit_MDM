import streamlit as st
import pandas as pd

# For demonstration, using a simple dictionary to store tags and descriptions.
# In a real scenario, this can be replaced with a database or another persistent storage.
metadata_storage = {
    'tags': {},
    'descriptions': {}
}

def display_metadata_management(data):
    st.title("Metadata Management")

    # Dataset Listings
    dataset_name = st.selectbox("Select a dataset", list(data.keys()))
    selected_dataset = data[dataset_name]

    # Display and Add Tags
    st.markdown("## Tags")
    existing_tags = metadata_storage['tags'].get(dataset_name, [])
    st.write("Existing Tags:", ', '.join(existing_tags))
    
    new_tag = st.text_input("Add a new tag:")
    if st.button("Add Tag"):
        if dataset_name not in metadata_storage['tags']:
            metadata_storage['tags'][dataset_name] = []
        metadata_storage['tags'][dataset_name].append(new_tag)
        st.success(f"Tag '{new_tag}' added!")
    
    # Field Descriptions and Tags
    st.markdown("## Field Descriptions and Tags")
    column_name = st.selectbox("Select a column", selected_dataset.columns)
    col_description = st.text_area("Description", metadata_storage['descriptions'].get(column_name, ""))
    col_tag = st.text_input("Add tag for this column")
    
    if st.button("Save Description and Tag"):
        metadata_storage['descriptions'][column_name] = col_description
        if column_name not in metadata_storage['tags']:
            metadata_storage['tags'][column_name] = []
        metadata_storage['tags'][column_name].append(col_tag)
        st.success(f"Description and tag for '{column_name}' saved!")

    # Display table with columns, descriptions, and tags
    st.markdown("## Table Overview")
    table_data = {
        "Column Name": selected_dataset.columns,
        "Description": [metadata_storage['descriptions'].get(col, "") for col in selected_dataset.columns],
        "Tags": [', '.join(metadata_storage['tags'].get(col, [])) for col in selected_dataset.columns]
    }
    st.table(pd.DataFrame(table_data))

