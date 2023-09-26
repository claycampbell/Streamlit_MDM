import networkx as nx
from pyvis.network import Network
import streamlit as st

def display_data_lineage():
    st.header("Data Lineage Visualization")
    
    # One-line description
    st.write("Data lineage provides a visual representation of data's journey across systems and transformations.")
    
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes for sources, processes, and datasets with realistic names
    sources = ["Bloomberg", "Reuters", "Bank Transactions", "ERP System", "CRM System", "Stock Exchange Feed", "Excel Reports"]
    processes = ["Data Cleansing", "Currency Conversion", "Aggregation", "Enrichment", "Anomaly Detection"]
    datasets_lineage = ["Quarterly Financial Reports", "Customer Financial Profiles", "Real-time Stock Dashboards", "Fraud Alert System", "Annual Financial Statements"]

    # Add nodes with color attributes
    for node in sources:
        G.add_node(node, color='blue', type='source', title=f"Details about {node}")
    for node in processes:
        G.add_node(node, color='green', type='process', title=f"Details about {node}")
    for node in datasets_lineage:
        G.add_node(node, color='red', type='dataset', title=f"Details about {node}")

    # Define a sample of the data flow edges (this can be extended further for a more intricate flow)
    edges = [("Bloomberg", "Data Cleansing"),
             ("Reuters", "Data Cleansing"),
             ("Bank Transactions", "Currency Conversion"),
             ("ERP System", "Aggregation"),
             ("CRM System", "Enrichment"),
             ("Stock Exchange Feed", "Real-time Stock Dashboards"),
             ("Excel Reports", "Quarterly Financial Reports"),
             ("Data Cleansing", "Quarterly Financial Reports"),
             ("Currency Conversion", "Annual Financial Statements"),
             ("Aggregation", "Customer Financial Profiles"),
             ("Enrichment", "Fraud Alert System"),
             ("Anomaly Detection", "Fraud Alert System")]

    for edge in edges:
        G.add_edge(*edge)

    # Visualize the graph using pyvis
    nt = Network(notebook=True)
    nt.from_nx(G)
    
    # Legend & Documentation
    st.write("Legend:")
    st.write("🔵: Data Source")
    st.write("🟢: ETL Process")
    st.write("🔴: Final Dataset")
    st.write("---")

    nt.show("data_lineage.html")

    # Display in Streamlit
    st.components.v1.html(open("data_lineage.html").read(), width=800, height=800)
