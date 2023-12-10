# Credit Card Fraud Detection
# Author: Rishi Thakkar (8877142)
#         Vijay Meena (8905210)
# Group: 13
# Description: This script performs data visualization on the cleaned dataset.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset (You must run data_cleaning_script.py first)
data = pd.read_csv('cleaned_creditcard_2023.csv')

# Visualization 1: Histogram of Transaction Amounts
plt.figure(figsize=(8, 6))
sns.histplot(data['Amount'], bins=30, kde=True)
plt.title('Histogram of Transaction Amounts')
plt.xlabel('Transaction Amount')
plt.ylabel('Frequency')
plt.show()

# Visualization 2: Count Plot of Fraudulent vs. Non-Fraudulent Transactions
plt.figure(figsize=(6, 4))
sns.countplot(x='Class', data=data)
plt.title('Count of Fraudulent vs. Non-Fraudulent Transactions')
plt.xlabel('Transaction Class')
plt.ylabel('Count')
plt.xticks([0, 1], ['Non-Fraudulent', 'Fraudulent'])
plt.show()

# Visualization 3: Boxplot of Transaction Amount for Fraudulent vs. Non-Fraudulent Transactions
plt.figure(figsize=(8, 6))
sns.boxplot(x='Class', y='Amount', data=data)
plt.title('Boxplot of Transaction Amount for Fraudulent vs. Non-Fraudulent Transactions')
plt.xlabel('Transaction Class')
plt.ylabel('Transaction Amount')
plt.xticks([0, 1], ['Non-Fraudulent', 'Fraudulent'])
plt.show()

# Visualization 4: Exploring Distribution Patterns and Relationships among Anonymized Transaction Attributes in Credit Card Data
# Select columns for analysis (V1, V5, V10, V15)
selected_columns = ['V1', 'V5', 'V10', 'V15']

# Subset the data with selected columns
selected_data = data[selected_columns]

# Summary statistics
summary_stats = selected_data.describe()

# Correlation matrix
correlation_matrix = selected_data.corr()

# Visualize distributions
plt.figure(figsize=(10, 6))
for i, column in enumerate(selected_columns, 1):
    plt.subplot(2, 2, i)
    sns.histplot(data[column], kde=True)
    plt.title(f'Distribution of {column}')
plt.tight_layout()
plt.show()

# Visualize correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix of Select Columns')
plt.show()

# Display summary statistics
print("Summary Statistics of Select Columns:")
print(summary_stats)

# Exploratory Analysis: Difference in Transaction Amounts between Fraudulent and Non-Fraudulent Transactions
fraudulent = data[data['Class'] == 1]['Amount']
non_fraudulent = data[data['Class'] == 0]['Amount']

mean_fraudulent = fraudulent.mean()
mean_non_fraudulent = non_fraudulent.mean()

print("Mean transaction amount for fraudulent transactions:", mean_fraudulent)
print("Mean transaction amount for non-fraudulent transactions:", mean_non_fraudulent)
