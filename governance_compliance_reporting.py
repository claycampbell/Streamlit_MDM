import streamlit as st
import pandas as pd
from datetime import datetime

def governance_compliance_reporting():
    st.title("Governance and Compliance Reporting")

    # Sample Data
    compliance_data = {
        "Regulation": ["GDPR", "CCPA", "HIPAA"],
        "Status": ["Compliant", "Non-Compliant", "In Review"]
    }

    audit_trail_data = {
        "Timestamp": [datetime.now(), datetime.now() - pd.Timedelta(hours=5), datetime.now() - pd.Timedelta(days=1)],
        "User": ["User_A", "User_B", "User_C"],
        "Action": ["Modified Data", "Accessed Data", "Deleted Record"]
    }

    # Tracking Compliance
    st.subheader("Compliance Status")
    compliance_df = pd.DataFrame(compliance_data)
    st.table(compliance_df)

    # Audit Trails
    st.subheader("Audit Trails")
    audit_trail_df = pd.DataFrame(audit_trail_data)
    st.table(audit_trail_df.sort_values(by="Timestamp", ascending=False))

    # Reports
    st.subheader("Generate Reports")
    report_option = st.selectbox("Choose a report type", ["Compliance Overview", "Recent Actions", "Potential Issues"])
    if st.button("Generate Report"):
        st.write(f"Generating report for: {report_option}")
        # Logic for generating and displaying the chosen report goes here
        if report_option == "Compliance Overview":
            st.write(compliance_df)
        elif report_option == "Recent Actions":
            st.write(audit_trail_df)
        else:
            st.write("Potential issues report is still under development.")

    # Additional features can be added such as filters for the audit trail logs, detailed insights on non-compliance, etc.

if __name__ == "__main__":
    governance_compliance_reporting()
