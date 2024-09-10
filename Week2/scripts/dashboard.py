import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Load data from MySQL
db_connection_str = 'mysql+pymysql://root:alki@localhost:3306/telecom' 
db_connection = create_engine(db_connection_str)
query = 'SELECT * FROM satisfaction_scores'
data = pd.read_sql(query, con=db_connection)

# Streamlit App
st.title('Customer Satisfaction Dashboard')

# KPIs
st.header('Key Performance Indicators')
st.write(f"Total Records: {data.shape[0]}")
st.write(f"Average Satisfaction Score: {data['Satisfaction Score'].mean():.2f}")

# Top 10 Satisfied Customers
st.header('Top 10 Satisfied Customers')
top_10 = data.nlargest(10, 'Satisfaction Score')
st.write(top_10[['MSISDN/Number', 'Satisfaction Score']])

# Visualizations
st.header('Visualizations')

# Plot Engagement and Experience Scores
fig, ax = plt.subplots()
sns.scatterplot(data=data, x='Engagement Score', y='Experience Score', hue='Cluster', ax=ax)
ax.set_title('Engagement vs Experience Scores')
st.pyplot(fig)


