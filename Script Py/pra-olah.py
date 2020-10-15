# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 23:08:28 2020

@author: William Walah
@desc: script untuk melakukan pra-olah data peserta pemiant pmdk 2013-2018. Praolah ditujukan
    untuk membuat dictionary yang dapat memetakan data kode propinsi dengan nama propinsi yang sesuai
"""

import os
import pickle
import pandas as pd

#read necessary data
os.chdir("D:\\Kuliah\\Semester 7\\Prosi 2\\Data")
df_pmdk_participant = pd.read_excel("PMDK\\03_Data_Peminat_PMDK_2013_2018.xlsx")
df_pmdk_participant["KODE_PROPINSI_SEKOLAH"].fillna('N/A',inplace=True)
df_country_state_1 = pd.read_excel("02_Data_Master_Provinsi_Kota_200.xlsx") 
df_country_state_2 = pd.read_excel("02_Data_Master_Provinsi_Kota_125.xlsx") 

#parse value if isdigit to integer, and remove string 'Prop' in V_NAMA_PROPINSI column
df_country_state_1['V_KODE_PROPINSI'] = df_country_state_1['V_KODE_PROPINSI'].apply(lambda x: int(x) if x.isdigit() else x)
df_country_state_1['V_NAMA_PROPINSI'] = df_country_state_1['V_NAMA_PROPINSI'].apply(lambda x: x[6:len(x)] if "Prop" in x else x)

#creating dictionary to parse province code to province name 
dict_indonesian_province_code_1 = pd.Series(df_country_state_1.V_NAMA_PROPINSI.values,index=df_country_state_1.V_KODE_PROPINSI.values).to_dict()
dict_indonesian_province_code_1['N/A'] = -1
dict_indonesian_province_code_2 = pd.Series(df_country_state_2.V_NAMA_PROPINSI.values,index=df_country_state_2.N_KODE_PROPINSI.values).to_dict()
dict_indonesian_province_code_2.update(dict_indonesian_province_code_1)   
with open('dict_province_code_name.pickle', 'wb') as handle:
    pickle.dump(dict_indonesian_province_code_2, handle, protocol=pickle.HIGHEST_PROTOCOL)
#the preparing process is stopped right here, because we will need the dictionary 

