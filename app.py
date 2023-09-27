
import streamlit as st
import pandas as pd
import plotly.express as px
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
# Load the generated datasets
st.markdown(
    """
<style>
    .appview-container .main .block-container{
        max-width: 1200px;
        padding: 0rem;
        padding-top: 3rem;
        
    }
    .appview-container .main {
        color: #111111;  # This sets the text color
        background-color: #FFFFFF;  # This sets the background color to white
    }
    .stApp{
    background-color: #fcfcfc;  # This sets the background color to white
    }
    .stHeader{
    background-color: #F2f2f2;  # This sets the background color to white
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
    "AI Rules"
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
    "AI Rules": "🔨"

}

# Grouped features for better organization
FEATURE_GROUPS = {
    "🗃️ Data Management": ["KPI Overview", "Data Profiling", "Data Lineage", "Data Quality"],
    "🛠️ Tools & Control": ["Hierarchy Management", "Data Versioning", "Deduplication Tools", "Golden Record","Interactive Data Exploration"],
    "📈 Reporting": ["Governance and Compliance","Workflow Visualization"],
    "🤖 AI": ["Anomaly Detection","AI Rules"],

    # Add more groups as needed...
}


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
    st.header("Key Performance Indicators")

    # Data Overview KPI
    st.subheader("Data Volume Overview")
    cols1 = st.columns(2)
    latest_data = data["Data Overview"].tail(10)
    fig = px.line(latest_data, x="Date", y=companies, title="Recent Data Volume Trend")
    cols1[0].plotly_chart(fig)

    # Data Completeness KPI
    missing_data = data["Data Completeness"].isna().sum()
    fig = px.bar(missing_data, title="Missing Data Points by Company")
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
    else:
        display_kpis()

if __name__ == '__main__':
    main()
