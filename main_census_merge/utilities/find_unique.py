import pandas as pd

"""
# Finding Id2 from DEC_10_SF1_P12_with_ann_county.csv that don't have a matching STCO_FIPS in Final_Main_Var_1990_2001.csv file
main_file_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/Final_Main_Var_1990_2001.csv')
main_file_stco_fips_set = set(main_file_df['STCO_FIPS'])
print(main_file_stco_fips_set.__len__())

county_census_2010_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/census_county_2010/DEC_10_SF1_P12_with_ann.csv', encoding = "ISO-8859-1")
county_census_2010_df_id2_set = set(county_census_2010_df['GEO.id2'])

print(county_census_2010_df_id2_set.__len__())
print((county_census_2010_df_id2_set-main_file_stco_fips_set).__len__())
"""


