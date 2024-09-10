import mysql.connector
from sqlalchemy import create_engine
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

engagement_scores = pd.read_csv('A:/10x/10X_Acadamy/Data/Data_saved/engagement_scores.csv') 
experience_scores = pd.read_csv('A:/10x/10X_Acadamy/Data/Data_saved/experience_scores.csv')  

# Merge engagement and experience scores
final_scores = engagement_scores.merge(experience_scores, on='MSISDN/Number', suffixes=('_eng', '_exp'))
final_scores['Engagement Score'] = engagement_scores['Satisfaction Score']
final_scores['Experience Score'] = experience_scores['Avg RTT DL (ms)'] 

# Normalize scores for clustering
scores_scaled = StandardScaler().fit_transform(final_scores[['Engagement Score', 'Experience Score']])

# Apply k-means clustering (k=2)
kmeans_final = KMeans(n_clusters=2, random_state=42)
final_scores['Cluster'] = kmeans_final.fit_predict(scores_scaled)

# Export to MySQL
db_connection_str = 'mysql+pymysql://root:alki@localhost:3306/telecom'  
db_connection = create_engine(db_connection_str)

# Export the DataFrame to MySQL
final_scores.to_sql('satisfaction_scores', con=db_connection, if_exists='replace', index=False)

print("Data exported to MySQL successfully.")