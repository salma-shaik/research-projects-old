import pandas as pd


dict1 = {'A':['a', 'b'], 'B':[1, 2]}
df_left = pd.DataFrame(dict1, list('XY'))
print(df_left)
print()
df_right = pd.DataFrame([['a', 3], ['b', 4]], list('PQ'), list('AC'))
print(df_right)
print()

# if the indexes didn't align
# print(df_left.join(df_right.reset_index(), lsuffix='_', how='outer'))
# still creates a col for right df's index
'''
    A_    B index    A    C
X    a  1.0   NaN  NaN  NaN
Y    b  2.0   NaN  NaN  NaN
0  NaN  NaN     P    a  3.0
1  NaN  NaN     Q    b  4.0
'''

print(df_left.reset_index().join(df_right, lsuffix='_', how='outer'))
# still creates a col for left df's index
'''
  index   A_    B    A    C
0     X    a  1.0  NaN  NaN
1     Y    b  2.0  NaN  NaN
P   NaN  NaN  NaN    a  3.0
Q   NaN  NaN  NaN    b  4.0
'''

"""
# join - wanting to combine two dataframes based on their respective indexes
# need to specify suffix to the overlapping column name from left df
print(df_left.join(df_right, lsuffix='_'))

print()
# if the indexes didn't align
print(df_left.join(df_right.reset_index(), lsuffix='_', how='outer'))

print()
# We can tell join to use a specific column in the left dataframe to use as the join key, but it will still use the index from the right.
print(df_left.reset_index().join(df_right, on='index', lsuffix='_'))

print()
# By default merge will look for overlapping columns in which to merge on. If there are more than one column, then need to specify 'on'
print(df_left.merge(df_right))
print()
print(pd.merge(df_left, df_right))

For both the above. Note the index is [0, 1] and no longer ['X', 'Y']
  A  B  C
0  a  1  3
1  b  2  4


print()
# You can explicitly specify that you are merging on the index with the left_index or right_index paramter
print(df_left.merge(df_right, left_index=True, right_index=True, suffixes=['_', '']))
# both indexes should be same. If not, error



dict1 = {'ID': [1, 2, 3], 'first': ['Amy', 'John', 'Katie']}
dict2 = {'ID': [1, 2, 3], 'last': ['Adams', 'Bolt', 'Holmes']}

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

print(df1)
print()
print(df2)

# joined_df = df1.set_index('ID').join(df2.set_index('ID'), lsuffix='_', on='ID')

joined_df = df1.reset_index().join(df2, lsuffix='_')

print()
print(joined_df)

"""