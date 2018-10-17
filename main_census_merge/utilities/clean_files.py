import pandas as pd
import os
import shutil

"""
Helper function to remove unwanted columns from a csv.
Can either return the modified df or write it to a file
"""

# global variable to hold the file path to be used across multiple functions
# file_loc = ''


def remove_unused_cols(file_path, file_out_path, out_type, drop_cols, enc_type='utf-8'):
    initial_file = pd.read_excel(file_path, encoding=enc_type)
    initial_file_df = pd.DataFrame(initial_file)

    initial_file_req_df = initial_file_df.drop(drop_cols, axis=1)

    if out_type == 'file':
        initial_file_req_df.to_csv(file_out_path, encoding='utf-8', index=False)
    elif out_type == 'df':
        return initial_file_req_df


# Removing Byrne, LLEB, WEED, GOT_COPS, HIRING_TOT2, HIRING_RATE columns from main file which won't be used.
'''
remove_unused_cols(file_path='C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/Final_Main_1990_2001.xlsx',
                   enc_type="ISO-8859-1", file_out_path='C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/Final_Main_Var_1990_2001.csv',
                   drop_cols=['BYRNE_DISCRET_580', 'LLEBG_592', 'WEED_AND_SEED_595', 'GOT_COPS', 'HIRING_TOT2', 'HIRING_RATE'], out_type='file')
'''


"""
Remove 2nd column header row i.e Id, Id2, Geography etc..
Rename 
"""


def remove_unused_rows(file_path):
    initial_df = pd.DataFrame(pd.read_csv(file_path, encoding='utf-8'))
    # Dropping the 1st row which has Id, Id2, Geography etc.. values below the 1st column headers. drop() returns a new df
    reduced_df = initial_df.drop(initial_df.index[0])
    return reduced_df


"""
The below function does the following:
 - renames 'GEO.display-label'column to 'placename'
 - extracts the corresponding 'P**' string from the filename and prefixes it to each of the column headers
"""


def update_census_file_headers(df_obj, file_path):
    # rename 'GEO.display-label' col
    df_obj.rename(columns={'GEO.display-label': 'placename'}, inplace=True)

    # extract file name from the file path
    file_name = file_path.split('/')[-1]

    # extract the corresponding 'P**' string from the filename
    file_type = file_name.split('_')[3]

    # get the list of column headers
    col_headers = list(df_obj)

    # create new list of column headers by appending correpsonding P*** string to the existing column headers
    new_col_headers = col_headers[:3]+list(file_type+x for x in col_headers[3:])
    df_obj.columns = new_col_headers
    return df_obj


"""
Write the modified df to modified_files folder
"""


def write_updated_df_file(updated_df, out_path):
    updated_df.to_csv(out_path, encoding='utf-8', index=False)


"""
Iterates over each directory(cities 00/10, counties 00/10) and then works on each census file within that directory
Uses remove_unused_rows, update_all_census_files functions to modify census files to have required headers with corresponding P*** prefixes
"""


def find_census_files_path(data_files_path,ori_files_folder_name, mod_files_folder_name):
    # Switch to the directory which has all the data folders/files
    fp_list=[]
    os.chdir(data_files_path)
    for census_dir in os.listdir():
        if not census_dir.startswith('.'): # to ignore hidden files such as .DS_Store
            census_folder_path = data_files_path+'/'+census_dir

            # move into the county/city census dir
            os.chdir(census_folder_path)

            # overwrite the mod files folder if it already exists
            out_dir_path = census_folder_path + '/' + mod_files_folder_name
            if os.path.exists(out_dir_path):
                shutil.rmtree(out_dir_path)
            os.mkdir(out_dir_path)
            # os.makedirs(out_dir_path) - if subdirectories. Implement if needed like may be pass a list and mkdirs if list len > 1

            # get a list of input files and capture their paths
            for sub_dir in os.listdir():
                if sub_dir == ori_files_folder_name:
                    sub_dir_path = census_folder_path+'/'+sub_dir
                    os.chdir(sub_dir_path)
                    for f in os.listdir():
                        # create input file path
                        in_file = sub_dir_path + '/' + f
                        # create output file path
                        out_file = out_dir_path + '/' + f
                        fp_list.append((in_file, out_file))
    return fp_list


# get the list of input and output file path tuples
file_paths_list = find_census_files_path('C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data',
                        ori_files_folder_name='original_files', mod_files_folder_name='updated_col_headers')


# for every tuple of inp and out file paths, perform the reqd operations
for f_paths in file_paths_list:
    ip_file, op_file = f_paths
    df1 = remove_unused_rows(ip_file)
    updated_df = update_census_file_headers(df1, ip_file)
    write_updated_df_file(updated_df, op_file)