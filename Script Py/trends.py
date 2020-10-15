# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 14:58:08 2020

@author: William Walah
@desc: script untuk membuat visualisasi untuk melihat trend 
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

import pickle
import os
os.chdir("D:\\Kuliah\\Semester 7\\Prosi 2\\Data")
with open('dict_province_code_name.pickle', 'rb') as handle:
    dict_provinceCode = pickle.load(handle)
    
with open('dict_city_code_name_125.pickle', 'rb') as handle:
    dict_cityCode_1 = pickle.load(handle)
    
with open('dict_city_code_name_200.pickle', 'rb') as handle:
    dict_cityCode_2 = pickle.load(handle)
    
df_pmdk = pd.read_excel(".\\PMDK\\03_Data_Peminat_PMDK_2013_2018.xlsx")

#trend of total participant, each year
df_allyear_trend = pd.DataFrame(df_pmdk.groupby('V_TAHUN').count()['V_NUSM'])
df_allyear_trend.columns = ['TOTAL']
df_allyear_trend.to_csv('.\\PMDK\\Result\\pmdk_allYear_trend.csv',index=True)
plt.figure(figsize=(12,8))
plt.plot(df_allyear_trend.index.values,df_allyear_trend.TOTAL.values,lw=2)
plt.plot(df_allyear_trend.index.values,df_allyear_trend.TOTAL.values,'bo')
plt.ylim(min(df_allyear_trend.TOTAL.values)-500,max(df_allyear_trend.TOTAL.values)+500)
plt.title('Trend Peserta PMDK setiap Tahun',fontsize=18)
plt.xlabel('Tahun',fontsize=16)
plt.ylabel('Total Peserta',fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

"""
Multitrend untuk provinsi
"""
#trend of total participant each year based by province
df_pmdk['PROPINSI_SEKOLAH'] = df_pmdk['PROPINSI_SEKOLAH'].apply(lambda x: x[6:len(x)] if isinstance(x, str) and 'Prop.' in x else x)
df_pmdk['PROPINSI_SEKOLAH'] = df_pmdk['PROPINSI_SEKOLAH'].apply(lambda x: x.title()if isinstance(x, str) else x)
dict_temp = {'D.K.I. Jakarta': 'Jakarta Raya', 'Jakarta': 'Jakarta Raya', 'D.I. Yogyakarta':'Yogyakarta', 'Bangka Belitung':'Kepulauan Bangka Belitung'}
df_pmdk['PROPINSI_SEKOLAH'] = df_pmdk['PROPINSI_SEKOLAH'].apply(lambda x: dict_temp.get(x,x))
df_pmdk['PROPINSI_SEKOLAH'] = df_pmdk['PROPINSI_SEKOLAH'].apply(lambda x: np.nan if x in ['[Prop] Amerika','[Prop] Kiribati','[Prop] Qatar','[Prop] Thailand','[Prop] Timor-Leste'] else x)
df_pmdk = df_pmdk[df_pmdk['PROPINSI_SEKOLAH'].notnull()] #pra olah selesai

#@Panji Pengstu: Skip loop dibawah ini
for province in df_pmdk['PROPINSI_SEKOLAH'].unique():
    df_filter=df_pmdk[df_pmdk['PROPINSI_SEKOLAH'] == province]
    if(len(df_filter.V_TAHUN.unique())>3 and max(df_filter.V_TAHUN) > 5):
        df_filter = pd.DataFrame(df_filter.groupby('V_TAHUN').count()['V_NUSM'])
        #len(df_filter[df_filter.V_TAHUN == 2013])
        df_filter.columns = ['TOTAL']
        print(df_filter.transpose())
        pad_bot = min(df_filter.TOTAL.values)-max(df_filter.TOTAL.values)
        pad_top = max(df_filter.TOTAL.values)+max(df_filter.TOTAL.values)
        plt.figure(figsize=(12,8))
        plt.plot(df_filter.index.values,df_filter.TOTAL.values,lw=2)
        plt.plot(df_filter.index.values,df_filter.TOTAL.values,'bo')
        for x in df_filter.index.values:
            plt.text(x,df_filter.loc[x].TOTAL+max(df_filter.TOTAL.values)*0.1,df_filter.loc[x].TOTAL)
        plt.ylim(pad_bot,pad_top)
        plt.title('Trend Peserta PMDK setiap Tahun di provinsi '+province,fontsize=18)
        plt.xlabel('Tahun',fontsize=16)
        plt.ylabel('Total Peserta',fontsize=16)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.show()

#multitrend
df_jakarta = df_pmdk[df_pmdk['PROPINSI_SEKOLAH'] == 'Jakarta Raya']
df_jabar = df_pmdk[df_pmdk['PROPINSI_SEKOLAH'] == 'Jawa Barat']
df_jakarta = pd.DataFrame(df_jakarta.groupby('V_TAHUN').count()['V_NUSM'])
df_jabar = pd.DataFrame(df_jabar.groupby('V_TAHUN').count()['V_NUSM'])
df_jakarta.columns = ['TOTAL']
df_jabar.columns = ['TOTAL']
plt.figure(figsize=(12,8))
plt.plot(df_jabar.index.values,df_jabar.TOTAL.values,lw=2, label='Jawa Barat')
plt.plot(df_jabar.index.values,df_jabar.TOTAL.values,'bo')
for x in df_jabar.index.values:
    plt.text(x,df_jabar.loc[x].TOTAL+max(df_jabar.TOTAL.values)*0.05,df_jabar.loc[x].TOTAL)
plt.plot(df_jakarta.index.values,df_jakarta.TOTAL.values,lw=2, label='DKI Jakarta')
plt.plot(df_jakarta.index.values,df_jakarta.TOTAL.values,color='orange',marker='o')
for x in df_jakarta.index.values:
    plt.text(x,df_jakarta.loc[x].TOTAL+max(df_jakarta.TOTAL.values)*0.1,df_jakarta.loc[x].TOTAL)
plt.ylim(200,1800)
plt.title('Trend Peserta PMDK setiap Tahun di provinsi DKI Jakarta & Jawa Barat',fontsize=18)
plt.xlabel('Tahun',fontsize=16)
plt.ylabel('Total Peserta',fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=14,markerscale=1.5)
plt.show()
"""
Akhir trend provinsi
"""


#trend of total participant each year based by city (2018 data only)        
#cant do a trend chart, because pmdk city's data only exist in year 2018
        

"""
Untuk multi trend sekolah
"""
#trend of total participant each year based by school
df_school = df_pmdk[df_pmdk['V_NAMA_SMTA'].notna()] #filter row yang value nama smta tidak NaN
#bikin dataframe kosong buat nampung rekord dengan kriteria
#row: untuk suatu sekolah, ada kolom tahunnya yang nandain total peserta ditiap tahunnya
df_test = pd.DataFrame(columns=['2013','2014','2015','2016','2017','2018']) 
for school in df_school.V_NAMA_SMTA.unique():
    df_filter = df_school[df_school.V_NAMA_SMTA == school]
    df_filter = df_filter.groupby('V_TAHUN').count()['V_NUSM']
    df_filter.columns = ['TOTAL']
    val = []
    yr = 2013
    while(yr<=2018):
        if yr in df_filter.index.values:
            val.append(df_filter[yr])
        else:
            val.append(0)
        yr = yr + 1
    df_test.loc[school] = val
    
    
#@PANJI PANGESTU: Abaikan sampe komentar berikut
#school_dict_prob = {} #iseng ngecek ratio kemiripan
#count = 1
#for school in df_test.index.unique():
#    print(count)
#    val = []
#    for school_b in df_test.index.unique():
#        val.append(similar(school,school_b))
#    school_dict_prob[school] = val
#    count = count + 1
#Akhir dari abaikan kode    

"""
Dari sini, val,yr ,val_2,yr_2 itu memuat informasi [array tahun] dan [array total peserta]
untuk sekolah A (val,yr) dan sekolah B(val_2,yr_2. Nanti dipakai di pyplot dibawah
"""
val = []
yr = []
count_year = 2013
for x in df_test.loc['SMU TRINITAS']:
    if(x>0):
        val.append(x)
        yr.append(count_year)
    count_year = count_year + 1
    
val_2 = []
yr_2 = []
count_year = 2013
for x in df_test.loc['SMA KRISTEN 1 BPK PENABUR']:
    if(x>0):
        val_2.append(x)
        yr_2.append(count_year)
    count_year = count_year + 1
    
#multi trend
plt.figure(figsize=(12,8))
plt.plot(yr,val,lw=2,label='SMU TRINITAS')
plt.plot(yr,val,'bo')
plt.plot(yr_2,val_2,lw=2,label='SMA KRISTEN 1\nBPK PENABUR')
plt.plot(yr_2,val_2,color='orange',marker='o')
#plt.ylim(min(val)-10,max(val)+10)
idx = 0
for x in yr:
    plt.text(x,val[idx]+2,val[idx])
    plt.text(x,val_2[idx]+2,val_2[idx])
    idx = idx + 1
plt.title('Trend Peserta PMDK setiap Tahun di SMU TRINITAS & \n SMA KRISTEN 1 BPK PENABUR',fontsize=18)
plt.xlabel('Tahun',fontsize=16)
plt.ylabel('Total Peserta',fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend()
plt.show()





