import pandas as pd

# Removing Byrne, LLEB, WEED, GOT_COPS, HIRING_TOT2, HIRING_RAT columns which won't be used.

main_file = pd.read_excel('data/Final_Main_1990_2001.xlsx', encoding = "ISO-8859-1")

main_file_df = pd.DataFrame(main_file)

main_file_req_df = main_file_df.drop(['BYRNE_DISCRET_580', 'LLEBG_592', 'WEED_AND_SEED_595', 'GOT_COPS', 'HIRING_TOT2', 'HIRING_RATE'], axis=1)

main_file_req_df.to_csv('data/Final_Main_Var_1990_2001.csv', encoding='utf-8', index=False)

main_file_req_csv_df = pd.read_csv('data/Final_Main_Var_1990_2001.csv')
# print(main_file_req_csv_df.head())