import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

# Sample storage for demonstration.
reference_data_storage = {
    'global_data': {
        "Countries": pd.DataFrame({
            'Code': ['US', 'CA', 'UK'],
            'Name': ['United States', 'Canada', 'United Kingdom'],
            'Description': ['', '', '']
        }),
        "States": pd.DataFrame({
            'Code': ['CA', 'TX', 'NY'],
            'Name': ['California', 'Texas', 'New York'],
            'Description': ['', '', '']
        })
    },
    'translate_data': {
        "Gender": pd.DataFrame({
            'Code': ['M', 'F', 'U', 'B', 'O'],
            'Name': ['Male', 'Female', 'Unknown', 'Both', 'Other'],
            'Description': ['', '', '', '', ''],
            'SRC': ['SRC_A', 'SRC_B', 'SRC_C', 'SRC_D', 'SRC_E'],
            'SRC_CD': ['1', '2', '3', '4', '5'],
            'Start_Date': ['', '', '2000-01-01', '', ''],
            'End_Date': ['', '', '2003-12-31', '', '']
        })
    }
}

def display_reference_data_management():
    st.title("Reference Data Management")

    # Reference Table Type Selection
    reference_type = st.selectbox("Select Reference Table Type", ["Global", "Translate"])

    # Global Reference Tables
    if reference_type == "Global":
        st.markdown("## Global Reference Tables")

        # Dropdown to select an existing global reference or create a new one
        global_table_name = st.selectbox("Choose or create a global table", list(reference_data_storage['global_data'].keys()) + ["Create New..."])
        if global_table_name == "Create New...":
            global_table_name = st.text_input("Enter the name for the new Global Table:")
            if st.button("Create New Global Table"):
                reference_data_storage['global_data'][global_table_name] = pd.DataFrame(columns=["Code", "Name", "Description"])
        
        if global_table_name in reference_data_storage['global_data']:
            AgGrid(reference_data_storage['global_data'][global_table_name])

    # Translate Reference Tables
    else:
        st.markdown("## Translate Reference Tables")

        # Dropdown to select an existing translation reference or create a new one
        translate_table_name = st.selectbox("Choose or create a translation table", list(reference_data_storage['translate_data'].keys()) + ["Create New..."])
        if translate_table_name == "Create New...":
            translate_table_name = st.text_input("Enter the name for the new Translation Table:")
            if st.button("Create New Translation Table"):
                reference_data_storage['translate_data'][translate_table_name] = pd.DataFrame(columns=["Code", "Name", "Description", "SRC", "SRC_CD", "Start_Date", "End_Date"])

        if translate_table_name in reference_data_storage['translate_data']:
            AgGrid(reference_data_storage['translate_data'][translate_table_name])

    # Save changes button
    if st.button("Save Changes"):
        st.success("Changes saved successfully!")

# Call the function to display the reference data management page
display_reference_data_management()