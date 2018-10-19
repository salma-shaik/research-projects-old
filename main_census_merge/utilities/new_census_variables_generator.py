import os
import shutil
import pandas as pd
import numpy as np
from main_census_merge.utilities import clean_files as cf
from main_census_merge.utilities import fips_codes_generator as fcg

"""
Helper function to create POP100 column which is the Total: column renamed as P012VD01 for 2000, P12D001 for 2010
"""


def create_new_census_cols(initial_df, new_df, pop_var, new_cen_vars=True):
    if new_cen_vars is False:
        new_df[f'{pop_var}'] = initial_df.iloc[:, 6]
    else:
        new_df[f'{pop_var}_count'] = initial_df.iloc[:, 6]
        new_df[f'Age1524_{pop_var}M'] = initial_df.iloc[:, 11:16].sum(axis=1)
        new_df[f'{pop_var}_Males_All'] = initial_df.iloc[:, 7]
        new_df[f'Age1524_{pop_var}F'] = initial_df.iloc[:, 35:40].sum(axis=1)
        new_df[f'{pop_var}_Females_All'] = initial_df.iloc[:, 31]

        if pop_var == 'White':
            new_df['Pct_WYM'] = new_df['Age1524_WhiteM']/new_df['White_Males_All']
            new_df['Pct_WYF'] = new_df['Age1524_WhiteF'] / new_df['White_Females_All']

        return new_df


if __name__ == '__main__':
    data_files_path = 'C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data'
    ori_files_folder_name = 'new_fips_cols'
    mod_files_folder_name = 'new_census_variables'
    os.chdir(data_files_path)
    for census_dir in os.listdir():
        if not census_dir.startswith('.') and census_dir != 'National_Census_00_10_All.csv':  # to ignore hidden files such as .DS_Store

            # create a new df for everytime we move into new census dir so that the data from previous iteration is not carried over as was happening with 2000 county census file
            new_df = pd.DataFrame()

            census_folder_path = data_files_path + '/' + census_dir
            # move into the county/city census dir
            os.chdir(census_folder_path)

            # get a list of input files and capture their paths
            for sub_dir in os.listdir():
                if sub_dir == ori_files_folder_name:
                    sub_dir_path = census_folder_path + '/' + sub_dir
                    os.chdir(sub_dir_path)
                    for f in os.listdir():
                        # create input file path
                        in_file = sub_dir_path + '/' + f
                        # create output file path
                        census_type, census_year = fcg.get_census_type_year(in_file)
                        pop_type = in_file.split('/')[-1].split('_')[3]
                        initial_df = pd.read_csv(in_file)

                        # can create only POP100 column
                        if pop_type == 'P012' or pop_type == 'P12':
                            create_new_census_cols(initial_df, new_df, 'POP100', new_cen_vars=False)
                        elif pop_type == 'P012A' or pop_type == 'P12A':
                            create_new_census_cols(initial_df, new_df,  'White')
                        elif pop_type == 'P012B' or pop_type == 'P12B':
                            create_new_census_cols(initial_df, new_df, 'Black')
                        elif pop_type == 'P012H' or pop_type == 'P12H':
                            create_new_census_cols(initial_df, new_df, 'Hispan')

            gov_fips_yr_df = initial_df.iloc[:, :6]
            final_df = gov_fips_yr_df.combine_first(new_df)

            # Rearrange the columns to match the respective positions in national_Census_1990_all file
            final_var_df =  fcg.arrange_cols(final_df, final_df.columns.tolist(),
                                                                  {0:'Govt_level', 1:'place_fips', 2:'placename', 3:'CNTY', 4:'STATEFP', 5:'YEAR',
                                                                   6:'POP100', 7:'White_count', 8:'Black_count', 9:'Hispan_count',
                                                                   10:'Age1524_WhiteM', 11:'White_Males_All', 12:'Age1524_WhiteF', 13:'White_Females_All',
                                                                   14:'Age1524_BlackM', 15:'Black_Males_All', 16:'Age1524_BlackF', 17:'Black_Females_All',
                                                                   18:'Hispan_Males_All', 19:'Age1524_HispanM', 20:'Age1524_HispanF', 21:'Hispan_Females_All',
                                                                   22:'Pct_WYM', 23:'Pct_WYF'})

            # overwrite the mod files folder if it already exists
            out_dir_path = census_folder_path + '/' + mod_files_folder_name
            if os.path.exists(out_dir_path):
                shutil.rmtree(out_dir_path)
            os.mkdir(out_dir_path)
            # os.makedirs(out_dir_path) - if subdirectories. Implement if needed like may be pass a list and mkdirs if list len > 1
            out_file = out_dir_path + '/' + 'new_vars_'+ census_dir + '.csv'
            #final_var_df.fillna(0)
            cf.write_updated_df_file(final_var_df, out_file)


# stack all the individual new census variables dataframes together to create a final csv similar to National_Census_1990_All file
# counties_2000_df = pd.read_csv('C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/census_county_2000/new_census_variables/new_vars_census_county_2000.csv')
# counties_2010_df = pd.read_csv('C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/census_county_2010/new_census_variables/new_vars_census_county_2010.csv')
# cities_2000_df = pd.read_csv('C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/census_cities_2000/new_census_variables/new_vars_census_cities_2000.csv')
# cities_2010_df = pd.read_csv('C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/census_cities_2010/new_census_variables/new_vars_census_cities_2010.csv')
#
#
# national_census_2000_2010_all_df = counties_2000_df.append([counties_2010_df, cities_2000_df, cities_2010_df])
# cf.write_updated_df_file(national_census_2000_2010_all_df, 'C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/National_Census_00_10_All.csv')

# print(national_census_2000_2010_all_df.head())