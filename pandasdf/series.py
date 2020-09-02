"""
Pandas DataFrame and Series objects.
"""

import pandas as pd

people = {
    'firstname': ['Rajesh', 'Lathesh', 'Sunit'],
    'lastname': ['Singh', 'Pandey', 'Reddy'],
    'email': ['rajesh.singh@dsm.com', 'lathesh.pandey@dsm.com', 'sunit.reddy@dsm.com']
}
print('people dict : key - email')
print(people['email'])

df = pd.DataFrame(people)
print('\npeople dataframe : column - email')
print(df['email'])  # Also, print(df.email)
print(type(df['email']))

print('\npeople dataframe : columns - lastname and email')
print(df[['lastname', 'email']])  # Also, print(df.email)
print(type(df[['lastname', 'email']]))

print('\n1st row,')
print(df.iloc[0])
print('--------------------------------')
print(df.loc[0])

print('\n1st and 2nd row,')
print(df.iloc[[0, 1]])

print('\n1st and 2nd row | 3rd column')
print(df.iloc[[0, 1], 2])
print('--------------------------------')
print(df.loc[[0, 1], 'email'])
print('--------------------------------')
print(df.loc[0:1, 'email'])
print('--------------------------------')
print(df.loc[[0, 1], ['lastname', 'email']])
print('--------------------------------')
print(df.loc[0:1, 'lastname':'email'])

print('\nCredit Transaction Data - email id counts,')
print(df['email'].value_counts())



