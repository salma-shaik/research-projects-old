import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None  # default='warn'
"""
Notes: Specify the correct index for county and city files respectively.
       Specify the year as needed to skip the 1st row.
       Specify code type as county when working with county files so that appropriate columns are created.
"""

"""
Returns the original csv in a dataframe
"""
def get_df(file_path, year=None):
    if year==2000:
        df = pd.DataFrame(pd.read_csv(file_path, skiprows=1)) # to skip GEO.id, GEO.id2 etc.. rows
    else:
        df = pd.DataFrame(pd.read_csv(file_path))
    return df


"""
1) Obtain the original csv in an initial df
"""
# initial_df = get_df(('C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_county_2010/DEC_10_SF1_P12_with_ann_county.csv')) # 2010 county census file
# initial_df = get_df('C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_county_2000/DEC_00_SF1_P012_with_ann.csv', 2000) # 2000 county census file
# initial_df = get_df(('C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_cities_2010/DEC_10_SF1_P12_with_ann_city.csv'))   # 2010 city census file
initial_df = get_df('C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_cities_2000/DEC_00_SF1_P012_with_ann.csv', 2000) # # 2000 city census file

"""
 Return Id2 column as a series to apply the split_id2 function to each element of the column
"""
def get_id2_series():
    initial_df['Id2'] = initial_df['Id2'].astype(str)
    return pd.Series(initial_df['Id2'])


"""
2) convert Id2 of int64 type to str type to split into fips state and fips plac    code respectively and get Id2 column
"""
id2_series = get_id2_series()


"""
Helper function to split Id2 column values
split_index is the position where FIPS_PLACE code ends in Id2
"""
def split_id2(id2_series, split_index, code_type=None):
    if code_type == 'FIPS_PLACE' or code_type == 'FIPS_COUNTY':
        return id2_series[split_index:]
    else:
        # if not FIPS_PLACE/FIPS_COUNTY, then we need FIPS_STATE from Id2 which would be the indices before FIPS_PLACE
        return id2_series[:split_index]


"""
Create FIPS_PLACE and FIPS_STATE columns
"""
def create_fips_cols(split_index, census_type=None):

    """
    3) Create a new FIPS_PLACE column by splitting the FIPS_PLACE code value from Id2 column
        Convert FIPS_PLACE/FIPS_COUNTY column types back to int64 to be in sync with the column types in final main file.
    """
    if census_type == 'county':
        initial_df['FIPS_COUNTY'] = id2_series.apply(split_id2, args=(split_index, 'FIPS_COUNTY'))
        initial_df['FIPS_COUNTY'] = initial_df['FIPS_COUNTY'].astype(np.int64)
    else:
        initial_df['FIPS_PLACE'] = id2_series.apply(split_id2, args=(split_index, 'FIPS_PLACE'))
        initial_df['FIPS_PLACE'] = initial_df['FIPS_PLACE'].astype(np.int64)

    """
    4) Create a new FIPS_STATE column by splitting the FIPS_STATE code value from Id2 column
        Convert FIPS_STATE column type back to int64 to be in sync with the column types in final main file.
    """
    initial_df['FIPS_STATE'] = id2_series.apply(split_id2, args=(split_index, ))

    # Also converting Id2 back to int to preserve original data format
    initial_df['Id2'] = initial_df['Id2'].astype(np.int64)

    """
    6) Place FIPS_PLACE and FIPS_STATE besides Id2 column
    """
    df_cols = initial_df.columns.tolist() # to get a list of columns

    # move FIPS_STATE and FIPS_PLACE columns to required positions.
    df_cols.insert(2, df_cols.pop(df_cols.index('FIPS_STATE')))
    if census_type == 'county':
        df_cols.insert(3, df_cols.pop(df_cols.index('FIPS_COUNTY')))
    else:
        df_cols.insert(3, df_cols.pop(df_cols.index('FIPS_PLACE')))

    return initial_df.reindex(columns=df_cols)


"""
3) Create final df with FIPS_PLACE/FIPS_COUNTY and FIPS_STATE columns
"""
# final_df = create_fips_cols(-3, 'county') # -3 split index for county Id2
final_df = create_fips_cols(-5) # -5 split index for city Id2


"""
To write final df to a csv
"""
def create_updated_csv(df, file_path, enc, ind_val):
    df.to_csv(file_path, encoding=enc, index=ind_val)
    df = pd.read_csv(file_path)
    print(df.head())
    # print(df.tail())



# new_file_path = 'C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_county_2010/DEC_10_SF1_P12_with_ann_county_FIPS_STATE_COUNTY.csv' # new 2010 county census file
# new_file_path = 'C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_county_2000/DEC_00_SF1_P012_with_ann_county_FIPS_STATE_COUNTY.csv' # new 2000 county census file
# new_file_path = 'C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_cities_2010/DEC_10_SF1_P12_with_ann_city_FIPS_STATE_PLACE.csv' # new 2010 city census file
new_file_path = 'C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_cities_2000/DEC_00_SF1_P012_with_ann_city_FIPS_STATE_PLACE.csv' # new 2000 city census file

enc_type = 'utf-8'
index_value = False

"""
4) Write the final modified dataframe with fips place and state columns to a new csv
"""
create_updated_csv(final_df, new_file_path, enc_type, index_value)
