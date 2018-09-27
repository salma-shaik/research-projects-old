import pandas as pd

'''
To disable the warning - SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame
The point of the SettingWithCopyWarning is to show users (and esp new users) that they may be operating on a copy and not the original as they think. 
These are False positives (you know what you are doing, so it ok). One possibility is simply to turn off the (by default warn)
'''
pd.options.mode.chained_assignment = None  # default='warn'

main_file_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/Final_Main_Var_1990_2001.csv')
main_file_df_subset = main_file_df.iloc[:24]

county_census_2010_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/census_county_2010/DEC_10_SF1_P12_with_ann_county.csv')
county_census_2010_df_subset = county_census_2010_df.iloc[[69, 74, 81]]
county_census_2010_df_subset.rename({'Total:':'Total'}, axis=1, inplace=True)

for row in county_census_2010_df_subset.itertuples():
    print(getattr(row, 'Id2'))
    print(getattr(row,'Total'))

# get the last occurence of matching STCO_FIPS for a given Id2 so that new record with year 2010 and Total: can be inserted below that
