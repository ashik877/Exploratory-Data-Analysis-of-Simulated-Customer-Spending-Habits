# Exploratory Data Analysis of Simulated Customer Spending Habits
## Advanced Version with Detailed Explanations

## Step 1: Import Required Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

## Step 2: Generate Synthetic Dataset

#We generate 500 customer records including:
num_records = 500

# Generate Age
ages = np.random.randint(18, 71, num_records)

# Generate Annual Income
annual_income = np.random.normal(75000, 20000, num_records)
annual_income = np.clip(annual_income, 30000, 150000)

# Generate Transaction Amount influenced by income
transaction_amount = np.random.normal(200, 80, num_records) + (annual_income / 1000) * 0.4
transaction_amount = np.clip(transaction_amount, 10, 500)

# Customer Segments
segments = np.random.choice(['A', 'B', 'C'], size=num_records, p=[0.4, 0.35, 0.25])

# Create DataFrame
data = pd.DataFrame({
    'Age': ages,
    'Annual_Income': annual_income,
    'Transaction_Amount': transaction_amount,
    'Customer_Segment': segments
})

data.head()

## Step 3: Data Inspection

data.info()

data.isnull().sum()

## Step 4: Descriptive Statistics

data[['Age', 'Annual_Income', 'Transaction_Amount']].describe()

## Step 5: Central Tendency (Mean & Median)

print('Mean Age:', data['Age'].mean())
print('Median Age:', data['Age'].median())

print('Mean Transaction:', data['Transaction_Amount'].mean())
print('Median Transaction:', data['Transaction_Amount'].median())

## Step 6: Correlation Analysis

correlation = data['Annual_Income'].corr(data['Transaction_Amount'])
print('Correlation between Annual Income and Transaction Amount:', correlation)

## Step 7: Distribution of Transaction Amount

plt.figure()
plt.hist(data['Transaction_Amount'], bins=30)
plt.title('Distribution of Transaction Amount')
plt.xlabel('Transaction Amount')
plt.ylabel('Frequency')
plt.show()

## Step 8: Income vs Transaction Amount

plt.figure()
plt.scatter(data['Annual_Income'], data['Transaction_Amount'])
plt.title('Annual Income vs Transaction Amount')
plt.xlabel('Annual Income')
plt.ylabel('Transaction Amount')
plt.show()

## Final Insights

#- Most transaction amounts cluster within a moderate range, indicating consistent purchasing behavior.
#- The positive correlation suggests that higher-income customers tend to spend slightly more per transaction.
#- Age distribution appears balanced across working-age individuals.
#- No missing values were found, meaning the dataset is clean and ready for analysis.