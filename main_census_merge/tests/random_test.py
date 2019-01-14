import pandas as pd
import numpy as np

from utilities import clean_files as cf
import re
#
# census_type=''
# year=''
# def get_census_type(file_path): # pass the indexes of census type and year wor dlocations in the file name if reqd. Need to agree upon either having uniform file names or passing on the indexes
#     cen_type=''
#     # Get a list of all the navigation folders in the file path
#     fp_words = file_path.split('/')
#
#     # Get a list of words in the folder name
#     fdn_words = fp_words[-3].split('_')
#
#     if 'county' in fdn_words:
#         cen_type = 'county'
#     elif 'city' in fdn_words:
#         cen_type = 'city'
#
#     # Extract the year from the file name list of words
#     cen_year = fp_words[-1].split('_')[-5] # get year which is in the 5th position from the end
#
#     return(cen_type, cen_year)
#
#
# file_loc = 'C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_county_2010/modified_files/DEC_10_SF1_P12_with_ann.csv'
#
# (census_type, year) = get_census_type(file_loc)
#
# print(census_type)
# print(year)
#
#
# df1 = pd.DataFrame({'A': [1,2,3], 'B':[6,5,7], 'C':[90.23, 56,234]})
#
# def arrange_cols(df, df_cols, cols_dict=None):
#     for ind, col in cols_dict.items():
#         df_cols.insert(ind, df_cols.pop(df_cols.index(col)))
#         # df_cols.insert(0, df_cols.pop(df_cols.index('C')))
#     return df.reindex(columns=df_cols)
#
# df1_cols = df1.columns.tolist()  # to get a list of columns
#
# df1 = arrange_cols(df=df1, df_cols=df1_cols, cols_dict={0:'C'})
#
# df1['test'] = 0
#
# print(df1)

# def test_tup_list():
#     fp_list = []
#     fp_list.append((1, 2))
#     fp_list.append((4, 5))
#     fp_list.append((7, 9))
#     return fp_list
#
#
# fp_tup_list= test_tup_list()
#
# for fp in fp_tup_list:
#     inp, op = fp
#     print(inp, op)

# df1 = pd.DataFrame({'Total:':[23423, 14,12456, 6434, 242]})
#
# df1['POP100'] = df1['Total:']
# print(df1)
#
# df1 = pd.DataFrame({'A': [1,2,3], 'B':[6,5,7], 'C':[90.23, 56,234]})
#
#
#
# # df1.rename(columns={'A': 'placename'}, inplace=True)
# # df1.rename(str.lower, axis='columns')
# # print(df1)
# # print()
# # print(df1.dtypes)
#
# df2 = pd.read_csv('C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/census_county_2010/new fips_cols/DEC_10_SF1_P12_with_ann.csv')
# print(df2.head())
# print(df2.dtypes)
#

# counties_2000_df = pd.read_csv('C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/census_county_2000/new_census_variables/new_vars_census_county_2000.csv', dtype={"place_fips":str, "CNTY":str, "STATEFP":str})
# print(counties_2000_df.head())

# counties_2000_df = pd.read_csv('C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/census_county_2000/new_census_variables/new_vars_census_county_2000.csv', dtype={"place_fips":str, "CNTY":str, "STATEFP":str})
# counties_2010_df = pd.read_csv('C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/census_county_2010/new_census_variables/new_vars_census_county_2010.csv', dtype={"place_fips":str, "CNTY":str, "STATEFP":str})
# cities_2000_df = pd.read_csv('C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/census_cities_2000/new_census_variables/new_vars_census_cities_2000.csv', dtype={"place_fips":str, "CNTY":str, "STATEFP":str})
# cities_2010_df = pd.read_csv('C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/census_cities_2010/new_census_variables/new_vars_census_cities_2010.csv', dtype={"place_fips":str, "CNTY":str, "STATEFP":str})
#
#
# national_census_2000_2010_all_df = counties_2000_df.append([counties_2010_df, cities_2000_df, cities_2010_df])
#
# print(national_census_2000_2010_all_df.tail(20))

#cf.write_updated_df_file(national_census_2000_2010_all_df, 'C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/National_Census_00_10_All.csv')

# test_str = '53380(r38811)'


# def remove_revised_pop100(pop100_val, ptrn):
#     pattern = re.compile(ptrn)
#     match = pattern.search(pop100_val)
#     if match:
#         return pop100_val[:match.start()]
#     else:
#         return pop100_val
#
#
# test_df = pd.DataFrame({'A':[1,2,3], 'POP100':['53380(r38811)', '53380', '530(r311)']})
# test_df['POP100'] = test_df['POP100'].apply(remove_revised_pop100, args=('\(',))
# print(test_df['POP100'])


# df1 = pd.DataFrame({'A': [1,2,2,4,1], 'B':[6,5,5,8,6], 'C':[90.23,56,56,222,90], 'D':['a','b','c','d','e']})
# df2 = pd.DataFrame({'A': [1,2,3], 'B':[6,5,7], 'C':[90.23, 59,234]})
#
# df_all_lt = df1.merge(df2.drop_duplicates(), on=['A', 'B'], how='left', indicator=True)
# print(df_all_lt)
#
# # Replace NaN value from c_y with c_x value
# # final['c'] = final['c_y'].fillna(final['c_x'])
#
# print()
#
# df_all_lt['C'] = df_all_lt['C_y'].fillna(df_all_lt['C_x'])
# df_all_lt = df_all_lt.drop(['C_x', 'C_y', '_merge'], axis=1)
# print(df_all_lt)
# # df_all_rt = df1.merge(df2.drop_duplicates(), on=['A','B','C'], how='right', indicator=True)
# # print(df_all_rt)

# df1 = pd.DataFrame({'A': [1,2,2,4,1], 'B':[6,5,5,8,6], 'C':[90,56,22,43,55], 'D':['a','b','c','d','e']})
# df2 = pd.DataFrame({'A': [10,20,30,40], 'B':[6,15,5,8], 'C':[90,66,22,43]})
#
# merged_df = df1.merge(df2.drop_duplicates(), on=['B', 'C'], how='left', indicator=True)
# print(merged_df)

"""
   A_x  B   C   A_y
0    1  6  90  10.0
1    2  5  56   NaN
2    2  5  22  30.0
3    4  8  43  40.0
4    1  6  55   NaN

for the column that needs to be merged, 2 columns _x and _y are created. _y will have NaNs in non matching
rows' cells. Replace these NaNs with values from corresponding cells of _x and assign this to new column
which will have the final column name
Then drop _x and _y

   A_x  B   C  D   A_y     _merge
0    1  6  90  a  10.0       both
1    2  5  56  b   NaN  left_only
2    2  5  22  c  30.0       both
3    4  8  43  d  40.0       both
4    1  6  55  e   NaN  left_only
"""
# df3 = pd.concat([df1, df2])
# print(df3)

# df4 = df1[['A', 'B']].append(df2[['A']])
# print(df4)

"""
Inner merge
"""

# df1 = pd.DataFrame({'A': [1,2,3,4,5], 'B':[6,7,8,9,10], 'C':[90,91,92,93,94], 'D':['a','b','c','d','e']})
# df2 = pd.DataFrame({'A': [20,30,40,60], 'B':[7,8,9,12], 'C':[91,92,93,99],'E':['B','C','D','F']})
#
# merged_df = df1.merge(df2, on=['B', 'C'], how='right')
#
# print(merged_df)

"""
Subset df based on certain values of a particular column
"""

# df1 = pd.DataFrame({'A': [1,2,3,4,5], 'B':[6,7,8,9,10], 'C':[90,91,92,93,94]})
# df1 = df1.loc[df1['A'].isin([2,3,4])]
#
# print(df1)


"""
pandas 3 way merge
"""
df1 = pd.DataFrame(np.array([
    ['a', 5, 9],
    ['b', 4, 61],
    ['c', 24, 9]]),
    columns=['name', 'attr1', 'attr2'])
df2 = pd.DataFrame(np.array([
    ['a', 5, 19],
    ['b', 14, 16],
    ['c', 4, 9]]),
    columns=['name', 'attr1', 'attr2'])
df3 = pd.DataFrame(np.array([
    ['a', 15, 49],
    ['b', 4, 36],
    ['c', 14, 9]]),
    columns=['name', 'attr1', 'attr2'])

# df1 = df1.merge(df2,on='name').merge(df3,on='name')
#
# print(df1)
"""
  name attr1_x attr2_x attr1_y attr2_y attr1 attr2
0    a       5       9       5      19    15    49
1    b       4      61      14      16     4    36
2    c      24       9       4       9    14     9
"""
print()

# df2 = df2.merge(df3,on='name').merge(df1,on='name')
#
# print(df2)
"""
  name attr1_x attr2_x attr1_y attr2_y attr1 attr2
0    a       5      19      15      49     5     9
1    b      14      16       4      36     4    61
2    c       4       9      14       9    24     9
"""
#
# df3 = df3.merge(df1,on='name').merge(df2,on='name')
#
#
# print(df3)
# print()
#
# df3['attr1'] = df3['attr1_x']
# df3['attr2'] = df3['attr2_x']
#
# df3.drop(['attr1_x', 'attr1_y', 'attr2_x', 'attr2_y'], axis=1, inplace=True)
#
# print(df3)

"""
  name attr1_x attr2_x attr1_y attr2_y attr1 attr2
0    a      15      49       5       9     5    19
1    b       4      36       4      61    14    16
2    c      14       9      24       9     4     9
"""


"""
merge test - different order of values in similar columns
"""
# df1 = pd.DataFrame({'A': [1,2,3,4,5], 'B':[6,7,8,9,10], 'C':[90,91,92,93,94]})
# df2 = pd.DataFrame({'A': [3,2,1,4,5], 'B':[80,7,60,9,10], 'C':[90,91,92,93,94]})
#
# print(df1.merge(df2, on=['A']))

"""
Population variables interpolation test
"""
#
# nat_cen_all = pd.read_csv('/Users/sshaik2/projects/research/research-projects/main_census_merge/data/wip_merge_files/National_Census_All_Sorted.csv')
#
# pop_vars = nat_cen_all[['YEAR', 'POP100', 'White_count', 'Black_count', 'Hispanic_count', 'Age1524_WhiteM', 'White_Males_All',
#                                     'Age1524_WhiteF', 'White_Females_All', 'Age1524_BlackM', 'Black_Males_All', 'Age1524_BlackF', 'Black_Females_All',
#                                     'Hispanic_Males_All', 'Age1524_HispanicM', 'Age1524_HispanicF', 'Hispanic_Females_All', 'Pct_WYM', 'Pct_WYF']]
#
# df_cols = pop_vars.columns
#
# pop_vars_int_temp = pd.DataFrame()
#
# test_df = pop_vars.head(10107)
#
# test_df_1 = pd.DataFrame(columns = test_df.columns)
#
# for row in zip(test_df['YEAR'], test_df['POP100'], test_df['White_count'], test_df['Black_count'], test_df['Hispanic_count'], test_df['Age1524_WhiteM'], test_df['White_Males_All'], test_df['Age1524_WhiteF'],
#                test_df['White_Females_All'], test_df['Age1524_BlackM'], test_df['Black_Males_All'], test_df['Age1524_BlackF'], test_df['Black_Females_All'], test_df['Hispanic_Males_All'],
#                test_df['Age1524_HispanicM'], test_df['Age1524_HispanicF'], test_df['Hispanic_Females_All'], test_df['Pct_WYM'], test_df['Pct_WYF']):
#     lst = []
#     lst.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18]])
#     test_df_1 = test_df_1.append(pd.DataFrame(lst, columns=test_df.columns), sort=False)
#     if row[0] != 1990:
#         for i in range(9):
#             test_df_1 = test_df_1.append(pd.Series(), ignore_index=True)
#
# # print(test_df_1)
#
# test_df_1.interpolate(inplace=True) # --> Only last 2 columns were getting interpolated :X:X:X:X:X
# print(test_df_1)


# for row in test_df.itertuples():
#     test_df_1 = test_df_1.append(pd.Series(row[1:], index=test_df.columns), ignore_index=True)
#     # test_df_1 = test_df_1.append(pd.DataFrame(lst, columns=(['YEAR', 'POP100'])), sort=False)
#     if row.YEAR != 1990:
#         for i in range(3):
#             test_df_1 = test_df_1.append(pd.Series(), ignore_index=True)
#
# print(test_df_1)
#
# test_df_1_int = test_df_1.interpolate(method='linear', axis=0)
# print(test_df_1_int)
#
# df1 = pd.DataFrame({'A': [1,2,3,4,5], 'B':[6,7,8,9,10], 'C':[90,91,92,93,94]})
# df2 = pd.DataFrame({'A': [2,1,4], 'B':[80,7,60], 'C':[90,91,92]})
#
#
# set_df1 = set(df1['A'])
# set_df2 = set(df2['A'])
#
#
# common_a_list = list(set_df1.intersection(set_df1.intersection(set_df2)))
# # print("list common_a: ", list(common_a))
#
# common_a_df = pd.DataFrame(common_a_list, columns=['A'])
#
# df1_final = df1.merge(common_a_df, on='A')
# print(df1_final)

nat_cen_fixed_yr = pd.DataFrame()

nat_cen_fixed_yr['YEAR'] = [2010, 2000, 1990, 2010, 2000, 1990, 2010, 2000, 1990]

conditions = [
    nat_cen_fixed_yr['YEAR'] == 2010,
    nat_cen_fixed_yr['YEAR'] == 2000,
    nat_cen_fixed_yr['YEAR'] == 1990,
]

outputs = [
    10, 10, 1
]

year_codes = np.select(conditions, outputs)

nat_cen_fixed_yr['YEAR'] = pd.Series(year_codes)

print(nat_cen_fixed_yr)