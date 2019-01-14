import pandas as pd

"""
We need to create an YEAR column with all the years between 2010 to 2000 and then between 2000 and 1990
Create a dataframe with 2010-1990 years and replicate it as many times required to fill up the existing dataframe length
"""

"""
Read the National_Census_FixedRows.csv to append YEAR column to it
"""
nat_cen_fixed_rows = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_FixedRows.csv')

# Get the column length of the dataframe
col_len = nat_cen_fixed_rows.__len__() # 212247. /21 is 10107

years = pd.DataFrame({'YEAR': [2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001,
                         2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990]})

years_rep = pd.concat([years]*10107, ignore_index=True)

nat_cen_fixed_rows_yr = pd.concat([nat_cen_fixed_rows, years_rep], axis=1)

nat_cen_fixed_rows_yr.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_FixedRows_Year.csv', index=False)
