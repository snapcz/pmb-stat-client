# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 14:17:57 2020

@author: William Walah
@desc: Eksplorasi data PMDK
"""
import os
import pandas as pd
import numpy as np
import math
import matplotlib.cm as cm
import matplotlib.patches as mpatches
from matplotlib import pyplot as plt
from matplotlib.colors import Normalize
from matplotlib import rcParams, cycler
from sklearn.preprocessing import normalize
from math import ceil
import pickle

plt.style.use('bmh')

"""
I. Data Peserta Peminat PMDK 2013-2018
"""
os.chdir("D:\\Kuliah\\Semester 7\\Prosi 2\\Data\\PMDK")
df_pmdk_participant = pd.read_excel("03_Data_Peminat_PMDK_2013_2018.xlsx")
dict_prodi_color={
            110: '#f0e500',
            120: '#f0e500',
            130: '#f0e500',
            200: '#ab0000',
            310: '#e7e5e5', 
            320: '#e7e5e5',
            330: '#e7e5e5',
            410: '#084394',
            420: '#084394',
            510: '#4f4f4f',
            610: '#a23f00',
            620: '#a23f00',
            630: '#a23f00',
            710: '#1499dc',
            720: '#1499dc',
            730: '#1499dc',
            910: '#e6da00',
    }
prodi_dict = {
        110:'Ekonomi Pembangunan',
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
# Total partisipan kegiatan PMDK UNPAR tahun 2013-2018 disetiap provinsi berdasarkan
# data provinsi sekolah. Sebelumnya diperlukan proses praolah 
# path-praolah: D:/Kuliah/Semester 7/Prosi 2/pra-olah.py

def getAllSchoolProvinceParticipants():
    # Tidak ada visualisasi yang akan diberikan disini, sebab akan dipadukan dengan
    # MapCharts pada website
    with open('dict_province_code_name.pickle', 'rb') as handle:
        dict_province_codename = pickle.load(handle)
    dict_correcting = dict({'D.K.I. Jakarta': 'Jakarta Raya',
                            'Jakarta':'Jakarta Raya', 
                            'D.I. Yogyakarta':'Yogyakarta', 
                            'Bangka Belitung':'Kepulauan Bangka Belitung',
                            'Irian Jaya Barat':'Papua Barat',
                            'Irian Jaya':'Papua'})
    df_participantTotal_provinceBased = pd.DataFrame(df_pmdk_participant.groupby('KODE_PROPINSI_SEKOLAH').count()["V_TAHUN"])
    df_participantTotal_provinceBased["INDEX"] = df_participantTotal_provinceBased.index.values
    df_participantTotal_provinceBased["INDEX"] = df_participantTotal_provinceBased["INDEX"].apply(lambda x: dict_province_codename.get(x,np.nan))
    df_participantTotal_provinceBased["INDEX"] = df_participantTotal_provinceBased["INDEX"].apply(lambda x: dict_correcting.get(x.title(),x.title()))
    df_participantTotal_provinceBased.dropna(inplace=True)
    df_res = df_participantTotal_provinceBased.groupby('INDEX').sum()
    df_res.columns = ['VALUE']
    df_res.drop(['[Prop] Amerika','[Prop] Kiribati','[Prop] Qatar','[Prop] Thailand','[Prop] Timor-Leste'],inplace=True)
    value_scaled = normalize(df_res.VALUE.values[:,np.newaxis], axis=0).ravel()
    df_res['NORMALIZED'] = value_scaled
    return df_res

def participantTrendsAllYear():
    # Trends partisipan peserta PMDK tahun 2013-2018
    df_trends = pd.DataFrame(df_pmdk_participant.groupby('V_TAHUN').count()['V_NUSM'])
    df_trends.index.names = ['TAHUN']
    df_trends.rename(columns={'V_NUSM':'TOTAL'},inplace=True)
    # uncommend to view visualization
#    fig,ax = plt.subplots(figsize=(15,10))
#    ax.set_facecolor('#ccbba7')
#    bar = plt.bar(df_trends.index.values,df_trends.TOTAL.values,width=0.5,color='#eb5534')
#    plotLines = plt.plot(df_trends.index.values,df_trends.TOTAL.values,color='black',linewidth=5)
#    for rect in bar:
#        height = rect.get_height()
#        x = rect.get_x()+rect.get_width()/2.0-0.15
#        plt.text(x, height+10, '%d' % int(height),color='black',fontsize=16,ha='center', va='bottom')
#    plt.xlabel('Tahun',fontsize=18)
#    plt.ylabel('Total Peserta',fontsize=18)
#    plt.title('Trend Total Partisipan peserta PMDK 2013-2018',fontsize=20)
#    plt.show()
    return df_trends

def participantProdiBased(year):
    df_year = df_pmdk_participant[df_pmdk_participant['V_TAHUN']==year]
    df_year = df_year[df_year['V_KODE_PROGRAM_STUDI_PILIHAN'].notna()]
    df_res = pd.DataFrame(df_year.groupby('V_KODE_PROGRAM_STUDI_PILIHAN').count()['V_TAHUN'])
    df_res.index.names = ['PRODI']
    df_res.rename(columns={'V_TAHUN':'TOTAL'},inplace=True)
    color_rule = []
    prodi = []
    patches = []
    for i in df_res.index.values:
        color_rule.append(dict_prodi_color.get(i,'#cacaca'))
        prodi.append(str(i)+": "+prodi_dict.get(i))
        patches.append(mpatches.Patch(color=dict_prodi_color.get(i,'#cacaca'),label=str(i)+": "+prodi_dict.get(i)))
    y_pos = np.arange(len(df_res))
    fig,ax = plt.subplots(figsize=(12,8))
    ax.set_facecolor('#38664c')
    bar = plt.bar(y_pos,df_res.TOTAL.values,width=0.7,color=color_rule)
    for rect in bar:
        height = rect.get_height()
        x = rect.get_x()+(rect.get_width()/2.0)
        plt.text(x, height+5, '%d' % int(height),color='white',fontsize=16,ha='center', va='bottom')
    plt.xticks(y_pos,df_res.index.values,fontsize=14)
    bottom,top = plt.ylim()
    plt.ylim(top=top+50)
    plt.xlabel("Kode Program Studi",fontsize=16)
    plt.ylabel("Total Peserta",fontsize=16)
    plt.title("Jumlah Peserta PMDK disetiap Program Studi tahun 2018",fontsize=16)
    legends = plt.legend(handles=patches,bbox_to_anchor=(1.5,1),title="Program Studi",fontsize=14,title_fontsize=16)
    print(legends)
    plt.show()
    return df_res;
    
