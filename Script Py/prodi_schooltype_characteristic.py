# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 11:21:57 2020

@author: William Walah
@desc: script untuk melihat karakteristik tipe sekolah pendaftar pmdk
"""

import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

#read necessary data
os.chdir("D:\\Kuliah\\Semester 7\\Prosi 2\\Data")
df_pmdk = pd.read_excel("PMDK\\03_Data_Peminat_PMDK_2013_2018.xlsx")
df_pmdk['V_KET_STATUS_SEKOLAH'] = df_pmdk['V_KET_STATUS_SEKOLAH'].apply(lambda x: (x).title() if isinstance(x, str) else x)
#df_pmdk['V_KET_STATUS_SEKOLAH'] = df_pmdk['V_KET_STATUS_SEKOLAH'].apply(lambda x:  x[0:6] if isinstance(x, str) and 'Swasta' in x else x)
df_pmdk['V_KET_STATUS_SEKOLAH'].isna().sum()
prodi_dict = {110:'Ekonomi Pembangunan',
              120:'Manajemen',
              130:'Akuntansi',
              200:'Ilmu Hukum',
              310:'Ilmu Administrasi Publik',
              320:'Ilmu Administrasi Bisnis',
              330:'Ilmu Hubungan Internasional',
              410:'Teknik Sipil',
              420:'Aristektur',
              510:'Ilmu Filsafat',
              610:'Teknik Industri',
              620:'Teknik Kimia',
              630:'Teknik Elektro',
              710:'Matematika',
              720:'Fisika',
              730:'Teknik Informatika',
              910:'D3 Manajemen Perusahaan'
              }

df_pmdk_ts = df_pmdk[df_pmdk.V_KODE_PROGRAM_STUDI_PILIHAN == 420]
df_pmdk_hi = df_pmdk[df_pmdk.V_KODE_PROGRAM_STUDI_PILIHAN == 330]

####test plot
df_pmdk_ts = df_pmdk_ts[df_pmdk_ts.V_TAHUN == 2017]
df_pmdk_hi = df_pmdk_hi[df_pmdk_hi.V_TAHUN == 2017]

df_pmdk_ts_res = df_pmdk_ts.groupby('V_KET_STATUS_SEKOLAH').count()['F_STATUS']
df_pmdk_hi_res = df_pmdk_hi.groupby('V_KET_STATUS_SEKOLAH').count()['F_STATUS']


####
sd_yearly = []
for year in df_pmdk.V_TAHUN.unique():
    df_yearly = df_pmdk[df_pmdk.V_TAHUN == year]
    df_major_characteristic = pd.DataFrame()
    for prodi in df_yearly.V_KODE_PROGRAM_STUDI_PILIHAN.unique():
        df_filtered = df_yearly[df_yearly.V_KODE_PROGRAM_STUDI_PILIHAN == prodi]
        df_res = df_filtered.groupby('V_KET_STATUS_SEKOLAH').count()['F_STATUS']
        #df_res = df_res.reindex(['NEGERI','SWASTA/SWASTA KATOLIK'])
        if len(df_res) > 0:
            df_res.name = prodi 
            df_major_characteristic = df_major_characteristic.append(df_res)
    df_major_characteristic.fillna(0,inplace=True)
    sd_yearly.append(df_major_characteristic)
    
    
df_pmdk_2017 = sd_yearly[4]

import numpy as np

std_negeri = np.std(df_pmdk_2017['Negeri'])  
std_swasta = np.std(df_pmdk_2017['Swasta Katolik'])  

patch_1 = mpatches.Patch(color='#969696', label='SD (Negeri): {:.2f}'.format(round(std_negeri,2)))
patch_2 = mpatches.Patch(color='#969696', label='SD (Swasta): {:.2f}'.format(round(std_swasta,2)))
plt.figure(figsize=(12,8))
plt.text(0.95,df_pmdk_ts_res.values[0]+1,df_pmdk_ts_res.values[0],fontsize=14)
plt.text(2.9,df_pmdk_ts_res.values[1]+1,df_pmdk_ts_res.values[1],fontsize=14)
plt.text(1.4,df_pmdk_hi_res.values[0]+1,df_pmdk_hi_res.values[0],fontsize=14)
plt.text(3.4,df_pmdk_hi_res.values[1]+1,df_pmdk_hi_res.values[1],fontsize=14)
plt.bar(np.arange(1,4,2),df_pmdk_ts_res.values,width=0.5,color='#eb403440')
plt.bar([1.5,3.5],df_pmdk_hi_res.values,width=0.5,color='#34b7eb40')
plt.xlim(0,5)
plt.xticks([1.25,3.25],df_pmdk_ts_res.index.values,fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Kategori Sekolah',fontsize=16)
plt.ylabel('Total Peserta',fontsize=16)
plt.title('Perbandingan Total Partisipan asal Sekolah Negeri & Sekolah Swasta \n Jalur PMDK Tahun 2017',fontsize=16)
plt.legend(handles=[patch_1,patch_2],fontsize=12)
plt.show()