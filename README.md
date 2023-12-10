# Credit Card Fraud Detection Data Cleaning Script

This script performs data cleaning tasks such as removing null values, outlier detection, basic data profiling, and data standardization for a credit card fraud detection dataset.

## Prerequisites
- Python installed on your system (Python 3.x recommended)
- Download the 'creditcard_2023.csv' dataset from [Kaggle](https://www.kaggle.com/datasets/nelgiriyewithana/credit-card-fraud-detection-dataset-2023) and place it in the same directory as the Python script.

## Installation
1. Clone or download this repository.
2. Install the required libraries by running: `pip install -r requirements.txt`

## How to Run Data Cleaning Script
1. Place your 'creditcard_2023.csv' dataset in the same directory as the Python script.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script by entering: `python data_cleaning_script.py`

## Output of Data Cleaning Script
The script will perform the following tasks:
- Remove null values from the dataset.
- Detect outliers using Z-score on the 'Amount' column.
- Generate summary statistics for the cleaned data.
- Standardize the 'Amount' column using Min-max scaling.
- Store the cleaned dataset in a file named 'cleaned_creditcard_2023.csv'.

The script will display information about the outliers found and summary statistics on the console. The cleaned data will be saved in the 'cleaned_creditcard_2023.csv' file in the same directory.

# Credit Card Fraud Detection Data Analysis and Visualization

This script performs exploratory data analysis (EDA) and visualization on a cleaned credit card fraud detection dataset.

## How to Run Data Analysis and Visualization Script
1. Ensure that your cleaned dataset ('cleaned_creditcard_2023.csv') is in the same directory as the Python script.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script by entering: `python data_visualization_script.py`

## Output of Data Analysis and Visualization Script
The script will perform the following tasks:
- Generate four visualizations:
  1. Histogram of Transaction Amounts
  2. Count Plot of Fraudulent vs. Non-Fraudulent Transactions
  3. Boxplot of Time vs. Transaction Class
  4. Correlation Heatmap of Features
- Conduct an analysis comparing mean transaction amounts between fraudulent and non-fraudulent transactions.

The visualizations will be displayed, and the analysis results will be printed in the console.
