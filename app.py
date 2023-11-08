import streamlit as st
from utilities.sf_operations import Snowflakeconnection

# Create an instance of Snowflakeconnection
connection_utility = Snowflakeconnection(profilename='snowflake_host')

# Use the instance to establish a connection
sfconnectionresults = connection_utility.get_snowflake_connection()

# Now sfconnectionresults should have the 'connection' object, status code, and status message
sfconnection = sfconnectionresults.get('connection')
statuscode = sfconnectionresults.get('statuscode')
statusmessage = sfconnectionresults.get('statusmessage')

# Check if the Snowflake connection already exists in the session state
if 'snowflake_ctx' not in st.session_state:
    # Establish a new connection and store it in the session state
    sfconnectionresults = connection_utility.get_snowflake_connection()
    sfconnection = sfconnectionresults.get('connection')
    st.session_state.snowflake_ctx = sfconnection

    # Handle the status code and message
    statuscode = sfconnectionresults.get('statuscode')
    statusmessage = sfconnectionresults.get('statusmessage')
    if statuscode != "Expected_success_code":  # Replace with your actual success code
        st.error(f"Failed to establish Snowflake connection: {statusmessage}")
    else:
        st.success(f"Connected to Snowflake: {statusmessage}")

import pandas as pd
import plotly.express as px
import numpy as np
from constants import constants

import datetime
import data_profiling
import data_lineage
import data_quality
import hierarchy_management
import data_versioning
import golden_record
import deduplication_tools
import governance_compliance_reporting
import workflow_visualization
import interactive_data_exploration
import ai_anomaly_detection
import ai_rules
import metadata_management
import reference_data_management

# Load the generated datasets
st.markdown(
    """
<style>
    .appview-container .main .block-container{
        max-width: 1200px !important;
        padding-top: 3rem !important;
        
    }
   
    .stApp{
    background-color: #fcfcfc !important;  # This sets the background color to white
    }
    @media (prefers-color-scheme: dark) {
    .appview-container .main {
        color: #FFFFFF; /* Adjust as needed */
        background-color: #111111; /* Adjust as needed */
        }
</style>
""",
    unsafe_allow_html=True,
)

@st.cache_data  # 👈 Use the caching decorator
def load_data():
    datasets = {
        "Stock Data": "stock_data.csv",
        "Stock Sector Information": "stock_sector_information.csv",
        "Mutal Funds": "mutalfund.csv",
        "Data Overview": "data_overview.csv",
        "Data Completeness": "data_completeness.csv",
        "Data Accuracy": "data_accuracy.csv",
        "Rule Management": "rule_management.csv",
        "AI Insights": "ai_insights.csv",
        "User Feedback": "user_feedback.csv",
        "Notifications": "notifications.csv",
        "Audit History": "audit_history.csv"       
        
    }
    print(type(datasets))
    print(datasets)
    return {name: pd.read_csv(file) for name, file in datasets.items()}
   

data = load_data()
companies = ["TechCorp", "HealthInc"]


# Title

features = [
    "KPI Overview", 
    "Data Profiling", 
    "Data Lineage ",
    "Data Quality", 
    "Hierarchy Management", 
    "Data Versioning", 
    "Data Stewardship", 
    "Deduplication Tools", 
    "Golden Record", 
    "Governance and Compliance", 
    "Integration Health", 
    "Reference Data Management", 
    "Workflow Visualization", 
    "Interactive Data Exploration", 
    "Search and Discovery", 
    "Notifications and Alerts", 
    "Role-based Access Control", 
    "Data Quality Scorecards",
    "Anomaly Detection",
    "AI Rules",
    "Metadata Management",
    "Reference Data Management"
]
feature_icons = {
    "KPI Overview": "📊",
    "Data Profiling": "🔍",
    "Data Lineage": "🔗",
    "Data Quality": "✅",
    "Hierarchy Management": "🌳",
    "Data Versioning": "🔄",
    "Data Stewardship": "👮",
    "Deduplication Tools": "🔧",
    "Golden Record": "📀",
    "Governance and Compliance": "📑",
    "Integration Health": "💊",
    "Reference Data Management": "📚",
    "Workflow Visualization": "📝",
    "Interactive Data Exploration": "🔬",
    "Search and Discovery": "🔎",
    "Notifications and Alerts": "🚨",
    "Role-based Access Control": "🔒",
    "Data Quality Scorecards": "📜",
    "Anomaly Detection": "⚠️",
    "AI Rules": "🔨",
    "Metadata Management": "📋",
    "Reference Data Management":"📋"

}

# Grouped features for better organization
FEATURE_GROUPS = {
    "🗃️ Data Management": ["KPI Overview", "Data Profiling", "Data Lineage", "Data Quality","Metadata Management","Reference Data Management"],
    "🛠️ Tools & Control": ["Hierarchy Management", "Data Versioning", "Deduplication Tools", "Golden Record","Interactive Data Exploration"],
    "📈 Reporting": ["Governance and Compliance","Workflow Visualization"],
    "🤖 AI": ["Anomaly Detection","AI Rules"],

    # Add more groups as needed...
}


# Use the connection throughout the app
# Example: pass it to another module that requires the connection
# some_module.some_function(st.session_state.snowflake_ctx)
def display_feature_buttons():
    selected_feature = None

    main_columns = st.columns(2)
    for index, (group, group_features) in enumerate(FEATURE_GROUPS.items()):

        col = main_columns[index % 2]
        with col:
            st.markdown(f"## {group}")

            # Adjusting number of columns based on the number of features in the group
            if len(group_features) <= 3:
                num_columns = 3
            else:
                num_columns = 4  # or even 5 if you want more columns

            feature_columns = st.columns(num_columns)

            for feature_index, feature in enumerate(group_features):
                feature_col = feature_columns[feature_index % num_columns]
                icon = feature_icons.get(feature, "")
                # Adjusting the button text for some of the longer labels
                adjusted_feature_name = feature.replace("Deduplication Tools", "Deduplication")\
                                               .replace("Governance and Compliance", "Governance & Compliance")\
                                               .replace("Interactive Data Exploration", "Data Exploration")\
                                               .replace("Notifications and Alerts", "Notifications")
                
                if feature_col.button(f"{icon} {adjusted_feature_name}"):
                    selected_feature = feature

    return selected_feature


def display_kpis():
    dates = pd.date_range(datetime.date.today() - datetime.timedelta(days=9), periods=10)
    companies = ["TechCorp", "HealthInc", "EduGroup", "FinServe"]

    # Data Volume Overview
    data_overview = pd.DataFrame({
        'Date': dates,
        'TechCorp': np.random.randint(8000, 10000, 10),
        'HealthInc': np.random.randint(6000, 8000, 10),
        'EduGroup': np.random.randint(4000, 6000, 10),
        'FinServe': np.random.randint(2000, 4000, 10)
    })

    # Data Completeness
    data_completeness = pd.DataFrame({
        'Company': companies,
        'Missing_Data': np.random.randint(50, 200, 4)
    })

    # Data Accuracy
    data_accuracy = pd.DataFrame({
        'Company': np.random.choice(companies, 100),
        'Correction_Type': np.random.choice(["Type A", "Type B", "Type C"], 100)
    })

    # Rule Management
    rule_management = pd.DataFrame({
        'Rule': np.random.choice(["Rule 1", "Rule 2", "Rule 3"], 100)
    })

    # AI Insights
    ai_insights = pd.DataFrame({
        'Date': dates,
        'TechCorp_Predicted': np.random.randint(8000, 10000, 10),
        'HealthInc_Predicted': np.random.randint(6000, 8000, 10)
    })

    # User Feedback
    user_feedback = pd.DataFrame({
        'User': np.random.choice(["User A", "User B", "User C"], 100),
        'Feedback_Type': np.random.choice(["Positive", "Neutral", "Negative"], 100)
    })

    # Notifications
    notifications = pd.DataFrame({
        'Alert_Type': np.random.choice(["Critical", "Warning", "Info"], 100)
    })

    # Audit & History
    audit_history = pd.DataFrame({
        'Change_Type': np.random.choice(["Addition", "Deletion", "Modification"], 100),
        'Timestamp': pd.date_range(datetime.date.today() - datetime.timedelta(days=99), periods=100)
    })

    # Combining all mock data into a dictionary
    data = {
        "Data Overview": data_overview,
        "Data Completeness": data_completeness,
        "Data Accuracy": data_accuracy,
        "Rule Management": rule_management,
        "AI Insights": ai_insights,
        "User Feedback": user_feedback,
        "Notifications": notifications,
        "Audit History": audit_history
    }
    st.header("Key Performance Indicators")

    # Data Overview KPI
    st.subheader("Data Volume Overview")
    cols1 = st.columns(2)
    latest_data = data["Data Overview"].tail(10)
    fig = px.line(latest_data, x="Date", y=companies, title="Recent Data Volume Trend")
    cols1[0].plotly_chart(fig)

    # Data Completeness KPI
    # Data Completeness KPI
    st.subheader("Data Completeness")
   

    # Visualize the missing data directly from the data_completeness DataFrame
    fig = px.bar(data_completeness, x="Company", y="Missing_Data", title="Missing Data Points by Company")
    cols1[1].plotly_chart(fig)


    # Data Accuracy KPI
    st.subheader("Data Accuracy")
    cols2 = st.columns(2)
    corrections = data["Data Accuracy"]["Company"].value_counts()
    fig = px.bar(corrections, title="Number of Corrections by Company", orientation='h')
    cols2[0].plotly_chart(fig)

    # Rule Management KPI
    rule_counts = data["Rule Management"]["Rule"].value_counts()
    fig = px.pie(names=rule_counts.index, values=rule_counts.values, title="Distribution of Rule Triggers")
    cols2[1].plotly_chart(fig)

    # AI Insights KPI
    st.subheader("AI Insights Trend")
    cols3 = st.columns(2)
    latest_predictions = data["AI Insights"].tail(10)
    fig = px.line(latest_predictions, x="Date", y=["TechCorp_Predicted", "HealthInc_Predicted"])
    cols3[0].plotly_chart(fig)

    # User Feedback KPI
    feedback_counts = data["User Feedback"]["User"].value_counts()
    fig = px.histogram(x=feedback_counts.values, labels={'x': 'Users', 'y': 'Feedback Count'})
    cols3[1].plotly_chart(fig)

    # Notifications & Alerts KPI
    st.subheader("Notifications & Alerts")
    cols4 = st.columns(2)
    alert_counts = data["Notifications"]["Alert_Type"].value_counts()
    fig = px.pie(names=alert_counts.index, values=alert_counts.values, title="Alert Types Distribution")
    cols4[0].plotly_chart(fig)

    # Audit & History KPI
    changes_made = len(data["Audit History"])
    cols4[1].metric(label="Changes Logged", value=changes_made)

def main():
    st.title("🏕 Trailblaze MDM Control Center")
    
    data = load_data()

    # Initialize the session state variables if not already done
    if 'selected_feature' not in st.session_state:
        st.session_state.selected_feature = None

    # Check if a feature has been selected during this run
    current_selection = display_feature_buttons()
    if current_selection is not None:
        st.session_state.selected_feature = current_selection

    # Display the appropriate feature/page based on session state
    if st.session_state.selected_feature == "Data Profiling":
        data_profiling.display(st, data) 
    elif st.session_state.selected_feature == "Data Lineage":
        data_lineage.display_data_lineage()
    elif st.session_state.selected_feature == "Data Quality":
        data_quality.display_data_quality(data)
    elif st.session_state.selected_feature == "Hierarchy Management":
        hierarchy_management.display_hierarchy_management(data)
    elif st.session_state.selected_feature == "Data Versioning":
        data_versioning.data_versioning()
    elif st.session_state.selected_feature == "Golden Record":
        golden_record.golden_record()
    elif st.session_state.selected_feature == "Deduplication Tools":
        deduplication_tools.deduplication_tools()
    elif st.session_state.selected_feature == "Governance and Compliance":
        governance_compliance_reporting.governance_compliance_reporting()
    elif st.session_state.selected_feature == "Workflow Visualization":
        workflow_visualization.workflow_visualization()
    elif st.session_state.selected_feature == "Interactive Data Exploration":
        interactive_data_exploration.interactive_data_exploration()
    elif st.session_state.selected_feature == "Anomaly Detection":
        ai_anomaly_detection.display_data_quality(data)
    elif st.session_state.selected_feature == "AI Rules":
        ai_rules.display_rules_engine(data)
    elif st.session_state.selected_feature == "Metadata Management":
        metadata_management.display_metadata_management(data)
    elif st.session_state.selected_feature == "Reference Data Management":
        reference_data_management.display_reference_data_management()
        
    else:
        display_kpis()

if __name__ == '__main__':
    main()
