# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 20:12:27 2020

@author: William Walah
@desc: 
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.chdir("D:\\Kuliah\\Semester 7\\Prosi 2\\Data")
df_nilai_pmdk_2013_2017 = pd.read_excel(".\\PMDK\\Data_Perolehan_Nilai_PMDK_2013_2017.xlsx")
df_peserta = pd.read_excel(".\\PMDK\\03_Data_Peminat_PMDK_2013_2018.xlsx")
df_merged = df_nilai_pmdk_2013_2017.merge(df_peserta,how='left',left_on=['V_TAHUN','V_NUSM','V_GELOMBANG'],right_on=['V_TAHUN','V_NUSM','V_GELOMBANG'])
df_merged = df_merged[['V_TAHUN','V_NUSM','V_GELOMBANG','V_NAMA_x','V_KODE_PROGRAM_STUDI_PILIHAN_x','V_KODE_SMU','N_NILAI','V_KODE_MATAPEL']]
df_merged.to_csv("test.csv")
temp = df_merged.groupby('V_KODE_SMU').count()
os.chdir("D:\\Kuliah\\Semester 7\\Prosi 2\\Plot\\PMDK\\")
school_dict = pd.Series(df_peserta.V_NAMA_SMTA.values, index=df_peserta.V_KODE_SMU).to_dict()
school_dict.get('00003144')
#school_dict_reverse = pd.Series(df_peserta.V_KODE_SMU.values, index=df_peserta.V_NAMA_SMTA).to_dict()
#school_dict_reverse.get('SMU BPK PENABUR')
map_matapel ={
        1: "Matematika",
        2: "Bahasa Indonesia",
        3: "Bahasa Inggris",
        4: "Fisika",
        5: "Menggambar",
        6: "Kewarganegaraan",
        7: "Kimia",
}
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

def getSpecificBoxPlotPMDK(year,prodi,school):
    df_filtered = df_merged[(df_merged.V_KODE_PROGRAM_STUDI_PILIHAN_x == prodi).values &
                                  (df_merged.V_TAHUN == year).values &
                                  (df_merged.V_KODE_SMU == school).values]
    print(df_filtered)
    matapel_unique = df_filtered.V_KODE_MATAPEL.unique()
    fig,axs = plt.subplots(1,len(matapel_unique),figsize=(14,10))
    fig.subplots_adjust(hspace=0.4, wspace=0.4)
    fig.suptitle('Ringkasan Data Nilai Mata Pelajaran Peserta PMDK Tahun '+str(year)+'\n Prodi Pilihan '+prodi_dict.get(prodi)+' asal '+school_dict.get(school), fontsize=16)
    col = 0
    print(matapel_unique)
    for matapel in matapel_unique:
        df_filtered_matapel = df_filtered[df_filtered.V_KODE_MATAPEL==matapel]
        df_res = pd.DataFrame(df_filtered_matapel.groupby(['V_NUSM','V_NAMA_x'])['N_NILAI'].mean())
        axs[col].boxplot(df_res["N_NILAI"]) 
        #axs[0,0].text(0.65,np.quantile(df_matematika["N_NILAI"],0.5)-2,np.quantile(df_matematika["N_NILAI"],0.5),fontSize=14,c='r')
        axs[col].set_xticklabels([1],{'fontsize':14})
        axs[col].set_ylabel("NILAI",fontSize=14)
        axs[col].set_title(map_matapel.get(matapel),fontSize=14)
        col = col + 1
    #fig.savefig('BoxPlot_PMDK_'+str(year)+'_'+prodi_dict.get(prodi)+'.png')
    plt.show()
    
getSpecificBoxPlotPMDK(2017,120,'00003144')


            
        
        