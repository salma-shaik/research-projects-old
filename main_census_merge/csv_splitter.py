import pandas as pd


def split_csv(filepath, census_type=None):
    """
        Using encoding = "ISO-8859-1" (or latin1) to handle the below UnicodeDecodeError

        UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1 in position 2:
            invalid continuation byte

        skiprows = 1 --> to skip the 1st row (GEO.id etc.)
    """
    initial_csv_df = pd.read_csv(filepath, skiprows=1)

    if census_type=='county':
        # index=False --> to avoid python/pandas from creating a default index in the csv
        county_df = initial_csv_df.head(3143)
        county_df.to_csv('data/census_county_2010/DEC_10_SF1_P12_with_ann_county.csv', encoding='utf-8', index=False)

        county_urban_df = initial_csv_df.iloc[3143:6286]
        county_urban_df.to_csv('data/census_county_2010/DEC_10_SF1_P12_with_ann_county_urban.csv', encoding='utf-8', index=False)

        county_rural_df = initial_csv_df.iloc[6286:]
        county_rural_df.to_csv('data/census_county_2010/DEC_10_SF1_P12_with_ann_county_rural.csv', encoding='utf-8', index=False)
    else:
        city_df = initial_csv_df.head(29261)
        city_df.to_csv('data/census_cities_2010/DEC_10_SF1_P12_with_ann_city.csv', encoding='utf-8', index=False)

        city_urban_df = initial_csv_df.iloc[29261:58522]
        city_urban_df.to_csv('data/census_cities_2010/DEC_10_SF1_P12_with_ann_city_urban.csv', encoding='utf-8', index=False)

        city_rural_df = initial_csv_df.iloc[58522:]
        city_rural_df.to_csv('data/census_cities_2010/DEC_10_SF1_P12_with_ann_city_rural.csv', encoding='utf-8', index=False)

    # Abanda CDP, Alabama -- Urban - 29264
    # Abanda CDP, Alabama -- Rural - 58525

# Splitting 2010 county census file into total, urban and rural respectively
# split_csv('data/census_county_2010/DEC_10_SF1_P12_with_ann.csv')

# Splitting 2010 city census file into total, urban and rural respectively
split_csv('data/census_cities_2010/DEC_10_SF1_P12_with_ann.csv')
