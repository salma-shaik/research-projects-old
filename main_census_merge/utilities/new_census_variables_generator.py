import pandas as pd
from main_census_merge.utilities import clean_files as cf


"""
Helper function to create POP100 column which is the Total: column renamed as P012VD01 for 2000, P12D001 for 2010
"""
# First obtain the paths to read input file and to write output file
fp_list = cf.find_census_files_path('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data', 'modified_files', 'modified_files_fips')


