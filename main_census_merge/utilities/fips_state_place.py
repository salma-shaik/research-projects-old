import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None  # default='warn'


"""
Returns the original csv in a dataframe
"""
def get_df(file_path, year=None):
    if year==2000:
        df = pd.DataFrame(pd.read_csv(file_path, skiprows=1))
    else:
        df = pd.DataFrame(pd.read_csv(file_path))
    return df


"""
1) Obtain the original csv in an initial df
"""
# initial_df = get_df(('C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_county_2010/DEC_10_SF1_P12_with_ann_county.csv')) # 2010 county census file
# initial_df = get_df(('C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_county_2000/DEC_00_SF1_P12_with_ann.csv', 2000)) # 2010 county census file
# initial_df = get_df(('C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_cities_2010/DEC_10_SF1_P12_with_ann_city.csv'))   # 2010 city census file
initial_df = get_df('C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_cities_2000/DEC_00_SF1_P012_with_ann.csv', 2000) # # 2000 city census file

"""
 Return Id2 column as a series to apply the split_id2 function to each element of the column
"""
def get_id2_series():
    initial_df['Id2'] = initial_df['Id2'].astype(str)
    return pd.Series(initial_df['Id2'])


"""
2) convert Id2 of int64 type to str type to split into fips state and fips place code respectively and get Id2 column
"""
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
def create_fips_place_state_cols(split_index):

    """
    3) create a new FIPS_PLACE column by splitting the FIPS_PLACE code value from Id2 column
    """
    initial_df['FIPS_PLACE'] = id2_series.apply(split_id2, args=(split_index, 'FIPS_PLACE'))

    """
    4) create a new FIPS_STATE column by splitting the FIPS_STATE code value from Id2 column
    """
    initial_df['FIPS_STATE'] = id2_series.apply(split_id2, args=(split_index, ))

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


"""
3) Create final df with FIPS_PLACE and FIPS_STATE columns
"""
# final_df = create_fips_place_state_cols(-3) # -3 split index for county Id2
final_df = create_fips_place_state_cols(-5) # -5 split index for city Id2


"""
To write final df to a csv
"""
def create_updated_csv(df, file_path, enc, ind_val):
    df.to_csv(file_path, encoding=enc, index=ind_val)
    df = pd.read_csv(file_path)
    print(df.head())
    # print(df.tail())



# new_file_path = 'C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_county_2010/DEC_10_SF1_P12_with_ann_county_FIPS_PLACE_STATE.csv' # new 2010 county census file
# new_file_path = 'C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_county_2000/DEC_00_SF1_P012_with_ann_county_FIPS_PLACE_STATE.csv' # new 2000 county census file
# new_file_path = 'C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_cities_2010/DEC_10_SF1_P12_with_ann_city_FIPS_PLACE_STATE.csv' # new 2010 city census file
new_file_path = 'C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_cities_2000/DEC_00_SF1_P12_with_ann_city_FIPS_PLACE_STATE.csv' # new 2000 city census file
enc_type = 'utf-8'
index_value = False

"""
4) Write the final modified dataframe with fips place and state columns to a new csv
"""
create_updated_csv(final_df, new_file_path, enc_type, index_value)
