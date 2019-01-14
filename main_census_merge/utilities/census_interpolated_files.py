import pandas as pd

fixed_rows_yr = pd.read_csv('/Users/sshaik2/projects/research/research-projects/main_census_merge/data/wip_merge_files/National_Census_FixedRows_Year.csv')
cen_var = pd.read_csv('/Users/sshaik2/projects/research/research-projects/main_census_merge/data/wip_merge_files/National_Census_All_Pop_Vars_Interpolated.csv')

final_int_df = pd.concat([fixed_rows_yr, cen_var], axis=1)

final_int_df.to_csv('/Users/sshaik2/projects/research/research-projects/main_census_merge/data/wip_merge_files/National_Census_All_Interpolated.csv', index=False)