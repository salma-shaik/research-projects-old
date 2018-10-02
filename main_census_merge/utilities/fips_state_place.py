import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None  # default='warn'

"""
Returns the original csv in a dataframe
"""


def get_df(file_path):
    df = pd.DataFrame(pd.read_csv(file_path))
    return df


# initial_df = get_df(('C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_county_2010/DEC_10_SF1_P12_with_ann_county.csv')) # 2010 county census file
initial_df = get_df(('C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_county_2000/DEC_00_SF1_P012_with_ann.csv'))
# print(county_census_df.dtypes)
"""
DEC_10_SF1_P12_with_ann_county.csv
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



"""
   1) convert Id2 of int64 type to str type to split into fips state and fips place code respectively
   2) returning Id2 column as a series to apply the split_id2 function to each element of the column
"""


def get_id2_series():
    # Getting just the top 5 rows to test splitting of id2 into fips state code and fips place code
    # county_census_df_head = county_census_df.head()

    initial_df['Id2'] = initial_df['Id2'].astype(str)
    return pd.Series(initial_df['Id2'])


id2_series = get_id2_series()


"""
Helper function to split Id2 column values
split_index is the position where FIPS_PLACE code ends in Id2
"""


def split_id2(id2_series, split_index, code_type=None):
    if code_type == 'FIPS_PLACE':
        return id2_series[split_index:]
    else:
        # if not FIPS_PLACE, then we need FIPS_STATE from Id2 which would be the indices before FIPS_PLACE
        return id2_series[:split_index]


"""
Create FIPS_PLACE and FIPS_STATE columns
"""


def create_fips_place_state_cols():
    """
    3) create a new FIPS_PLACE column by splitting the FIPS_PLACE code value from Id2 column
    """
    initial_df['FIPS_PLACE'] = id2_series.apply(split_id2, args=(-3, 'FIPS_PLACE'))

    """
    4) create a new FIPS_STATE column by splitting the FIPS_STATE code value from Id2 column
    """
    initial_df['FIPS_STATE'] = id2_series.apply(split_id2, args=(-3, ))

    """
    5) Convert FIPS_PLACE and FIPS_STATE column types back to int64 to be in sync with the column types in final main file.
    """
    # Also converting Id2 back to int to preserve original data format
    initial_df['Id2'] = initial_df['Id2'].astype(np.int64)
    initial_df['FIPS_PLACE'] = initial_df['FIPS_PLACE'].astype(np.int64)
    initial_df['FIPS_STATE'] = initial_df['FIPS_STATE'].astype(np.int64)

    """
    6) Place FIPS_PLACE and FIPS_STATE besides Id2 column
    """
    df_cols = initial_df.columns.tolist() # to get a list of columns

    # move FIPS_STATE and FIPS_PLACE columns to required positions.
    df_cols.insert(2, df_cols.pop(df_cols.index('FIPS_STATE')))
    df_cols.insert(3, df_cols.pop(df_cols.index('FIPS_PLACE')))

    return initial_df.reindex(columns=df_cols)


final_df = create_fips_place_state_cols()


def create_updated_csv(df, file_path, enc, ind_val):
    """
    7) Write the modified dataframe to a new csv
    """
    df.to_csv(file_path, encoding=enc, index=ind_val)
    df = pd.read_csv(file_path)
    print(df.head())
    # print(df.tail())


# new_file_path = 'C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_county_2010/DEC_10_SF1_P12_with_ann_county_FIPS_PLACE_STATE.csv' # new 2010 county census file
new_file_path = 'C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_county_2000/DEC_00_SF1_P012_with_ann_county_FIPS_PLACE_STATE.csv'
enc_type = 'utf-8'
index_value = False
create_updated_csv(final_df, new_file_path, enc_type, index_value)
