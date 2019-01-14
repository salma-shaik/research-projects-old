import pandas as pd

"""
Interpolate intercensal census data for all the census variables
"""

"""
1. Obtain the national census all file which has census data from 1990 - 2010
"""

nat_cen_all_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_All.csv')

"""
2. Sort the df by 'ORI' and 'YEAR' to get the 3 occurences of each ORI together and then sort by YEAR(10,00,90)
"""
nat_cen_all_sorted = nat_cen_all_df.sort_values(by=['ORI', 'YEAR'], ascending=[True, False])


"""
3. Write the above sorted df to a csv for future use and reference
"""
nat_cen_all_sorted.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_All_Sorted.csv', index=False)