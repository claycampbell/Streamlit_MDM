import streamlit as st
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.impute import SimpleImputer
import numpy as np
def detect_anomalies(df):
    model = IsolationForest(contamination=0.05)
    df['anomaly'] = model.fit_predict(df.select_dtypes(include=['float64', 'int64']))
    return df[df['anomaly'] == -1]
    
def detect_duplicates(df):
    return df[df.duplicated(keep=False)]
def impute_data(df):
    # Separate the dataframe into numeric and non-numeric
    df_numeric = df.select_dtypes(include=['float64', 'int64'])
    df_non_numeric = df.select_dtypes(exclude=['float64', 'int64'])

    # Impute numeric data with mean
    imputer_numeric = SimpleImputer(strategy="mean")
    data_numeric_imputed = imputer_numeric.fit_transform(df_numeric)
    df_numeric = pd.DataFrame(data_numeric_imputed, columns=df_numeric.columns)

    # Impute non-numeric data with most frequent value
    imputer_non_numeric = SimpleImputer(strategy="most_frequent")
    data_non_numeric_imputed = imputer_non_numeric.fit_transform(df_non_numeric)
    df_non_numeric = pd.DataFrame(data_non_numeric_imputed, columns=df_non_numeric.columns)

    # Concatenate the dataframes to get the final imputed dataframe
    df_imputed = pd.concat([df_numeric, df_non_numeric], axis=1)

    return df_imputed
def display_data_quality(data):
    st.subheader("Data Quality Assessment")

    # Allow users to select a dataset from the loaded datasets
    selected_dataset = st.selectbox("Select Dataset for Quality Check:", list(data.keys()))

    df = data[selected_dataset].copy()  # Using copy to avoid in-place modifications
    
    # Impute missing values
    df = impute_data(df)

    st.write("Data Preview:")
    st.write(df.head())

    if st.button("Detect Anomalies"):
        anomalies = detect_anomalies(df)
        st.write("Detected Anomalies:")
        styled_anomalies = anomalies.style.apply(random_highlight_anomalies, axis=None)
        st.dataframe(styled_anomalies)


    if st.button("Detect Duplicates"):
        duplicates = detect_duplicates(df)
        st.write("Detected Duplicates:")
        st.write(duplicates)
def random_highlight_anomalies(data, prob=0.1):
    '''
    Randomly highlight cells with a certain probability.
    '''
    # Create a mask of the same shape as the data
    mask = np.random.rand(*data.shape) < prob

    # Create a styled dataframe based on the mask
    styled_data = pd.DataFrame('', index=data.index, columns=data.columns)
    for col in data.columns:
        styled_data[col] = np.where(mask[:, data.columns.get_loc(col)], 'background-color: red', '')
        
    return styled_data
