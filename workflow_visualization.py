import streamlit as st
import pandas as pd

def workflow_visualization():
    st.title("Workflow Visualization")

    # Sample Data
    workflow_stages = ["Data Collection", "Processing", "Review", "Approval", "Publication"]
    current_stage = "Review"

    tasks_awaiting_approval = {
        "Task ID": [101, 102, 103],
        "Task Description": ["Review Data Collection Method", "Approve New Data Source", "Finalize Processed Data"],
        "Submitted By": ["Alice", "Bob", "Charlie"],
        "Submitted On": ["2023-09-24", "2023-09-25", "2023-09-26"]
    }

    # Workflow Status Overview
    st.subheader("Workflow Status Overview")
    for stage in workflow_stages:
        if stage == current_stage:
            st.write(f"🔵 {stage} (Current Stage)")
        else:
            st.write(stage)

    # Pending Approvals
    st.subheader("Pending Approvals")
    pending_approvals_df = pd.DataFrame(tasks_awaiting_approval)
    st.table(pending_approvals_df)

    # Bottlenecks Identification (For simplicity, we assume Review is the bottleneck)
    st.subheader("Bottlenecks Identification")
    st.write("🔴 Review Stage has a prolonged wait time. Consider expediting review processes or allocate more resources.")

    # The above is a basic visualization. In a complete solution, dynamic data would be used, and visual aids like graphs would be more interactive.


