import pandas as pd

"""
# Uniform datatypes in the same name column
dict1 = {"Employee_ID": [1, 2, 3], "first_name": ['John', 'Mary', 'Sam'], "salary": [2000, 1500, 3000]}
dict2 = {"Employee_ID": [1, 2, 3], "last_name": ['Doe', 'Smith', 'Jacob'], "salary": [2500, 2000, 2500]} # "2", "3" would force the entire column to be parsed as string values

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

print('df1: \n', df1, '\n')
print('type')
print(df1.dtypes,'\n') # int64

print('df2: \n', df2, '\n')
print('type')
print(df2.dtypes) # object

df3 = pd.merge(df1, df2, on='Employee_ID')
print("df3 obtained by concatenating df1 and df2: \n", df3)


'''
    Employee_ID first_name  salary_x last_name  salary_y
0            1       John      2000       Doe      2500
1            2       Mary      1500     Smith      2000
2            3        Sam      3000     Jacob      2500

'''
"""


"""
# Different datatypes in the same name column
dict1 = {"Employee_ID": [1, 2, 3], "first_name": ['John', 'Mary', 'Sam'], "salary": [2000, 1500, 3000]}
dict2 = {"Employee_ID": [1, 2, 3], "last_name": ['Doe', 'Smith', 'Jacob'], "salary": [2500, "2000", 2500]} # "2000", forces the entire column to be parsed as string values

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

print('df1: \n', df1, '\n')
print('type')
print(df1.dtypes,'\n') # int64

print('df2: \n', df2, '\n')
print('type')
print(df2.dtypes) # object

df3 = pd.merge(df1, df2, on='Employee_ID')
print("df3 obtained by concatenating df1 and df2: \n", df3)
'''
    Employee_ID first_name  salary_x last_name salary_y
0            1       John      2000       Doe     2500
1            2       Mary      1500     Smith     2000
2            3        Sam      3000     Jacob     2500
'''
"""


"""
# If trying to merge on same name column with uniform datatypes
dict1 = {"Employee_ID": [1, 2, 3], "first_name": ['John', 'Mary', 'Sam'], "salary": [2000, 1500, 3000]}
dict2 = {"Employee_ID": [1, 2, 3], "last_name": ['Doe', 'Smith', 'Jacob'], "salary": [2500, 2000, 2500]} # "2", "3" would force the entire column to be parsed as string values

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

print('df1: \n', df1, '\n')
print('type')
print(df1.dtypes,'\n') # int64

print('df2: \n', df2, '\n')
print('type')
print(df2.dtypes) # object

df3 = pd.merge(df1, df2, on='salary')
print("df3 obtained by concatenating df1 and df2: \n", df3)

'''
    Employee_ID_x first_name  salary  Employee_ID_y last_name
0              1       John    2000              2     Smith

'''
"""


"""
# If trying to merge on same name column with different datatypes
dict1 = {"Employee_ID": [1, 2, 3], "first_name": ['John', 'Mary', 'Sam'], "salary": [2000, 1500, 3000]}
dict2 = {"Employee_ID": [1, 2, 3], "last_name": ['Doe', 'Smith', 'Jacob'], "salary": [2500, "2000", 2500]} # "2000", forces the entire column to be parsed as string values

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

print('df1: \n', df1, '\n')
print('type')
print(df1.dtypes,'\n') # int64

print('df2: \n', df2, '\n')
print('type')
print(df2.dtypes) # object

# df3 = pd.merge(df1, df2, on='salary') # ValueError: You are trying to merge on int64 and object columns. If you wish to proceed you should use pd.concat
# print("df3 obtained by concatenating df1 and df2: \n", df3)

df3 = pd.concat([df1, df2])
print("df3 obtained by concatenating df1 and df2: \n", df3)

'''
    Employee_ID first_name last_name salary
0            1       John       NaN   2000
1            2       Mary       NaN   1500
2            3        Sam       NaN   3000
0            1        NaN       Doe   2500
1            2        NaN     Smith   2000
2            3        NaN     Jacob   2500
'''

# # df3 = pd.merge(df1, df2) # ValueError: You are trying to merge on int64 and object columns. If you wish to proceed you should use pd.concat
# df3 = pd.concat([df1, df2])
#
# print("df3 obtained by concatenating df1 and df2: \n", df3)
"""


# Uniform datatypes in the same name column
# dict1 = {"Employee_ID": [1, 2, 3], "first_name": ['John', 'Mary', 'Sam'], "salary": [2000, 1500, 3000]}
# dict2 = {"Employee_ID": [1, 2, 3], "last_name": ['Doe', 'Smith', 'Jacob'], "salary": [2500, 2000, 2500]} # "2", "3" would force the entire column to be parsed as string values

dict1 = {"Employee_ID": [1, 2, 3], "first_name": ['John', 'Mary', 'Sam']}
dict2 = {"Employee_ID": [3, 4, 5], "last_name": ['Doe', 'Smith', 'Jacob']}

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

# df3 = pd.merge(df1, df2, on='Employee_ID')
# print("df3 obtained by concatenating df1 and df2: \n", df3)

df3 = df1.merge(df2)
print("df3 obtained by concatenating df1 and df2: \n", df3)

print()
print(df1.join(df2, lsuffix='_')) # by default left join on indices if no 'on' is specified
# if we want a specific index, then we can set it using set_index='col name' on a df
print()
print(df1.join(df2, on='Employee_ID', lsuffix='_')) # by default left join