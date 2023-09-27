import random
import streamlit as st

def ai_generate_rules(df):
    """Generates a list of AI-powered rules based on the dataframe."""
    
    rules = []
    
    # Check for missing values in columns
    missing_data = df.isna().sum()
    for col, missing in missing_data.items():
        if missing > 0:
            rules.append({
                'Rule Name': f'Missing Value Rule for {col}',
                'Description': f'{missing} missing values detected in {col}',
                'Affected Columns': col,
                'Suggested Action': 'Impute or Remove'
            })
    
    # Generate some random rules for demo purposes
    for col in df.columns:
        if df[col].dtype == 'float64' or df[col].dtype == 'int64':
            rules.append({
                'Rule Name': f'Outlier Rule for {col}',
                'Description': f'Detect and handle outliers in {col}',
                'Affected Columns': col,
                'Suggested Action': 'Notify'
            })
    
    return rules

def display_rules_engine(data):
    st.subheader("AI-Powered Rules Engine for MDM")
    
    # Dataset selection
    selected_dataset = st.selectbox("Select Dataset for Rule Generation:", list(data.keys()))
    df = data[selected_dataset]
    st.write("Data Preview:")
    st.write(df.head())

    # Initialize session state for enforced and deployed rules if they don't exist
    if 'enforced_rules' not in st.session_state:
        st.session_state['enforced_rules'] = []
    if 'deployed_rules' not in st.session_state:
        st.session_state['deployed_rules'] = []

    if st.button("Generate AI-Powered Rules"):
        st.session_state.generated_rules = ai_generate_rules(df)  # Store generated rules in session state
        st.session_state['enforced_rules'] = []  # Reset when new rules are generated
        st.session_state['deployed_rules'] = []

    if 'generated_rules' in st.session_state:
        for rule in st.session_state.generated_rules:
            st.markdown(f"**Rule Name:** {rule['Rule Name']}")
            st.markdown(f"- **Description:** {rule['Description']}")
            st.markdown(f"- **Affected Columns:** {rule['Affected Columns']}")
            st.markdown(f"- **Suggested Action:** {rule['Suggested Action']}")

            rule_id = rule['Rule Name']
            
            if rule_id not in st.session_state['enforced_rules']:
                enforce_button = st.button(f"Enforce {rule_id}")
                if enforce_button:
                    st.session_state['enforced_rules'].append(rule_id)
            else:
                st.markdown("✅ Enforced")

            if rule_id not in st.session_state['deployed_rules']:
                deploy_button = st.button(f"Deploy {rule_id}")
                if deploy_button:
                    st.session_state['deployed_rules'].append(rule_id)
            else:
                st.markdown("✅ Deployed")

            st.write("---")
