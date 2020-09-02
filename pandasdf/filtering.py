import pandas as pd

people = {
    'firstname': ['Rajesh', 'Lathesh', 'Sunit'],
    'lastname': ['Singh', 'Reddy', 'Reddy'],
    'email': ['rajesh.singh@dsm.com', 'lathesh.pandey@dsm.com', 'sunit.reddy@dsm.com']
}

df = pd.DataFrame(people)

print(df['lastname'] == 'Reddy')
print('\nFilter where lastname is equal to \'Reddy\'')
print(df[df['lastname'] == 'Reddy'])
print()
print('\nFilter where firstname is \'Lathesh\' and lastname is equal to \'Reddy\'')
print(df[(df['firstname'] == 'Lathesh') & (df['lastname'] == 'Reddy')])
print()
print(df.loc[df['lastname'] == 'Reddy'])
print()
print(df.loc[(df['lastname'] == 'Reddy', 'email')])
