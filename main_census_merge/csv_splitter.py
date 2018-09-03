import pandas as pd

def split_csv(filepath, *split_list):
    """
        Using encoding = "ISO-8859-1" (or latin1) to handle the below UnicodeDecodeError

        UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1 in position 2:
            invalid continuation byte

        skiprows = 1 --> to skip the 1st row (GEO.id etc.)
    """
    initial_csv_df = pd.read_csv(filepath, skiprows = 1, encoding = "ISO-8859-1")

    # index=False --> to avoid python/pandas from creating a default index in the csv
    county_df = initial_csv_df.head(3143)
    county_df.to_csv('data/census_county_2010/DEC_10_SF1_P12_with_ann_county.csv', encoding = 'utf-8', index=False)

    county_urban_df = initial_csv_df.iloc[3143:6286]
    county_urban_df.to_csv('data/census_county_2010/DEC_10_SF1_P12_with_ann_county_urban.csv', encoding = 'utf-8', index=False)

    county_rural_df = initial_csv_df.iloc[6286:]
    county_rural_df.to_csv('data/census_county_2010/DEC_10_SF1_P12_with_ann_county_rural.csv', encoding='utf-8', index=False)


split_csv('data/census_county_2010/DEC_10_SF1_P12_with_ann.csv')

# urban_county_list = ['Autauga County, Alabama -- Urban', 'Big Horn County, Wyoming -- Rural']
#
# urban_county_ex = 'Autauga County, Alabama -- Urban'
# pattern = re.compile(r'.+(Urban, Rural)')
#
# matches = filter(pattern.search, urban_county_list)
#
# print(matches)

# for m in matches:
#     print(m)

