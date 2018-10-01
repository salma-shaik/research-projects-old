import pandas as pd

# Removing Byrne, LLEB, WEED, GOT_COPS, HIRING_TOT2, HIRING_RATE columns which won't be used.

main_file = pd.read_excel('data/Final_Main_1990_2001.xlsx', encoding = "ISO-8859-1")

main_file_df = pd.DataFrame(main_file)
print(main_file_df.dtypes)

"""
ORI                   object
AGENCY                object
YEAR                   int64
ORICOUNT               int64
FIPS_STATE             int64
FIPS_COUNTY            int64
POP                  float64
GROUP                 object
CGOVTYPE               int64
PER_CAPITA_INCOME    float64
EMPLOYMENT           float64
STCO_FIPS              int64
PROP_MALE            float64
PROP_AGE1524         float64
PROP_NONWHITE        float64
COUNTYPOP              int64
EMPLOYMENT_RATE      float64
VIOLENT_SUM            int64
VIOLENT_RATE         float64
PROPERTY_RATE        float64
MURDER_RATE          float64
MANSLAUGHTER_RATE    float64
RAPE_RATE            float64
ROBBERY_RATE         float64
BURGLARY_RATE        float64
LARCENY_RATE         float64
VEHICLE_RATE         float64
AGG_ASSAULT_RATE     float64
FIPS_PLACE             int64
ALLCOUNTY              int64
SIZECAT                int64
OFFICERS             float64
OFFICER_RATE         float64
TOT_ALL              float64
TOT_FELONIES         float64
TOT_NONUCR           float64
PROP_MISD            float64
MISD_PER_OFC         float64
MISD_Arrests         float64
MISD_Rate            float64
DRUG_Rate            float64
SQRTPOP              float64
NONWHITE             float64
AGE_1524             float64
BYRNE_DISCRET_580     object
LLEBG_592             object
WEED_AND_SEED_595     object
GOT_COPS             float64
HIRING_TOT2          float64
HIRING_RATE          float64
dtype: object
"""

main_file_req_df = main_file_df.drop(['BYRNE_DISCRET_580', 'LLEBG_592', 'WEED_AND_SEED_595', 'GOT_COPS', 'HIRING_TOT2', 'HIRING_RATE'], axis=1)

main_file_req_df.to_csv('data/Final_Main_Var_1990_2001.csv', encoding='utf-8', index=False)

main_file_req_csv_df = pd.read_csv('data/Final_Main_Var_1990_2001.csv')

# print(main_file_req_csv_df.dtypes)
# print(main_file_req_csv_df.head())
"""
ORI                   object
AGENCY                object
YEAR                   int64
ORICOUNT               int64
FIPS_STATE             int64
FIPS_COUNTY            int64
POP                  float64
GROUP                 object
CGOVTYPE               int64
PER_CAPITA_INCOME    float64
EMPLOYMENT           float64
STCO_FIPS              int64
PROP_MALE            float64
PROP_AGE1524         float64
PROP_NONWHITE        float64
COUNTYPOP              int64
EMPLOYMENT_RATE      float64
VIOLENT_SUM            int64
VIOLENT_RATE         float64
PROPERTY_RATE        float64
MURDER_RATE          float64
MANSLAUGHTER_RATE    float64
RAPE_RATE            float64
ROBBERY_RATE         float64
BURGLARY_RATE        float64
LARCENY_RATE         float64
VEHICLE_RATE         float64
AGG_ASSAULT_RATE     float64
FIPS_PLACE             int64
ALLCOUNTY              int64
SIZECAT                int64
OFFICERS             float64
OFFICER_RATE         float64
TOT_ALL              float64
TOT_FELONIES         float64
TOT_NONUCR           float64
PROP_MISD            float64
MISD_PER_OFC         float64
MISD_Arrests         float64
MISD_Rate            float64
DRUG_Rate            float64
SQRTPOP              float64
NONWHITE             float64
AGE_1524             float64
dtype: object

"""