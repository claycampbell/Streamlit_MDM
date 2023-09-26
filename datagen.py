import pandas as pd
import numpy as np

# Generate synthetic data for each category

# 1. Data Overview: Latest Data Snapshot & Data Volume Over Time
dates = pd.date_range(start="2022-01-01", periods=10, freq="D")
companies = ["TechCorp", "HealthInc", "EduTech", "FinServe", "GreenEnergy"]
data_overview = {"Date": dates}
for company in companies:
    data_overview[company] = np.random.randint(50, 150, size=(10,))

data_overview_df = pd.DataFrame(data_overview)
data_overview_df.to_csv("data_overview.csv", index=False)

# 2. Data Quality Metrics: Data Completeness
# For simplicity, we'll introduce some missing data for one company
data_completeness = data_overview.copy()
data_completeness["TechCorp"] = data_completeness["TechCorp"].astype(float)
data_completeness["TechCorp"][3] = np.nan
data_completeness_df = pd.DataFrame(data_completeness)
data_completeness_df.to_csv("data_completeness.csv", index=False)

# ... Continue this pattern for other categories ...

print("Data Overview and Data Completeness CSVs generated successfully!")
# 3. Data Accuracy: Historical corrections made to the data
data_accuracy = {
    "Date": dates,
    "Company": ["TechCorp"] * 10,
    "Original_Price": np.random.randint(45, 155, size=(10,)),
    "Corrected_Price": np.random.randint(45, 155, size=(10,))
}
data_accuracy_df = pd.DataFrame(data_accuracy)
data_accuracy_df.to_csv("data_accuracy.csv", index=False)

# 4. Rule Management: Active rules and their trigger counts
rules = ["Rule1", "Rule2", "Rule3", "Rule4", "Rule5"]
rule_management = {
    "Rule": rules,
    "Description": ["Description for " + rule for rule in rules],
    "Trigger_Count": np.random.randint(1, 100, size=(5,))
}
rule_management_df = pd.DataFrame(rule_management)
rule_management_df.to_csv("rule_management.csv", index=False)

# 5. AI Insights: Predicted stock prices based on historical data (mock predictions)
ai_insights = {
    "Date": dates,
    "TechCorp_Predicted": np.random.randint(50, 150, size=(10,)),
    "HealthInc_Predicted": np.random.randint(50, 150, size=(10,))
}
ai_insights_df = pd.DataFrame(ai_insights)
ai_insights_df.to_csv("ai_insights.csv", index=False)

# 6. User Feedback and Corrections: A log of user feedback and corrections
user_feedback = {
    "Date": dates,
    "User": ["User" + str(i) for i in np.random.randint(1, 5, size=(10,))],
    "Feedback": ["Feedback " + str(i) for i in np.random.randint(1, 100, size=(10,))],
    "Correction_Made": np.random.choice([True, False], size=(10,))
}
user_feedback_df = pd.DataFrame(user_feedback)
user_feedback_df.to_csv("user_feedback.csv", index=False)

# 7. Notifications & Alerts: Mock alerts and notifications
notifications = {
    "Date": dates,
    "Alert_Type": np.random.choice(["Critical", "Warning", "Info"], size=(10,)),
    "Message": ["Alert " + str(i) for i in np.random.randint(1, 100, size=(10,))]
}
notifications_df = pd.DataFrame(notifications)
notifications_df.to_csv("notifications.csv", index=False)

# 8. Audit & History: A change log for data modifications
audit_history = {
    "Date": dates,
    "Modified_Field": ["Field" + str(i) for i in np.random.randint(1, 5, size=(10,))],
    "Original_Value": np.random.randint(45, 155, size=(10,)),
    "New_Value": np.random.randint(45, 155, size=(10,))
}
audit_history_df = pd.DataFrame(audit_history)
audit_history_df.to_csv("audit_history.csv", index=False)

print("All CSV files generated successfully!")
if __name__ == "__main__":
    print("Generating synthetic datasets...")
    # ... [Place all the dataset generation code here] ...
    print("All CSV files generated successfully!")