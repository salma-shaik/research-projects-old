import pandas as pd
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

df1 = pd.DataFrame({'A': [1,2,3], 'B':[6,5,7], 'C':[90.23, 56,234]})



df1.rename(columns={'A': 'placename'}, inplace=True)
# df1.rename(str.lower, axis='columns')
print(df1)