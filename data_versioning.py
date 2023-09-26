import streamlit as st
import pandas as pd
import numpy as np

# Sample data versioning structure (In reality, this could be more complex and backed by a database)
VERSIONS = {
    "v1": pd.DataFrame({
        'Stock': ['Apple', 'Microsoft', 'Pfizer'],
        'Price': [130, 240, 40]
    }),
    "v2": pd.DataFrame({
        'Stock': ['Apple', 'Microsoft', 'Pfizer', 'BMW'],
        'Price': [135, 242, 40, 80]
    }),
    "v3": pd.DataFrame({
        'Stock': ['Apple', 'Microsoft', 'Pfizer', 'Volkswagen'],
        'Price': [138, 245, 42, 85]
    })
}

def data_versioning():
    st.header("Data Versioning")

    st.subheader("Available Versions")
    version_selected = st.selectbox("Select a version", list(VERSIONS.keys()))

    st.subheader("Dataset for the selected version")
    st.write(VERSIONS[version_selected])

    col1, col2 = st.columns(2)

    version_1 = col1.selectbox("Compare Version 1", list(VERSIONS.keys()))
    version_2 = col2.selectbox("Compare Version 2", list(VERSIONS.keys()))

    if st.button("Compare Versions"):
        # This is a basic comparison. In a real application, we could highlight changed rows/cells.
        df_diff = pd.concat([VERSIONS[version_1], VERSIONS[version_2]]).drop_duplicates(keep=False)
        st.write(df_diff)

    if st.button("Rollback to Selected Version"):
        # Logic to rollback to the selected version
        st.success(f"Rolled back to version {version_selected}")

    if st.button("Save Current as New Version"):
        # Logic to save the current state as a new version (e.g., "v4")
        new_version = "v" + str(len(VERSIONS) + 1)
        VERSIONS[new_version] = VERSIONS[version_selected].copy()
        st.success(f"Saved current state as {new_version}")
    # Create two columns
    col1, col2 = st.columns(2)

    # 1. Version Metadata
    with col1:
        st.subheader("Version Metadata")
        version_selected = st.selectbox("Select Version", options=["Version 1", "Version 2", "Version 3"])
        st.write(f"Selected: {version_selected}")
        st.write("Created by: John Doe")
        st.write("Created on: 01 Jan 2023")
        st.write("Reason: Initial version")

    # 2. Annotations/Comments
    with col2:
        st.subheader("Annotations/Comments")
        st.text_area("Add your comment or annotation for this version:", value="", max_chars=None, key=None)

    # 3. Differential View
    with col1:
        st.subheader("Differential View")
        st.write("Differential between Version 1 and Version 2: +2 rows, -1 row, 3 cells modified")

    # 4. Version History Visualization
    with col2:
        st.subheader("Version History Visualization")
        st.line_chart([1, 3, 2])

    # 5. Tagging and Bookmarking
    with col1:
        st.subheader("Tagging and Bookmarking")
        st.write("Tags: [Initial], [Post-Q1]")
        st.button("Add Tag")

    # 6. Automated Version Summaries
    with col2:
        st.subheader("Automated Version Summaries")
        st.write("Version 1: 3 rows added, 2 rows deleted, 5 cells modified.")

    # 8. Alerts on Version Changes
    with col1:
        st.subheader("Alerts on Version Changes")
        st.checkbox("Notify me about changes to this version")

    # 9. Export/Download
    with col2:
        st.subheader("Export/Download")
        st.button("Download Selected Version")

    # 11. Version Search
    with col1:
        st.subheader("Version Search")
        st.text_input("Search for versions")

    # 12. Backups and Recovery
    with col2:
        st.subheader("Backups and Recovery")
        st.button("Backup Current Version")
        st.button("Recover Version")

    # 13. Access Control and Permissions
    with col1:
        st.subheader("Access Control and Permissions")
        st.multiselect("Select users with access", options=["User A", "User B", "User C"])

    # 15. Batch Version Operations
    with col2:
        st.subheader("Batch Version Operations")
        st.checkbox("Select Version 1")
        st.checkbox("Select Version 2")
        st.button("Rollback Selected Versions")

    # 16. Validation and Testing
    with col1:
        st.subheader("Validation and Testing")
        st.button("Validate Current Version")