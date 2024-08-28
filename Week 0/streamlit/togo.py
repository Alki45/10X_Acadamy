import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the CSV file
data_togo = pd.read_csv('A:/10x/10X_Acadamy/data/togo-dapaong_qc.csv')

# Create a Streamlit dashboard
st.title("Togo-Dapaong QC Data Analysis")

# Display the DataFrame
st.subheader("Data Preview")
st.write(data_togo.head())

# Display summary statistics
st.subheader("Summary Statistics")
st.write(data_togo.describe())

# Add a sidebar for user interaction
st.sidebar.title("Dashboard Options")
analysis_type = st.sidebar.selectbox("Select analysis type", ["Numeric Column Distributions", "Categorical Column Frequencies", "Correlation Matrix"])

# Select columns for analysis
selected_cols = None
if analysis_type == "Numeric Column Distributions":
    numeric_cols = list(data_togo.select_dtypes(include=['float64', 'int64']).columns)
    selected_cols = st.sidebar.multiselect("Select numeric columns", numeric_cols, default=numeric_cols)
elif analysis_type == "Categorical Column Frequencies":
    categorical_cols = list(data_togo.select_dtypes(include=['object']).columns)
    selected_cols = st.sidebar.multiselect("Select categorical columns", categorical_cols, default=categorical_cols)
elif analysis_type == "Correlation Matrix":
    selected_cols = st.sidebar.multiselect("Select columns for correlation matrix", list(data_togo.columns), default=list(data_togo.columns))
