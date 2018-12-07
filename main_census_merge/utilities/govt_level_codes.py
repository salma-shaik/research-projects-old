import pandas as pd


counties_2000_df = pd.read_csv('/Users/sshaik2/projects/research-projects/main_census_merge/data/census_county_2000/new_census_variables/new_vars_census_county_2000.csv')
cities_2000_df = pd.read_csv('/Users/sshaik2/projects/research-projects/main_census_merge/data/census_cities_2000/new_census_variables/new_vars_census_cities_2000.csv')
"""
Append 2000 cities to 2000 counties
"""
national_census_2000_all_df = counties_2000_df.append([cities_2000_df])
# print(national_census_2000_all_df.shape[0]) # --> (rows, columns) - (28291, 24)
national_census_2000_fips = national_census_2000_all_df[['place_fips', 'STATEFP', 'Govt_level', 'placename']]

counties_2010_df = pd.read_csv('/Users/sshaik2/projects/research-projects/main_census_merge/data/census_county_2010/new_census_variables/new_vars_census_county_2010.csv')
cities_2010_df = pd.read_csv('/Users/sshaik2/projects/research-projects/main_census_merge/data/census_cities_2010/new_census_variables/new_vars_census_cities_2010.csv')
"""
Append 2010 cities to 2010 counties
"""
national_census_2010_all_df = counties_2010_df.append([cities_2010_df])
# print(national_census_2010_all_df.shape[0]) # --> (rows, columns) -- (32404, 24)

lnkng_crswlk_df = pd.read_excel('/Users/sshaik2/projects/research-projects/main_census_merge/data/crosswalk_improved_2006.xlsx')
"""
# Crosswalk file variables
SOURCE
STATE
UORI
UAGENCY
UCORI
UMULTICO
USTATENO
UCOUNTY
UCTYNAME
UMSA
UPOPGRP
UPOPCOV
UADD1
UADD2
UADD3
UADD4
UADD5
CSTATENO
CGOVIDNU
CGOVIDST
CGOVTYPE
CNAME
CPOP94
FSTATE
FCOUNTY
FPLACE
FMSA
FMSANAME
FCMSA
ORI
fpl
st_pl_fips
fips_place
fips_state
fips_county
zip_code
"""
lnkng_crswlk_fips_cgov_df = lnkng_crswlk_df[['fips_place', 'fips_state', 'CGOVTYPE']]
"""
Rename 'fips_place', 'fips_state', 'CGOVTYPE' to 'place_fips', 'STATEFP', 'Govt_level' to match national census file
"""
lnkng_crswlk_fips_cgov_df = lnkng_crswlk_fips_cgov_df.rename({'fips_place':'place_fips', 'fips_state':'STATEFP', 'CGOVTYPE':'Govt_level'}, axis='columns')
lnkng_crswlk_fips_cgov_df.to_csv('/Users/sshaik2/projects/research-projects/main_census_merge/data/lnkng_crswlk_fips_cgov.csv', index=False)
# print(lnkng_crswlk_fips_cgov_df.shape[0]) # --> (rows, columns) -- (23521, 3)

"""
Check the differences between national_census_2000_all_df and lnkng_crswlk_fips_cgov_df 
i.e trying to obtain fips place, state that are in national_census_2000_all_df but not in lnkng_crswlk_fips_cgov_df
"""
nat_cen_00_lc_merged_df = national_census_2000_fips.merge(lnkng_crswlk_fips_cgov_df.drop_duplicates(), on=['STATEFP', 'place_fips'], how='left', validate='one_to_one', indicator=True)

nat_cen_00_lc_merged_df.to_csv('/Users/sshaik2/projects/research-projects/main_census_merge/data/cen_00_lc_merged.csv', index=False)
# print((nat_cen_00_lc_merged_df['_merge'] == 'left_only').count())