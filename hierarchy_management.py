import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

def display_hierarchy_management (data):

    st.header("Hierarchy Management for Financial Stocks")
    
    # Sample hierarchy for a financial services company (This should be replaced with actual hierarchy data)
    G = nx.DiGraph()
    G.add_edges_from([
        ('All Markets', 'US Market'), 
        ('US Market', 'Tech Stocks'), ('Tech Stocks', 'Apple'), ('Tech Stocks', 'Microsoft'),
        ('US Market', 'Health Stocks'), ('Health Stocks', 'Pfizer'), ('Health Stocks', 'Johnson & Johnson'),
        ('All Markets', 'European Market'),
        ('European Market', 'Automobile Stocks'), ('Automobile Stocks', 'Volkswagen'), ('Automobile Stocks', 'BMW')
    ])
    
    # Define colors for nodes based on their hierarchy level
    color_map = {
        'All Markets': 'purple',
        'US Market': 'blue',
        'European Market': 'blue',
        'Tech Stocks': 'green',
        'Health Stocks': 'green',
        'Automobile Stocks': 'green',
        'Apple': 'yellow',
        'Microsoft': 'yellow',
        'Pfizer': 'yellow',
        'Johnson & Johnson': 'yellow',
        'Volkswagen': 'yellow',
        'BMW': 'yellow'
    }
    colors = [color_map[node] for node in G.nodes()]
    
    # Display the hierarchy using networkx and matplotlib
    st.subheader("Hierarchy Visualization for Financial Markets")
    pos = nx.spring_layout(G)
    fig, ax = plt.subplots(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_size=4000, node_color=colors, ax=ax)
    st.pyplot(fig)

    # Tools to manage the hierarchy
    st.subheader("Manage Stock Hierarchies")

    # List of nodes for selection (Replace with actual data nodes)
    nodes = list(G.nodes())
    
    col1, col2 = st.columns(2)
    
    node_to_merge_1 = col1.selectbox("Select first node to merge:", nodes)
    node_to_merge_2 = col2.selectbox("Select second node to merge:", nodes)
    
    if st.button("Merge Nodes"):
        # Logic to merge nodes in the hierarchy
        st.success(f"Merged {node_to_merge_1} and {node_to_merge_2}")

    node_to_split = st.selectbox("Select a node to split:", nodes)
    if st.button("Split Node"):
        # Logic to split node in the hierarchy
        st.success(f"Split {node_to_split} into ...")

# Sample call to the function
# hierarchy_management(data)
