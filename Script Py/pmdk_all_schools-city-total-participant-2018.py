# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:04:55 2020

@author: William Walah
@desc: script untuk membuat peta sebaran peserta pendaftar jalur PMDK diseluruh kota, setiap tahunnya
"""

import os
import pandas as pd
import numpy as np
import pickle

os.chdir("D:\\Kuliah\\Semester 7\\Prosi 2\\Data")
df_pmdk = pd.read_excel(".\\PMDK\\03_Data_Peminat_PMDK_2013_2018.xlsx")
df_city_125 = pd.read_excel("02_Data_Master_Provinsi_Kota_125.xlsx")
df_city_125 = df_city_125[df_city_125['V_KODE_KOTA'].notna()]
df_city_200 = pd.read_excel("02_Data_Master_Provinsi_Kota_200.xlsx")
df_city_200 = df_city_200[df_city_200['V_KODE_KOTA'].notna()]

#create dict of city code and city name
#dict_1 dan dict_2 berasal dari sumber data berbeda, karena sumber data '125' merupakan sumber kode data
#untuk tahun yang lebih lama, dibandingkan sumber data '200'
dict_1 = pd.Series(df_city_125['V_NAMA_KOTA'].values,index=df_city_125['V_KODE_KOTA'].apply(lambda x: int(x) if (x).isdigit() else x)).to_dict()
dict_2 = pd.Series(df_city_200['V_NAMA_KOTA'].values,index=df_city_200['V_KODE_KOTA'].apply(lambda x: int(x) if (x).isdigit() else x)).to_dict()
dict_2[316100] = 'Kota Tanjung Pinang' #sebelumnya Kota Tanjungpinang, diubah agar sesuai dengan data long-lat
with open('dict_city_code_name_125.pickle', 'wb') as handle: #save dict_1 as pickle
    pickle.dump(dict_1, handle, protocol=pickle.HIGHEST_PROTOCOL) 
with open('dict_city_code_name_200.pickle', 'wb') as handle: #save dict_2 as pickle
    pickle.dump(dict_2, handle, protocol=pickle.HIGHEST_PROTOCOL)

#filter row dimana atribut kota tidak bernilai nan
df_pmdk_filtered = df_pmdk[df_pmdk['V_KODE_SEKOLAH_KOTA'].notna()] #cuman ada tahun 2018 doang .- .
df_pmdk_filtered['V_TAHUN'].unique()
df_counted =pd.DataFrame(df_pmdk_filtered.groupby('V_KODE_SEKOLAH_KOTA').count()['V_TAHUN'])
df_counted['NAMA_KOTA'] = df_counted.index.values
df_counted['NAMA_KOTA'] = df_counted['NAMA_KOTA'].apply(lambda x: (dict_1.get(x,dict_2.get(x,x))).title())
df_counted.set_index('NAMA_KOTA',inplace=True)

#read city xlsx
df_city = pd.read_csv("ind_city_long-lat_clear.csv",index_col=0)

#merge counted and city
df_res = df_counted.merge(df_city,how='left',left_index=True, right_index=True)
df_res.loc['Kota Tanjungpinang'] = [2, 0.9179205, 104.446464]
df_res.columns = ['total','latitude','longitude']
df_res.to_csv(".\\PMDK\\Result\\2018\\pmdk_2018_school_city-reg_participants.csv",index=True)