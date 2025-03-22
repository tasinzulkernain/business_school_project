import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html

# Load the CSV file
df = pd.read_csv('../../anxiety_depression_data.csv')  # Ensure the file name matches

# Exclude non-numeric columns for correlation heatmap
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Anxiety and Depression Data Report", style={'textAlign': 'center'}),
    
    # Age Distribution
    html.H2("Age Distribution"),
    dcc.Graph(
        id='age-distribution',
        figure=px.histogram(df, x='Age', nbins=20, title='Age Distribution')
    ),
    
    # Gender Distribution
    html.H2("Gender Distribution"),
    dcc.Graph(
        id='gender-distribution',
        figure=px.pie(df, names='Gender', title='Gender Distribution')
    ),
    
    # Anxiety Score Distribution
    html.H2("Anxiety Score Distribution"),
    dcc.Graph(
        id='anxiety-distribution',
        figure=px.histogram(df, x='Anxiety_Score', nbins=20, title='Anxiety Score Distribution')
    ),
    
    # Depression Score Distribution
    html.H2("Depression Score Distribution"),
    dcc.Graph(
        id='depression-distribution',
        figure=px.histogram(df, x='Depression_Score', nbins=20, title='Depression Score Distribution')
    ),
    
    # Stress Level Distribution
    html.H2("Stress Level Distribution"),
    dcc.Graph(
        id='stress-distribution',
        figure=px.histogram(df, x='Stress_Level', nbins=20, title='Stress Level Distribution')
    ),
    
    # Correlation Heatmap (using only numeric columns)
    html.H2("Correlation Heatmap"),
    dcc.Graph(
        id='correlation-heatmap',
        figure=px.imshow(numeric_df.corr(), text_auto=True, title='Correlation Heatmap')
    )
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8051)  # Use a different port to avoid conflicts
