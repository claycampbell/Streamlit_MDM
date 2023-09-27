import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

# For demonstration, using a simple dictionary to store tags and descriptions.
# In a real scenario, this can be replaced with a database or other persistent storage.
metadata_storage = {
    'tags': {},
    'descriptions': {}
}

def display_metadata_management(data):
    st.title("Metadata Management")

    # Dataset Listings
    dataset_name = st.selectbox("Select a dataset", list(data.keys()))
    selected_dataset = data[dataset_name]

    # 1. Display and Add Tags for Datasets
    st.markdown("## Dataset Tags")
    existing_tags = metadata_storage['tags'].get(dataset_name, [])
    st.write("Existing Tags for the dataset:", ', '.join(existing_tags))
    
    new_tag = st.text_input("Add a new tag for the dataset:")
    if st.button("Add Dataset Tag"):
        if dataset_name not in metadata_storage['tags']:
            metadata_storage['tags'][dataset_name] = []
        metadata_storage['tags'][dataset_name].append(new_tag)
        st.success(f"Tag '{new_tag}' added for the dataset!")

    # 2. Field Descriptions and Tags
    st.markdown("## Column Descriptions and Tags")
    column_name = st.selectbox("Select a column", selected_dataset.columns)
    col_description = st.text_area("Description", metadata_storage['descriptions'].get(column_name, ""))
    col_tag = st.text_input(f"Add tag for the column '{column_name}'")
    
    if st.button("Save Column Description and Tag"):
        metadata_storage['descriptions'][column_name] = col_description
        if column_name not in metadata_storage['tags']:
            metadata_storage['tags'][column_name] = []
        metadata_storage['tags'][column_name].append(col_tag)
        st.success(f"Description and tag for column '{column_name}' saved!")

    # Display table with columns, descriptions, and tags using ag-grid
    st.markdown("## Table Overview")
    
    table_data = {
        "Column Name": selected_dataset.columns,
        "Description": [metadata_storage['descriptions'].get(col, "") for col in selected_dataset.columns],
        "Tags": [', '.join(metadata_storage['tags'].get(col, [])) for col in selected_dataset.columns]
    }
    df_table_data = pd.DataFrame(table_data)

    # Configure grid options for ag-grid
    gridOptions = {
        'defaultColDef': {
            'editable': True,
            'resizable': True
        },
        'columnDefs': [
            {'field': 'Column Name', 'editable': False},
            {'field': 'Description'},
            {'field': 'Tags'}
        ]
    }

    # Display the grid with ag-grid and get the returned data
    grid_return = AgGrid(df_table_data, gridOptions=gridOptions, height=300, width='100%', 
                         return_mode_values='AS_INPUT', update_mode='VALUE_CHANGED', 
                         fit_columns_on_grid_load=True, key='grid')

    if 'data' in grid_return:
        updated_data = grid_return['data']
        st.write(updated_data)

        # Update metadata_storage with any changes made in the grid
        for idx, row in updated_data.iterrows():
            column_name = row['Column Name']
            metadata_storage['descriptions'][column_name] = row['Description']
            metadata_storage['tags'][column_name] = row['Tags'].split(', ')
    else:
        st.error('Failed to retrieve updated data from the grid.')

