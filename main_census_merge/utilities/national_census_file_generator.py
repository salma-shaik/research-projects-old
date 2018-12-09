import pandas as pd

pd.options.mode.chained_assignment = None


def get_final_main_cgovtype_ori_agency(file_path):
    """
        Obtain ORI, AGENCY, CGOVTYPE, FIPS_STATE, FIPS_PLACE from final main(90-01) file
    """
    final_main_df = pd.read_csv(file_path)
    final_main_fips_ori_agency = final_main_df[['ORI', 'AGENCY', 'CGOVTYPE', 'FIPS_STATE', 'FIPS_PLACE']]

    """
    1. Obtain only unique records from the final main file - key: fips place + fips state
    """
    final_main_fips_ori_agency_unique = final_main_fips_ori_agency.drop_duplicates(['FIPS_STATE', 'FIPS_PLACE']) # --> 11,602 rows

    """
    2. Rename CGOVTYPE, FIPS_STATE, FIPS_PLACE to Govt_level, 'STATEFP', 'place_fips' to match national census file
    """
    final_main_fips_ori_agency_unique = final_main_fips_ori_agency_unique.rename(
        {'CGOVTYPE': 'Govt_level', 'FIPS_STATE': 'STATEFP', 'FIPS_PLACE': 'place_fips'}, axis='columns')

    """
    3. Get only those records from 90 final main file whose cgovtype is 1,2 or 3
    """
    final_main_fips_ori_agency_unique = final_main_fips_ori_agency_unique.loc[
        final_main_fips_ori_agency_unique['Govt_level'].isin([1, 2, 3])]

    return final_main_fips_ori_agency_unique


def get_glevel_ori_agency(county_cens_file, final_main_df, filename, city_cens_file=False):

    """
    ***
        Merge CGOVTYPE, ORI, AGENCY from final main file into census files based on state and place fips.
    ***
    """

    """
    1. Append cities census file to counties census file
    """
    national_census_df = pd.read_csv(county_cens_file)
    national_census_df.sort_values(by=['STATEFP', 'CNTY'], inplace=True)
    if city_cens_file:
        cities_df = pd.read_csv(city_cens_file)
        cities_df.sort_values(by=['STATEFP', 'CNTY'], inplace=True)
        national_census_df = national_census_df.append([cities_df])

    """
    2.
    Merge national all census files with 1990 final main file to get the correct cgovtype based on fips state, fips place. 
    Also to obtain ORI and Agency columns from final main file.
    Inner join coz we want only those agencies that are present in both the files so that we can analyze agencies that have data consistently over time    
    """

    national_census_df = national_census_df.merge(final_main_df, on=['STATEFP', 'place_fips'])

    """
    3. In National_Census_2000, create final Govt_level = Govt_level_y column and get rid of _x and _y columns 
    """
    national_census_df['Govt_level'] = national_census_df['Govt_level_y']
    national_census_df.drop(['Govt_level_x', 'Govt_level_y'], axis=1, inplace=True)

    """
    4. Rearrange columns so that ORI, AGENCY, Govt_level are at the beginning
    """
    cols = list(national_census_df.columns.values)
    cols.pop(cols.index('ORI'))
    cols.pop(cols.index('AGENCY'))
    cols.pop(cols.index('Govt_level'))

    national_census_df = national_census_df[['ORI', 'AGENCY', 'Govt_level'] + cols]

    # print(f'{filename} rows: ', national_census_df.shape[0])

    national_census_df.to_csv(f'/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/{filename}.csv', index=False)



def merge_cen_final_main():
    # Get the required df from 90 final main file
    final_main_cgovtype_ori_agency_df = get_final_main_cgovtype_ori_agency('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/Final_Main_Var_1990_2001.csv')

    # Create the national census 2000 file
    counties_00_file = '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/census_county_2000/new_census_variables/new_vars_census_county_2000.csv'
    cities_00_file = '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/census_cities_2000/new_census_variables/new_vars_census_cities_2000.csv'
    get_glevel_ori_agency(county_cens_file = counties_00_file, city_cens_file = cities_00_file, final_main_df = final_main_cgovtype_ori_agency_df, filename = 'National_Census_2000_fm_merge')


    # Create the national census 2010 file
    counties_10_file = '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/census_county_2010/new_census_variables/new_vars_census_county_2010.csv'
    cities_10_file = '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/census_cities_2010/new_census_variables/new_vars_census_cities_2010.csv'
    get_glevel_ori_agency(county_cens_file = counties_10_file, city_cens_file = cities_10_file, final_main_df = final_main_cgovtype_ori_agency_df, filename = 'National_Census_2010_fm_merge')


    """
        # Clean up 1990 census file
        # sort by state(smallest to largest) then cnty(smallest to largest) then pop(largest to smallest)
        # drop the duplicates based on state and place fips
    """
    national_cens_90_df = pd.read_excel('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_1990_All_Initial.xlsx')
    national_cens_90_df_unique = national_cens_90_df.drop_duplicates(['STATEFP', 'place_fips'])

    # add YEAR column with 1990 value at 5th position
    national_cens_90_df_unique.insert(5, 'YEAR', 1990)

    # Rename Hispan columns to Hispanic
    national_cens_90_df_unique.rename({'Hispan_allcount': 'Hispanic_count', 'Hispan_Males_All': 'Hispanic_Males_All', 'Age1524_HispanM': 'Age1524_HispanicM', 'Age1524_HispanF': 'Age1524_HispanicF', 'Hispan_Females_All': 'Hispanic_Females_All'}, inplace=True)

    # drop 'other' columns
    national_cens_90_df_unique.drop(['Other_count', 'Other_Males_All', 'Age1524_OtherM', 'Age1524_OtherF', 'Other_Females_All', 'Hispan_allcount', 'Hispan_Males_All', 'Age1524_HispanM', 'Age1524_HispanF', 'Hispan_Females_All'], inplace=True, axis=1)

    national_cens_90_df_unique.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_1990_unique.csv', index=False)

    # Create the final 1990 census file by merging with 90 final main file
    get_glevel_ori_agency(county_cens_file = '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_1990_unique.csv', final_main_df = final_main_cgovtype_ori_agency_df, filename = 'National_Census_1990_fm_merge')


def merge_three_cen_files():
    nat_cen_90 = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_1990_fm_merge.csv')
    nat_cen_90_codes = nat_cen_90[['ORI', 'STATEFP', 'place_fips']]

    nat_cen_00 = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_2000_fm_merge.csv')
    nat_cen_00_codes = nat_cen_00[['ORI', 'STATEFP', 'place_fips']]

    nat_cen_10 = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_2010_fm_merge.csv')
    nat_cen_10_codes = nat_cen_10[['ORI', 'STATEFP', 'place_fips']]

    nat_cen_10_merged = nat_cen_10.merge(nat_cen_00_codes, on='ORI').merge(nat_cen_90_codes, on='ORI')
    clean_nat_cen_file(nat_cen_10_merged, 'National_Census_2010_All')

    nat_cen_00_merged = nat_cen_00.merge(nat_cen_10_codes, on='ORI').merge(nat_cen_90_codes, on='ORI')
    clean_nat_cen_file(nat_cen_00_merged, 'National_Census_2000_All')

    nat_cen_90_merged = nat_cen_90.merge(nat_cen_00_codes, on='ORI').merge(nat_cen_10_codes, on='ORI')
    clean_nat_cen_file(nat_cen_90_merged, 'National_Census_1990_All')


def clean_nat_cen_file(nat_cen_df, fl_name):
    # print(f'{fl_name} rows: ', nat_cen_df.shape[0])
    # drop _x and _y columns from merge
    nat_cen_df.drop(['place_fips_x','place_fips_y','STATEFP_x', 'STATEFP_y'], axis=1, inplace=True)

    # MOVE STATEFP and place_fips to to 4th and 1st position respectively
    # ORI, AGENCY, placename(2), Govt_level, place_fips(4), STATEFP(5), CNTY
    cols = list(nat_cen_df)
    cols.insert(2, cols.pop(cols.index('placename')))
    cols.insert(4, cols.pop(cols.index('place_fips')))
    cols.insert(5, cols.pop(cols.index('STATEFP')))

    # re-order df with the new column order
    nat_cen_df = nat_cen_df.loc[:, cols]

    nat_cen_df.to_csv(f'/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/{fl_name}.csv', index=False)


def create_nat_cen_all_file():

    """

    :return:
    """

    """
    Merge the census files with final main file to get correct govt level values
    """
    merge_cen_final_main()


    """
    Perform 3 way merge on the census files to have uniform ORIs and st+place fips throughout
    """
    merge_three_cen_files()


    nat_cen_90_all_df = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_1990_All.csv')
    nat_cen_00_all_df = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_2000_All.csv')
    nat_cen_10_all_df = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_2010_All.csv')

    nat_cen_all = nat_cen_10_all_df.append([nat_cen_00_all_df, nat_cen_90_all_df], sort=False)

    print(nat_cen_all.shape[0])

    nat_cen_all.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_All.csv', index=False)


create_nat_cen_all_file()