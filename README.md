YouTube Data Analysis

This repository contains Python code for performing data analysis on YouTube statistics. The code uses Python libraries such as NumPy, pandas, seaborn, and matplotlib to load, clean, and visualize the data. It provides insights into various aspects of YouTube channels and their performance.

Table of Contents

Requirements

Usage

Data Loading

Data Cleaning

Data Visualization

License


Requirements

To run this code, you need the following Python libraries installed:

NumPy
pandas
seaborn
matplotlib
You can install these libraries using pip:

pip install numpy pandas seaborn matplotlib

Usage

Clone this repository to your local machine:

git clone https://github.com/yourusername/youtube-data-analysis.git

Navigate to the project directory:

cd youtube-data-analysis

Run the Python script using your preferred Python environment (e.g., Jupyter Notebook, VSCode, or any IDE).

Data Loading

The code begins by loading YouTube statistics data from the 'Global YouTube Statistics.csv' file using pandas. You can replace this file with your own dataset if needed. The data is loaded with ISO-8859-1 encoding.

Data Cleaning

Data cleaning is an essential step in any data analysis process. The code performs the following data cleaning tasks:

Checks for and prints the basic information about the dataset, including the number of rows and columns, data types, and missing values.
Drops rows with missing values (NaN) to ensure data completeness.
Removes unrequired columns from the dataset.
You can uncomment and modify the code in the "Data Cleaning" section to suit your specific data cleaning needs.

Data Visualization

Data visualization is a crucial part of data analysis for gaining insights. The code provides several visualization examples:

Top 10 YouTubers in terms of subscribers and views using bar plots.
Channel subscribers by category using a bar plot.
Distribution of channel types using a count plot.
Relationship between subscribers and video views using a line plot.
Yearly average subscribers using a line plot.

You can uncomment and customize these visualization sections according to your analysis requirements. The code uses seaborn and matplotlib for plotting, so feel free to adjust the visualizations to your liking.

License

This code is provided under the MIT License. You are free to use, modify, and distribute it as needed. See the LICENSE file for more details.

Happy analyzing YouTube data!
