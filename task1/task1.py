import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('transactions.csv')

# Return the column names as a list
def columnNames():
    return list(df.columns)
print(columnNames())

# Return the first k rows from the dataframe
def First_k_Rows(k):
    return df.head(k)
print(First_k_Rows(5))

# Return a random sample of k rows from the dataframe
def randomSample(k):
    return df.sample(n=k)
print(randomSample(5))

# Return a list of the unique transaction types
def unique_transaction_types():
    return df['type'].unique().tolist()

print(unique_transaction_types())

# Return a Pandas series of the top 10 transaction destinations with frequencies
def top_10_destinations():
    return df['nameDest'].value_counts().head(10)
print(top_10_destinations())

# Return all the rows from the dataframe for which fraud was detected
def get_fraud_detected_rows():
    return df[df['isFraud'] == 1]
print(get_fraud_detected_rows())

# Bonus: Return a dataframe that contains the number of distinct destinations that each source has interacted with, sorted in descending order
def distinct_destinations_per_source():
    result = df.groupby('nameOrig')['nameDest'].nunique().reset_index()
    result.columns = ['nameOrig', 'distinct_destinations']
    return result.sort_values(by='distinct_destinations', ascending=False)
print(distinct_destinations_per_source())

#  Transaction types bar chart
def plot_transaction_types():
    plt.figure(figsize=(10, 6))
    sns.countplot(x='type', data=df)
    plt.title('Distribution of Transaction Types')
    plt.xlabel('Transaction Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()
    return "This bar chart shows the distribution of different transaction types, highlighting which transaction types are most common in the dataset."
print(plot_transaction_types())

#  Transaction types split by fraud bar chart
def plot_transaction_types_by_fraud():
    plt.figure(figsize=(10, 6))
    sns.countplot(x='type', hue='isFraud', data=df)
    plt.title('Transaction Types Split by Fraud')
    plt.xlabel('Transaction Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.legend(title='Fraud Detected', loc='upper right')
    plt.show()   
    return "This chart splits transaction types by whether fraud was detected, helping identify if certain transaction types are more susceptible to fraud."
print(plot_transaction_types_by_fraud())

#  Origin account balance delta vs. Destination account balance delta scatter plot for Cash Out transactions
def plot_cash_out_balance_delta():
    cash_out_df = df[df['type'] == 'CASH-OUT']
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='oldbalanceOrg', y='oldbalanceDest', data=cash_out_df)
    plt.title('Origin vs. Destination Account Balance Delta for Cash Out Transactions')
    plt.xlabel('Origin Account Balance (Before)')
    plt.ylabel('Destination Account Balance (Before)')
    plt.show()
    
    return "This scatter plot shows the relationship between the origin and destination account balances before the Cash Out transactions. It can help detect anomalies or irregular patterns."
print(plot_cash_out_balance_delta())
