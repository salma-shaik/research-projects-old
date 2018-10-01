import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'

county_census_df = pd.DataFrame(pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/census_county_2010/DEC_10_SF1_P12_with_ann_county.csv'))

# print(county_census_df.dtypes)
"""
Id                             object
Id2                             int64
Geography                      object
Total:                         object
Male:                           int64
Male: - Under 5 years           int64
Male: - 5 to 9 years            int64
Male: - 10 to 14 years          int64
Male: - 15 to 17 years          int64
Male: - 18 and 19 years         int64
Male: - 20 years                int64
Male: - 21 years                int64
Male: - 22 to 24 years          int64
Male: - 25 to 29 years          int64
Male: - 30 to 34 years          int64
Male: - 35 to 39 years          int64
Male: - 40 to 44 years          int64
Male: - 45 to 49 years          int64
Male: - 50 to 54 years          int64
Male: - 55 to 59 years          int64
Male: - 60 and 61 years         int64
Male: - 62 to 64 years          int64
Male: - 65 and 66 years         int64
Male: - 67 to 69 years          int64
Male: - 70 to 74 years          int64
Male: - 75 to 79 years          int64
Male: - 80 to 84 years          int64
Male: - 85 years and over       int64
Female:                         int64
Female: - Under 5 years         int64
Female: - 5 to 9 years          int64
Female: - 10 to 14 years        int64
Female: - 15 to 17 years        int64
Female: - 18 and 19 years       int64
Female: - 20 years              int64
Female: - 21 years              int64
Female: - 22 to 24 years        int64
Female: - 25 to 29 years        int64
Female: - 30 to 34 years        int64
Female: - 35 to 39 years        int64
Female: - 40 to 44 years        int64
Female: - 45 to 49 years        int64
Female: - 50 to 54 years        int64
Female: - 55 to 59 years        int64
Female: - 60 and 61 years       int64
Female: - 62 to 64 years        int64
Female: - 65 and 66 years       int64
Female: - 67 to 69 years        int64
Female: - 70 to 74 years        int64
Female: - 75 to 79 years        int64
Female: - 80 to 84 years        int64
Female: - 85 years and over     int64
dtype: object
"""

# Getting just the top 5 rows to test splitting of id2 into fips state code and fips place code
county_census_df_head = county_census_df.head()

# convert Id2 of int64 type to str type to split into fips state and fips place code respectively
county_census_df_head['Id2'] = county_census_df_head['Id2'].astype(str)

# print("Id2 dtype after conversion", county_census_df_head['Id2'].dtypes)

# helper function to split Id2 column values
def split_id2(id2_col, split_index):
    return id2_col[split_index:], id2_col[split_index:]

# obtaining Id2 column as a series to apply the split_id2 function to each element of the column
id2_series = pd.Series(county_census_df_head['Id2'])
county_census_df_head['FIPS_STATE'], county_census_df_head['FIPS_PLACE'] = id2_series.apply(split_id2, args=(-3,))
print(county_census_df_head['FIPS_STATE'], county_census_df_head['FIPS_PLACE'])
