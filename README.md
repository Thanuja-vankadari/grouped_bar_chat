This repository contains a Python script that generates a grouped bar chart comparing the average rating and total review count for the top 10 app categories by number of installs. The chart is restricted to display only between 3 PM IST and 5 PM IST.

Files Included

grouped_bar_chart.py - The Python script to generate the grouped bar chart.

grouped_bar_chart.html - The output HTML file with the interactive chart.

app_data.csv - Sample dataset (not included, provide your own dataset with the required columns).

Installation and Usage

Prerequisites

Ensure you have Python installed along with the following libraries:

pip install pandas plotly pytz

Running the Script

Place your dataset (app_data.csv) in the same directory as grouped_bar_chart.py.

Run the script using:

python grouped_bar_chart.py

If the current time is between 3 PM IST and 5 PM IST, the chart will be displayed and saved as grouped_bar_chart.html.

If the script is run outside this time window, it will display a message indicating the chart is not available.

Dataset Requirements

The dataset should be a CSV file with the following columns:

Category (string) - App category.

Installs (numeric) - Number of installs.

Rating (numeric) - Average user rating.

Reviews (numeric) - Number of user reviews.

Size (numeric) - App size in MB (should be 10MB or more).

Last Updated (date) - Last update date (should be in January).
