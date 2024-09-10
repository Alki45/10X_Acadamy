import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load the data with error handling
def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

engagement_scores = load_data('A:/10x/10X_Acadamy/Data/Data_saved/engagement_scores.csv') 
experience_scores = load_data('A:/10x/10X_Acadamy/Data/Data_saved/experience_scores.csv')  

# Initialize the Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='User Engagement Analysis', children=[
            html.Div([
                dcc.Graph(
                    figure=px.bar(
                        engagement_scores, 
                        x='MSISDN/Number', 
                        y='Session Frequency', 
                        title='Top 10 Customers by Session Frequency'
                    )
                ),
                dcc.Graph(
                    figure=px.bar(
                        engagement_scores, 
                        x='MSISDN/Number', 
                        y='Total Traffic', 
                        title='Top 10 Customers by Total Traffic'
                    )
                )
            ])
        ]),
        dcc.Tab(label='Experience Analysis', children=[
            html.Div([
                dcc.Graph(
                    figure=px.scatter(
                        experience_scores, 
                        x='Avg Bearer TP DL (kbps)', 
                        y='Avg RTT DL (ms)', 
                        color='Cluster', 
                        title='Throughput vs RTT by Cluster'
                    )
                ),
                dcc.Graph(
                    figure=px.bar(
                        experience_scores, 
                        x='MSISDN/Number', 
                        y='TCP DL Retrans. Vol (Bytes)', 
                        title='Top and Bottom 10 TCP Retransmission Values'
                    )
                )
            ])
        ]),
    ])
])
if __name__ == '__main__':
    app.run_server(debug=True)
