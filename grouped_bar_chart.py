import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import pytz

# Load dataset (update with the correct file path)
df = pd.read_csv("app_data.csv")

# Convert 'Last Updated' to datetime format
df['Last Updated'] = pd.to_datetime(df['Last Updated'], errors='coerce')

# Apply filters
df_filtered = df[(df['Rating'] >= 4.0) & (df['Size'] >= 10) &
                 (df['Last Updated'].dt.month == 1)]

# Identify top 10 categories by number of installs
top_categories = df_filtered.groupby('Category')['Installs'].sum().nlargest(10).index

df_filtered = df_filtered[df_filtered['Category'].isin(top_categories)]

# Calculate average rating and total review count
category_summary = df_filtered.groupby('Category').agg({
    'Rating': 'mean',
    'Reviews': 'sum'
}).reset_index()

# Check current time in IST
ist = pytz.timezone('Asia/Kolkata')
current_time = datetime.now(ist).time()
allowed_start = datetime.strptime("15:00", "%H:%M").time()
allowed_end = datetime.strptime("17:00", "%H:%M").time()

if allowed_start <= current_time <= allowed_end:
    # Create grouped bar chart
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=category_summary['Category'], 
        y=category_summary['Rating'],
        name='Average Rating',
        marker_color='blue'
    ))
    
    fig.add_trace(go.Bar(
        x=category_summary['Category'], 
        y=category_summary['Reviews'],
        name='Total Reviews',
        marker_color='red'
    ))
    
    # Configure layout
    fig.update_layout(
        title='Average Rating and Total Reviews for Top 10 Categories',
        xaxis_title='Category',
        yaxis_title='Value',
        barmode='group',
        legend=dict(x=0.1, y=1.1)
    )
    
    # Show the figure
    fig.show()
    
    # Save plot as HTML
    fig.write_html("grouped_bar_chart.html")
else:
    print("Graph is only available between 3 PM IST and 5 PM IST.")
