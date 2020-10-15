# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:36:56 2020

@author: William Walah
"""

import os
import pandas as pd
import numpy as np

os.chdir("D:\\Kuliah\\Semester 7\\Prosi 2\\Data")

df_status = pd.read_excel(".\\PMDK\\04_Data_Status_Peminat_PMDK_2013_2018.xlsx")
df_status_filtered = df_status[(pd.isnull(df_status['V_NO_REGISTRASI'])).values & (~pd.isnull(df_status['V_NPM'])).values]
len(df_status_filtered)

df_nilai_18 = pd.read_excel(".\\PMDK\\05_Data_Peserta_PMDK_2018_edit_rapih.xlsx")
len(df_status_filtered.merge(df_nilai_18,left_on='V_NO_PMDK',right_on='NO. PMB'))