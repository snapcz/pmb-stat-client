# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 11:20:25 2020

@author: William Walah
@desc: script untuk membuat barchart ranking total partisipan jalur PMDK untuk kota-kota dari suatu provinsi
"""

"""
1. Load data
"""
import os
import pandas as pd

os.chdir("D:\\Kuliah\\Semester 7\\Prosi 2\\Data")
df_pmdk = pd.read_excel(".\\PMDK\\03_Data_Peminat_PMDK_2013_2018.xlsx")

"""
2. Membenarkan dahulu penamaan provinsi menggunakan dictionary
"""
import pickle
with open('dict_province_code_name.pickle', 'rb') as handle:
    dict_province_codename = pickle.load(handle) 

"""
2.1. buat kolom baru yang menyimpan nama provinsi dari dictionary. Sebenarnya bisa duplikat dari nama provinsi saja
"""
import numpy as np
df_pmdk["Nama_Provinsi_Cleaned"] = df_pmdk["KODE_PROPINSI_SEKOLAH"].apply(lambda x: dict_province_codename.get(x,np.nan)) 

"""
2.2 cleaning: membuat format nama provinsi menjadi 'Jawa Barat' (Title), dan menghilangkan rekord dengan provinsi diluar indonesia
"""
#2.2.1 buat agar nilai kolom nama provinsi cleaned jadi seperti judul (huruf kapital didepan, sisanya huruf kecil pake .title())
df_pmdk["Nama_Provinsi_Cleaned"] = df_pmdk["Nama_Provinsi_Cleaned"].apply(lambda x: x.title() if isinstance(x,str) else x) 
#penjelasan: apply adalah sebuah fungsi untuk mengaplikasikan sebuah proses ke nilai-nilai kolom nama provinsi cleaned. selalu
#            notasinya pakai apply(lambda x) -> x adalah nilai kolom Nama_Provinsi_Cleaned.
#penjelasan: isinstance untuk mengecek apakah x bertipe str. Digunakan agar x.title() tidak error karena fungsi title hanya ada untuk string

#2.2.2 Drop rekord dengan nilai-nilai provinsi diluar Indonesia, kalau run df_pmdk["Nama_Provinsi_Cleaned"].unique() pasti 
#ada yang namanya: [Prop.] Amerika -> tidak perlu ini
#langkah: pertama pakai fungsi apply untuk mendapatkan row mana yang sesuai dengan kriteria:
#         x dari kolom Nama_Provinsi_Cleaned yang tipe "String" dan tidak ada string [Prop]. Hasilnya array_of_boolean
#langkah: kedua, filter row yang sesuai dengan hasil filtrasi diatas pakai df_pmdk[array_of_boolean]
#langkah: ketiga, pilih kolom dari hasil yang difilter, kolom Nama_Provinsi_Cleaned kembali, dari df_pmdk yang telah diambil
df_pmdk["Nama_Provinsi_Cleaned"] = df_pmdk[df_pmdk["Nama_Provinsi_Cleaned"].apply(lambda x: isinstance(x,str) and not('[Prop]' in x))]["Nama_Provinsi_Cleaned"]
#                                          'dari batas sini, hingga akhir, ini langkah pertama                                       '
#                                  'dari batas sini, hingga akhir, ini langkah kedua                                                 '
#                                                                                                                                    'langkah ketiga          '

#cek lagi pakai df_pmdk["Nama_Provinsi_Cleaned"].unique() bila masih ada nama provinsi luar indonesia atau NaN
print(df_pmdk["Nama_Provinsi_Cleaned"].unique())

#2.2.3 Ganti nilai-nilai nama provinsi agar seragam, e.g. ada Jakarta dengan D.K.I Jakarta, diubah jadi satu nilai
dict_temp = {
        'Jakarta': 'D.K.I. Jakarta', 
        'Yogyakarta':'D.I. Yogyakarta', 
        'Bangka Belitung':'Kepulauan Bangka Belitung'
        }
df_pmdk["Nama_Provinsi_Cleaned"] = df_pmdk["Nama_Provinsi_Cleaned"].apply(lambda x: dict_temp.get(x,x))
#df_pmdk.to_excel
#print(df_pmdk["Nama_Provinsi_Cleaned"].unique()) untuk cek apakah sudah benar atau tidak
#tahap 2 selesai

"""
3. Filter: Provinsi - Jawa Barat, Tahun 2017
"""
df_filter = df_pmdk[(df_pmdk.V_TAHUN == 2017).values & (df_pmdk.Nama_Provinsi_Cleaned == 'Jawa Barat').values]


"""
4. Agregasi gorupby berdasarkan nama sma, dan count jumlah peserta, sort ascending
"""
df_aggr = df_filter.groupby('V_NAMA_SMTA').count()['V_TAHUN'] #groupby kode smu, ambil
df_aggr.columns = ['TOTAL']
df_aggr = df_aggr.sort_values(ascending=True)


"""
5. Buat Bar Chart
"""
df_res = df_aggr[len(df_aggr)-5:len(df_aggr)]
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

plt.figure(figsize=(12,8))
plt.barh(np.arange(0,5),df_res.values)
plt.yticks(np.arange(0,5),df_res.index.values,fontsize=14)
plt.xlabel('Total Partisipan',fontsize=16)
plt.xticks(fontsize=14)
plt.title('Daftar Total Partisipan Setiap Sekolah Jalur PMDK di Jawa Barat tahun 2017',fontsize=16)
plt.show()

#or, versi lebih bagus (OPTIONAL)

plt.figure(figsize=(12,8))
plt.barh(np.arange(0,5),df_res.values,color=['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple'])
plt.xlabel('Total Partisipan',fontsize=16)
plt.xticks(fontsize=14)
plt.title('Daftar Total Partisipan Setiap Sekolah Jalur PMDK di Jawa Barat tahun 2017',fontsize=16)
plt.yticks([],[])
arr_patches = []
dict_color = {
        0: 'tab:blue', 
        1: 'tab:orange', 
        2: 'tab:green', 
        3: 'tab:red', 
        4:'tab:purple',
        }
for x in np.arange(0,5):
    arr_patches.append(mpatches.Patch(color=dict_color.get(x,'b'), label=df_res.index.values[x]))
plt.legend(handles=arr_patches)
# agar legendnya diluar kanan atas box
# plt.legend(handles=arr_patches,fontsize=14,bbox_to_anchor=(1, 1), loc=2)
plt.show()