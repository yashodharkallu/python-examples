import pandas as pd

txn_df = pd.read_csv('/Users/sidhartharay/Documents/my-workspace/rdd-examples/data/cred_txn.csv', sep='~')
print('Credit Transaction Data,')
print(txn_df)

print('\nDimension: ', txn_df.shape)

print("\nSchema:")
print(txn_df.info(verbose=True))

print("\nColumns:")
print(txn_df.columns)

pd.set_option('display.max_columns', 4)
pd.set_option('display.max_rows', 20)

print('\nCredit Transaction Data,')
print(txn_df)

print('\nCredit Transaction Data - 1st 10 records,')
print(txn_df.head())
print('\nCredit Transaction Data - last 10 records,')
print(txn_df.tail())
