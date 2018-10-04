import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None  # default='warn'
"""
TO BE IN SYNC WITH National_Census_1990_All FILE

Notes: Specify the correct index for county and city files respectively.
       Specify the year as needed to skip the 1st row.
       Specify code type as county when working with county files so that appropriate columns are created.
"""

"""
Reads the original csv and returns it in a data-frame
"""


def get_df(file_path, year=None):
    if year == 2000:
        init_df = pd.DataFrame(pd.read_csv(file_path, skiprows=1))  # to skip GEO.id, GEO.id2 etc.. rows
    else:
        init_df = pd.DataFrame(pd.read_csv(file_path))
    return init_df


"""
 Return Id2 column as a series of strings to apply the split_id2 function to each element of the column
"""


def get_id2_series():
    initial_df['Id2'] = initial_df['Id2'].astype(str)
    return pd.Series(initial_df['Id2'])


"""
Helper function to split Id2 column values
split_index is the position where place_fips code ends from the end(reverse) in Id2
"""


def split_id2(id2_ser, split_index, code_type=None):
    if code_type == 'place_fips' or code_type == 'CNTY':
        return id2_ser[split_index:]
    else:
        # if not place_fips/CNTY, then we need STATEFP from Id2 which would be the indices before place_fips
        return id2_ser[:split_index]


"""
Create place_fips, CNTY and STATEFP columns
"""


def create_fips_cols(split_index, census_type=None):

    """
    3) Create a new place_fips column by splitting the place_fips code value from Id2 column
        Convert place_fips/CNTY column types back to int64 to be in sync with the column types in final main file.
    """
    if census_type == 'county':
        initial_df['CNTY'] = id2_series.apply(split_id2, args=(split_index, 'CNTY'))
    else:
        initial_df['place_fips'] = id2_series.apply(split_id2, args=(split_index, 'place_fips'))

    """
    4) Create a new STATEFP column by splitting the STATEFP code value from Id2 column
        Convert STATEFP column type back to int64 to be in sync with the column types in final main file.
    """
    initial_df['STATEFP'] = id2_series.apply(split_id2, args=(split_index, ))

    # Also converting Id2 back to int to preserve original data format
    initial_df['Id2'] = initial_df['Id2'].astype(np.int64)

    """
    6) Place place_fips and STATEFP besides Id2 column
    """
    df_cols = initial_df.columns.tolist()  # to get a list of columns

    # move STATEFP and place_fips columns to required positions.
    df_cols.insert(2, df_cols.pop(df_cols.index('STATEFP')))
    if census_type == 'county':
        df_cols.insert(3, df_cols.pop(df_cols.index('CNTY')))
    else:
        df_cols.insert(3, df_cols.pop(df_cols.index('place_fips')))

    return initial_df.reindex(columns=df_cols)


"""
Create a corresponding YEAR column
"""


def create_year_col(df1, year):
        df1 = df1.assign(YEAR=year)
        return df1


"""
To write final df to a csv
"""


def create_updated_csv(fnl_df, file_path, enc, ind_val):
    fnl_df.to_csv(file_path, encoding=enc, index=ind_val)
    fnl_df = pd.read_csv(file_path)
    print(fnl_df.head())
    # print(df.tail())


"""
1) Obtain the original csv in an initial df
"""
############### TO-DO: Automate reading of files from the required directory so that all iles are modified as required with single run of the program ######################
# initial_df = get_df(('C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_county_2010/DEC_10_SF1_P12_with_ann_county.csv')) # 2010 county census file
# initial_df = get_df('C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_county_2000/DEC_00_SF1_P012_with_ann.csv', 2000) # 2000 county census file
initial_df = get_df(('C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/census_cities_2010/DEC_10_SF1_P12_with_ann_city_FIPS_STATE_PLACE.csv'))   # 2010 city census file
#initial_df = get_df('C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/census_cities_2000/DEC_00_SF1_P012_with_ann.csv', 2000)  # 2000 city census file

"""
2) convert Id2 of int64 type to str type to split into fips state and fips place code respectively and get Id2 column
"""
id2_series = get_id2_series()
# C:\Users\sshaik2\Criminal_Justice\Projects\main_census_merge\utilities\fips_codes_generator.py
# C:\Users\sshaik2\Criminal_Justice\Projects\main_census_merge\data\census_county_2010\DEC_10_SF1_P12_with_ann_county.csv

"""
3) Create df with place_fips/CNTY, STATEFP, YEAR columns
"""
# final_df = create_fips_cols(-3, 'county')  # -3 split index for county Id2
df = create_fips_cols(-5)  # -5 split index for city Id2

"""
4) Create YEAR column
"""
final_df = create_year_col(df, 2000)
print(final_df['YEAR'].head())

"""
5) Write the final modified dataframe with fips place and state columns to a new csv
"""
############# TO-DO : Automate creating new file path and calling create_updated_csv function to write final df to a csv at required location. ##################
# new_file_path = 'C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_county_2010/DEC_10_SF1_P12_with_ann_county_FIPS_STATE_COUNTY.csv' # new 2010 county census file
# new_file_path = 'C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_county_2000/DEC_00_SF1_P012_with_ann_county_FIPS_STATE_COUNTY.csv' # new 2000 county census file
new_file_path = 'DEC_10_SF1_P12_with_ann_city_FIPS_STATE_PLACE.csv' # new 2010 city census file
#new_file_path = 'DEC_00_SF1_P012_with_ann_city_FIPS_STATE_PLACE.csv' # new 2000 city census file

enc_type = 'utf-8'
index_value = False
create_updated_csv(final_df, new_file_path, enc_type, index_value)
