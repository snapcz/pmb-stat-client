# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 00:38:45 2020

@author: William Walah
"""
import os
import pandas as pd
import pickle
import numpy as np

#read necessary data
os.chdir("D:\\Kuliah\\Semester 7\\Prosi 2\\Data")
df_pmdk_participant = pd.read_excel("PMDK\\03_Data_Peminat_PMDK_2013_2018.xlsx")
df_pmdk_participant["KODE_PROPINSI_SEKOLAH"].fillna('N/A',inplace=True)
with open('dict_province_code_name.pickle', 'rb') as handle:
    dict_province_codename = pickle.load(handle)
    
#aggregate to get the result for total participant in PMDK UNPAR 2013-2018, based on their school's province
df_participantTotal_provinceBased = pd.DataFrame(df_pmdk_participant.groupby('KODE_PROPINSI_SEKOLAH').count()["V_TAHUN"])
df_participantTotal_provinceBased.drop('N/A',inplace=True)
df_participantTotal_provinceBased["INDEX"] = df_participantTotal_provinceBased.index.values
df_participantTotal_provinceBased["INDEX"] = df_participantTotal_provinceBased["INDEX"].apply(lambda x: dict_province_codename.get(x,np.nan))
df_participantTotal_provinceBased["INDEX"] = df_participantTotal_provinceBased["INDEX"].apply(lambda x: x.title())
df_participantTotal_provinceBased.dropna(inplace=True)
dict_temp = {'D.K.I Jakarta': 'Jakarta Raya', 'D.I. Yogyakarta':'Yogyakarta', 'Bangka Belitung':'Kepulauan Bangka Belitung'}
df_participantTotal_provinceBased["INDEX"] = df_participantTotal_provinceBased["INDEX"].apply(lambda x: dict_temp.get(x,x))
df_res = df_participantTotal_provinceBased.groupby('INDEX').sum()
#df_res = df_res.rename(index={'D.K.I Jakarta': 'Jakarta Raya', 'D.I. Yogyakarta':'Yogyakarta', 'Bangka Belitung':'Kepulauan Bangka Belitung'})
df_res.drop(['[Prop] Amerika','[Prop] Kiribati','[Prop] Qatar','[Prop] Thailand','[Prop] Timor-Leste'],inplace=True)
df_res.columns=['VALUE']
os.chdir('.\\PMDK\\Result')
df_res.to_csv("pmdk_all_school_province_participants.csv",index=True)