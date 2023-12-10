# Credit Card Fraud Detection
# Author: Rishi Thakkar (8877142)
#         Vijay Meena (8905210)
# Group: 13
# Description: This script performs data cleaning on the dataset.

import pandas as pd
from scipy import stats

# Load the dataset
data = pd.read_csv('creditcard_2023.csv')

# Data Validation - Checking for null values
null_counts = data.isnull().sum()
print("Null value counts:\n", null_counts)

# Remove null values if any
data.dropna(inplace=True)

# Outlier Detection - Using Z-score for 'Amount' column
z_scores = stats.zscore(data['Amount'])
threshold = 3
outliers = data[(z_scores > threshold) | (z_scores < -threshold)]
print("Outliers found:\n", outliers)

# Data Profiling - Basic summary statistics
summary_stats = data.describe()
print("Summary Statistics:\n", summary_stats)

# Data Standardization - Min-max scaling 'Amount' column
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
data['Amount_scaled'] = scaler.fit_transform(data[['Amount']])

# Store the cleaned data
cleaned_data_path = 'cleaned_creditcard_2023.csv'
data.to_csv(cleaned_data_path, index=False)

# Displaying the first few rows of the cleaned data as a summary
print("Cleaned Data Summary:\n", data.head())
