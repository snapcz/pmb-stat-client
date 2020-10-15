# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 13:14:07 2020

@author: William Walah
@desc: script to generate in certain 'year' and certain 'province', list of school and its participants
"""

import os
import pandas as pd
import numpy as np
import pickle
import math
import json

os.chdir("D:\\Kuliah\\Semester 7\\Prosi 2")

#1. read data
df_pmdk = pd.read_excel(".\\Data\\PMDK\\03_Data_Peminat_PMDK_2013_2018.xlsx")
df_pmdk_status = pd.read_excel(".\\Data\\PMDK\\04_Data_Status_Peminat_PMDK_2013_2018.xlsx")

#INTERMEZO, data cleaning on df_pmdk_status
#case: terdapat row dengan nilai tahun,gelombang,dan no pdmk yang serupa namun nilai no_reg,no_npm berbeda
#dalam kasus ini dilihat dengan cara:
df_dupli = df_pmdk_status[df_pmdk_status.duplicated(subset=['V_TAHUN','V_GELOMBANG','V_NO_PMDK'],keep=False)]
#len(df_dupli) = 90, ada 45 row duplikat pada nilai kolom V_TAHUN,V_GELOMBANG,V_NO_PMDK
#setelah ditelusuri, rekord pertama dari rekord duplikat memiliki nilai lebih komplit, maka akan dilakukan proses
#untuk menyimpan rekord duplikat pertama saja
df_pmdk_status = df_pmdk_status[~df_pmdk_status.duplicated(subset=['V_TAHUN','V_GELOMBANG','V_NO_PMDK'],keep='first')]
df_pmdk_status.to_excel(".\\Data\\PMDK\\04_Data_Status_Peminat_PMDK_2013_2018_REM_DUPLICATE.xlsx")

#2. load city lat-long data, used in map chart
df_city = pd.read_csv(".\\Data\\ind_city_long-lat_clear.csv")

#3. load pickle data
with open('.\\Data\\dict_city_code_name_125.pickle', 'rb') as handle:
    dict_cityCode_1 = pickle.load(handle)
    
with open('.\\Data\\dict_city_code_name_200.pickle', 'rb') as handle:
    dict_cityCode_2 = pickle.load(handle)
    
#4. slice data, we only need certain column
df_pmdk_sliced = df_pmdk[["V_TAHUN","V_NUSM","V_KODE_SEKOLAH_KOTA","V_NAMA_SMTA"]]
df_pmdk_sliced["NAMA_KOTA"] = df_pmdk_sliced["V_KODE_SEKOLAH_KOTA"].apply(lambda x: (dict_cityCode_1.get(int(x),dict_cityCode_2.get(int(x),int(x)))).title() if not math.isnan(x) else x)


#4.5 create dictionary of school with its location
dict_school_loc = pd.Series(df_pmdk['V_ALAMAT_SMU'].values,index=df_pmdk['V_NAMA_SMTA'].values).to_dict()

#loop through each year, each city
for year in df_pmdk_sliced.V_TAHUN.unique():
    df_yearly = df_pmdk_sliced[df_pmdk_sliced.V_TAHUN==year]
    df_yearly = df_yearly[df_yearly['V_KODE_SEKOLAH_KOTA'].notna()]
    if(len(df_yearly)>0):
        print(year)
        df_merged = df_yearly.merge(df_pmdk_status, how='inner', left_on=['V_TAHUN','V_NUSM'], right_on=['V_TAHUN','V_NO_PMDK'])    
        if(len(df_merged) == len(df_yearly)): #cek apakah data peserta tahunan terdapat di data status
            check_city = len(df_merged.merge(df_city,how='left',left_on='NAMA_KOTA',right_on='name'))
            if(check_city == len(df_merged)): #cek apakah seluruh daftar kota sudah sesuai dengan nama kota yang digunakan di map chart
                for city in df_merged.NAMA_KOTA.unique():
                    df_city_filtered = df_merged[df_merged.NAMA_KOTA == city]
                    df_city_filtered['TOTAL'] = [1] * len(df_city_filtered)
                    df_city_filtered['PASS'] = df_city_filtered['V_NO_REGISTRASI'].apply(lambda x: 1 if not math.isnan(x) else 0)
                    df_city_filtered['ENROLL'] = df_city_filtered['V_NPM'].apply(lambda x: 1 if not math.isnan(x) else 0)
                    df_result = df_city_filtered.groupby('V_NAMA_SMTA').sum()[['TOTAL','PASS','ENROLL']]
                    df_result['LOCATION'] = df_result.index.values
                    df_result['LOCATION'] = df_result['LOCATION'].apply(lambda x: dict_school_loc.get(x,"Data tidak tersedia"))
                    df_result.to_csv(".\\Result\\school_list\\pmdk\\"+str(year)+"\\"+city+".csv")
            else:
                print("Error: Ada nama kota yang tidak terdaftar pada daftar kota yang digunakan pada map chart")
        else:
            print("Error: Ada peserta yang tidak memiliki data status peserta")
    else:
        print("Error: Tidak ada data kota untuk tahun "+str(year))
                

tes = pd.read_csv(".\\..\\Result\\school_list\\pmdk\\2018\\Kota Bandung.csv",index_col=0)
tessssssssssss = tes.to_dict('records')
lel = json.dumps(tessssssssssss)
print(lel)
        
    










