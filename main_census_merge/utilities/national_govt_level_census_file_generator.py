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

    """
        Checking for city census file coz we need to first append city census file to the bottom of county census file for 2000 and 2010.
        And city census file is passed only for 2000 and 2010 since for 1990 city and county census data is already together.
    """
    if city_cens_file:
        cities_df = pd.read_csv(city_cens_file)
        national_census_df = national_census_df.append([cities_df])


    """
    2.
    Merge national all census files with 1990 final main file to get the correct cgovtype based on fips state, fips place. 
    Also obtain ORI and Agency columns from final main file.
    Inner join coz we want only those agencies that are present in both the files so that we can analyze agencies that have data consistently over time    
    """
    national_census_df = national_census_df.merge(final_main_df, on=['STATEFP', 'place_fips'])


    """
    3. Create final Govt_level = Govt_level_y column which has govt_level values from final main file and get rid of _x and _y columns 
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

    # write the final df with updated govt_level, ori, agency etc. to a csv
    national_census_df.to_csv(f'/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/{filename}.csv', index=False)


def merge_cen_final_main():

    # Get the required df with 'cgovtype', 'ori', 'agency', fips place and fips state from 90 final main file
    final_main_cgovtype_ori_agency_df = get_final_main_cgovtype_ori_agency('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/Final_Main_Var_1990_2001.csv')

    # Create the final national census 2000 file by merging combining 2000 cities and counties.
    counties_00_file = '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/census_county_2000/new_census_variables/new_vars_census_county_2000.csv'
    cities_00_file = '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/census_cities_2000/new_census_variables/new_vars_census_cities_2000.csv'
    get_glevel_ori_agency(county_cens_file = counties_00_file, city_cens_file = cities_00_file, final_main_df = final_main_cgovtype_ori_agency_df, filename = 'National_Census_2000_fm_merge')


    # Create the final national census 2010 file by merging combining 2010 cities and counties.
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
    national_cens_90_df_unique.rename({'Hispan_allcount': 'Hispanic_count', 'Hispan_Males_All': 'Hispanic_Males_All', 'Age1524_HispanM': 'Age1524_HispanicM', 'Age1524_HispanF': 'Age1524_HispanicF', 'Hispan_Females_All': 'Hispanic_Females_All'}, inplace=True, axis=1)

    # drop 'other' columns
    national_cens_90_df_unique.drop(['Other_count', 'Other_Males_All', 'Age1524_OtherM', 'Age1524_OtherF', 'Other_Females_All'], inplace=True, axis=1)

    national_cens_90_df_unique.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_1990_unique.csv', index=False)

    # Create the final 1990 census file by merging with 90 final main file
    get_glevel_ori_agency(county_cens_file = '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_1990_unique.csv', final_main_df = final_main_cgovtype_ori_agency_df, filename = 'National_Census_1990_fm_merge')


def merge_three_cen_files():
    nat_cen_90 = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_1990_fm_merge.csv')

    nat_cen_00 = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_2000_fm_merge.csv')

    nat_cen_10 = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_2010_fm_merge.csv')

    nat_cen_90_ORIs = set(nat_cen_90['ORI'])
    nat_cen_00_ORIs = set(nat_cen_00['ORI'])
    nat_cen_10_ORIs = set(nat_cen_10['ORI'])

    nat_cen_common_ORIs = list(nat_cen_90_ORIs.intersection(nat_cen_00_ORIs).intersection(nat_cen_10_ORIs))

    nat_cen_common_ORIs_df = pd.DataFrame(nat_cen_common_ORIs, columns=['ORI'])

    nat_cen_10_merged = nat_cen_10.merge(nat_cen_common_ORIs_df, on='ORI')
    nat_cen_10_merged.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_2010_All.csv', index=False)

    nat_cen_00_merged = nat_cen_00.merge(nat_cen_common_ORIs_df, on='ORI')
    nat_cen_00_merged.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_2000_All.csv', index=False)

    nat_cen_90_merged = nat_cen_90.merge(nat_cen_common_ORIs_df, on='ORI')
    nat_cen_90_merged.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_1990_All.csv', index=False)


def create_nat_cen_all_file():

    """
    Merge each of the final 90, 00 and 10 the census files with final main file to get correct govt level values
    """
    merge_cen_final_main()


    """
    Perform 3 way merge on the census files to have uniform ORIs and st+place fips throughout
    """
    merge_three_cen_files()


    # Finally, read all the years' census files to append together and form a consolidated census file with updated govt level, ORI from the 1990 final main file
    nat_cen_90_all_df = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_1990_All.csv')
    nat_cen_00_all_df = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_2000_All.csv')
    nat_cen_10_all_df = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_2010_All.csv')

    # Append all the census files together
    nat_cen_all = nat_cen_10_all_df.append([nat_cen_00_all_df, nat_cen_90_all_df], sort=False)

    nat_cen_all.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_All.csv', index=False)


"""
    To create the final census file by updating govt levels from main file
"""
create_nat_cen_all_file()