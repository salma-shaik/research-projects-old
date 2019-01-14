import pandas as pd

from datetime import datetime

pd.options.mode.chained_assignment = None

"""
Subset the nat_cen_all_sorted df to get the population variables' columns
"""

print("########## Start: ", datetime.now().time())

nat_cen_all = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_All_Sorted.csv')

# Get the required columns from the national all census file.
pop_vars = nat_cen_all[['YEAR', 'POP100', 'White_count', 'Black_count', 'Hispanic_count', 'Age1524_WhiteM', 'White_Males_All', 'Age1524_WhiteF',
                        'White_Females_All', 'Age1524_BlackM', 'Black_Males_All', 'Age1524_BlackF', 'Black_Females_All','Hispanic_Males_All',
                        'Age1524_HispanicM', 'Age1524_HispanicF', 'Hispanic_Females_All', 'Pct_WYM', 'Pct_WYF']]


# Create an empty df to append the original rows and empty rows for every iteration of the original nat_cen_all df.
pop_var_int = pd.DataFrame(columns = pop_vars.columns)

# for each row of the pop_vars df, append 9 empty rows if the year is != 1990 coz we are interpolating till 1990.
for row in pop_vars.itertuples():
    # ????? ###
    pop_var_int = pop_var_int.append(pd.Series(row[1:], index=pop_vars.columns), ignore_index=True)
    if row.YEAR != 1990:
        for i in range(9):
            pop_var_int = pop_var_int.append(pd.Series(), ignore_index=True)

# Drop the YEAR column
pop_var_int = pop_var_int.drop(['YEAR'], axis=1)

# Interpolate. This fills all the NaN rows between 2 given years that were added above.
pop_var_int = pop_var_int.interpolate(method='linear', axis=0)

print("########## End: ", datetime.now().time()) # --> Process between line 11-line 38 takes around 30 minutes

# Write the df with interpolated values for all population variables to a csv
pop_var_int.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_All_Pop_Vars_Interpolated.csv', index=1)

# Get the fixed columns and years file into a df
fixed_rows_yr = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_FixedRows_Year.csv')

# concatenate fixed columns, year and population variables together vertically
final_int_df = pd.concat([fixed_rows_yr, pop_var_int], axis=1)

# Write the final interpolated file to a csv
final_int_df.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_All_Interpolated.csv', index=False)