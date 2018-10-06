import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None  # default='warn'
"""
TO BE IN SYNC WITH National_Census_1990_All FILE

Notes: Specify the correct index for county and city files respectively.
       Specify the year as needed to skip the 1st row.
       Specify code type as county when working with county files so that appropriate columns are created.
"""

# Every time a file is read get the census type and census year to be used across various functions

census_type = ''
census_year = ''


"""
Returns the census type of the current file being read
"""


def get_census_type_year(file_path): # pass the indexes of census type and year wor dlocations in the file name if reqd. Need to agree upon either having uniform file names or passing on the indexes
    en_type = ''
    # Get a list of all the navigation folders in the file path
    fp_words = file_path.split('/')

    # Get a list of words in the folder name
    fdn_words = fp_words[-3].split('_')

    if 'county' in fdn_words:
        cen_type = 'county'
    elif 'city' in fdn_words:
        cen_type = 'city'

    # Extract the year from the file name list of words
    cen_year = fp_words[-1].split('_')[-5]  # get year which is in the 5th position from the end

    return (cen_type, cen_year)


"""
Reads the original csv and returns it in a data-frame
"""


def get_df(file_path):
    init_df = pd.DataFrame(pd.read_csv(file_path))
    return init_df


"""
 Return GEO.id2 column as a series of strings to apply the split_geo_id2 function to each element of the column
"""


def get_geo_geo_id2_ser(ini_df):
    ini_df['GEO.id2'] = ini_df['GEO.id2'].astype(str)
    return pd.Series(ini_df['GEO.id2'])


"""
Helper function to split GEO.id2 column values
split_index is the position where place_fips code ends from the end(reverse) in GEO.id2
"""


def split_geo_id2(geo_id2, split_index, code_type=None):
    if code_type == 'place_fips' or code_type == 'CNTY':
        return geo_id2[split_index:]
    else:
        # if not place_fips/CNTY, then we need STATEFP from GEO.id2 which would be the indices before place_fips
        return geo_id2[:split_index]


"""
Helper function to prefix county fips value with zeroes as required so as to make all of them 3 chars long 
"""


def update_code_len(fips_code, fp_type):
    req_code_len = ''  # placeholder to assign required code length based on whether it is a city, county or state fips code
    if fp_type == 'city':
        req_code_len = 2
    elif fp_type == 'county':
        req_code_len = 3
    elif census_type == 'city':
        req_code_len == 5
    while fips_code.__len__() < req_code_len:
        fips_code = '0' + fips_code
        return fips_code


"""
Helper function to create a new column with constant value
"""


def create_new_col(df, name, val):
    df[name] = val
    return df


"""
Helper function to move columns to the required locations
"""


def arrange_cols(df, df_cols, cols_dict):
    for ind, col in cols_dict.iteritems():
        df.insert(ind, df_cols.pop(df_cols.index(col)))
    return df.reindex(columns=df_cols)


"""
Create place_fips, CNTY and STATEFP columns
"""


def create_fips_cols(ini_df, geo_id2_ser):
    split_index = '' # placeholder to set split_index based on the census type -> -3 for county and -5 for city
    fips_code_type = ''  # placeholder to assign whether it is a city, county or state fips code type

    """
    3) Create a new place_fips column by splitting the place_fips code value from GEO.id2 column
        Convert place_fips/CNTY column types back to int64 to be in sync with the column types in final main file.
    """
    if census_type == 'county':
        split_index = -3
        fips_code_type = 'county'

        # split county code from geo id2
        ini_df['CNTY'] = geo_id2_ser.apply(split_geo_id2, args=(split_index, 'CNTY'))

        # convert all county codes to be 3 chars long as reqd
        ini_df['CNTY'] = ini_df['CNTY'].apply(update_code_len, args=(fips_code_type))

        # create place_fips col by appending '99' to the CNTY code
        ini_df['place_fips'] = ['99'+x for x in ini_df['CNTY']]

        # create a Govt_level column with value 1 for county
        ini_df = create_new_col('Govt_level', 1)

    elif census_type == 'city':
        split_index = -5
        fips_code_type = 'city'

        # get fips place code from geo id2
        ini_df['place_fips'] = geo_id2_ser.apply(split_geo_id2, args=(split_index, 'place_fips'))

        # convert all fips place code to be 5 char long by appending with 0s as required
        ini_df['place_fips'] = ini_df['place_fips'].apply(update_code_len, args=(fips_code_type))

        # create a Govt_level column with value 3 for city
        ini_df = create_new_col('Govt_level', 3)

    """
    4) Create a new STATEFP column by splitting the STATEFP code value from GEO.id2 column
    """
    # First get the state fips code from geo id2
    ini_df['STATEFP'] = geo_id2_ser.apply(split_geo_id2, args=(split_index, ))

    # Convert all state fips codes to be 2 chars long by prefixing with 0s as required
    fips_code_type = 'state'
    ini_df['STATEFP'] = ini_df['STATEFP'].apply(update_code_len, args=(fips_code_type))

    # Create a YEAR column with value = census_year obtained at the beginning while reading the file
    ini_df['YEAR'] = create_new_col('YEAR', census_year)

    # dropping GEO.id, GEO.id2 columns as they no longer will be needed in the final national census all file
    ini_df = ini_df.drop(['GEO.id', 'GEO.id2'], axis=1)

    """
    6) Place Govt_level in 1st col, place_fips in 2nd col, placename in 3rd col, CNTY in 4th col and STATEFP in 5th col
    """
    df_cols = ini_df.columns.tolist()  # to get a list of columns

    ini_df = arrange_cols(ini_df, df_cols, {1:'Govt_level', 2:'place_fips', 3:'placename', 4:'CNTY', 5:'STATEFP'})

    return ini_df


"""
To write final df to a csv
"""


def create_updated_csv(fnl_df, file_path, enc, ind_val):
    fnl_df.to_csv(file_path, encoding=enc, index=ind_val)
    fnl_df = pd.read_csv(file_path)
    print(fnl_df.head())
    # print(df.tail())


def add_fips_cols(file_path):
    """
    1) Obtain the original csv in an initial df
    """
    initial_df = get_df(file_path)

    """
    2) convert GEO.id2 of int64 type to str type to split into fips state and fips place code respectively and get GEO.id2 column
    """
    geo_id2_series = get_geo_geo_id2_ser(initial_df)

    """
    3) Create df with place_fips/CNTY, STATEFP, YEAR columns
    """
    df = create_fips_cols(ini_df=initial_df, geo_id2_ser=geo_id2_series)


############### TO-DO: Automate reading of files from the required directory so that all iles are modified as required with single run of the program ######################
# ini_df = get_df(('C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_county_2010/DEC_10_SF1_P12_with_ann_county.csv')) # 2010 county census file
# ini_df = get_df('C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_county_2000/DEC_00_SF1_P012_with_ann.csv', 2000) # 2000 county census file

# First get census type to set it to the global census type variable
file_loc = 'C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_county_2010/modified_files/DEC_10_SF1_P12_with_ann_county.csv'
(census_type, census_year) = get_census_type_year(file_loc)
add_fips_cols(file_loc)   # 2010 city census file
#ini_df = get_df('C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/census_cities_2000/DEC_00_SF1_P012_with_ann.csv', 2000)  # 2000 city census file


# geo_id2_ser = get_geo_id2_ser()
# C:\Users\sshaik2\Criminal_Justice\Projects\main_census_merge\utilities\fips_codes_generator.py
# C:\Users\sshaik2\Criminal_Justice\Projects\main_census_merge\data\census_county_2010\DEC_10_SF1_P12_with_ann_county.csv


# final_df = create_fips_cols(-3, 'county')  # -3 split index for county GEO.id2
# df = create_fips_cols(-5)  # -5 split index for city GEO.id2

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
