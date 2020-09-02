import pandas as pd

txn_df = pd.read_csv('/Users/sidhartharay/Documents/my-workspace/rdd-examples/data/cred_txn.csv', sep='~')
print('Median of txn amount = ', txn_df['Amount'].median())
print('Median txn data columns = ', txn_df.median())

print('\nTxn data summary,')
print(txn_df.describe())

print('\nAccNum frequency')
print(txn_df['AccNum'].value_counts())

print('\nAccNum wise mean and median Amount,')
print(txn_df.groupby('AccNum')['Amount'].agg(['median', 'mean']))
print('\nAccNum \'333-XYZ-999\' -  mean and median Amount,')
print(txn_df.groupby('AccNum')['Amount'].agg(['median', 'mean']).loc['333-XYZ-999'])

