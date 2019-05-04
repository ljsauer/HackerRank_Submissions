# Tutorial from u/guipsamora on GitHub


import pandas as pd

users = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user',
                           sep='|', index_col='user_id')

(users.head(25))
(users.tail(10))

total_rows = users.shape[0]
total_columns = users.shape[1]
print(total_rows, total_columns)

col = users.columns
print(col)
    
labels = users.index
print(labels)

data_type = users.dtypes
print(data_type)

#print(users['occupation'])

occupations = users.occupation.nunique()
print(occupations)

occ_freq = users.occupation.value_counts().head()
print(occ_freq)

summary_data = (users.describe())
print(summary_data)

summary_columns = users.describe(include = 'all')
print(summary_columns)

summary_occ_col = users.occupation.describe()
print(summary_occ_col)

avg_age = round(users.age.mean())
print(avg_age)

avg_age_rare = users.age.value_counts().tail()
print(avg_age_rare)


# End tutorial


