import pandas as pd


counties_2000_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/census_county_2000/new_census_variables/new_vars_census_county_2000.csv')
cities_2000_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/census_cities_2000/new_census_variables/new_vars_census_cities_2000.csv')

national_census_2000_all_df = counties_2000_df.append([cities_2000_df])

national_census_2000_all_df = national_census_2000_all_df.rename({'place_fips':'place_fips_00', 'STATEFP':'STATEFP_00', 'Govt_level':'Govt_level_00'}, axis=1)
national_census_2000_all_df.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/National_Census_2000_All.csv', index=False)

counties_2010_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/census_county_2010/new_census_variables/new_vars_census_county_2010.csv')
cities_2010_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/census_cities_2010/new_census_variables/new_vars_census_cities_2010.csv')

national_census_2010_all_df = counties_2010_df.append([cities_2010_df])
national_census_2010_all_df = national_census_2010_all_df.rename({'place_fips':'place_fips_10', 'STATEFP':'STATEFP_10', 'Govt_level':'Govt_level_10'}, axis=1)
national_census_2010_all_df.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/National_Census_2010_All.csv', index=False)


lnkng_crswlk_df = pd.read_excel('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/crosswalk_improved_2006.xlsx')
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
# print(lnkng_crswlk_df[['fips_place', 'fips_state', 'CGOVTYPE']].head())
lnkng_crswlk_df1 = lnkng_crswlk_df[['fips_place', 'fips_state', 'CGOVTYPE']]
# print(lnkng_crswlk_df1.head())

# Rename 'fips_place', 'fips_state', 'CGOVTYPE' to 'place_fips', 'STATEFP', 'Govt_level' to match national census file
lnkng_crswlk_df1 = lnkng_crswlk_df1.rename({'fips_place':'place_fips', 'fips_state':'STATEFP', 'CGOVTYPE':'Govt_level'}, axis='columns')
lnkng_crswlk_df1 = lnkng_crswlk_df1.rename({'place_fips':'place_fips_lc', 'STATEFP':'STATEFP_lc', 'Govt_level':'Govt_level_lc'}, axis='columns')
lnkng_crswlk_df1.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/Linking_Crosswalk_Fips_Govtlevel.csv', index=False)



# print(lnkng_crswlk_df1.head())

# print(natnl_cen_df['place_fips'].count())
# print(lnkng_crswlk_df1['place_fips'].count())


# get the count of unique entries from national census file
# natnl_crswlk_merge_all = national_census_2000_all_df.merge(lnkng_crswlk_df1.drop_duplicates(), on=['place_fips', 'STATEFP'], how='left', indicator=True)
#
# print((natnl_crswlk_merge_all['_merge'] == 'left_only').count())