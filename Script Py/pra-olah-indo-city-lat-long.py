# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 23:40:48 2020

@author: William Walah
@desc: pra-olah indonesia city's latitude & longitude information, Original file found on github
"""

import os
import pandas as pd
import numpy as np

os.chdir("D:/Kuliah/Semester 7/Prosi 2/Data/")
df_city = pd.read_csv("indo_city_province_long_lat.csv")
df_city = df_city.set_index("nid",drop=True)
df_city = df_city[["name","latitude","longitude"]]
df_city = df_city.groupby('name').filter(lambda x: "kota" in (x.name).lower() or ("kabupaten" in (x.name).lower()))
df_city = df_city.drop_duplicates()
df_city['name'] = df_city['name'].apply(lambda x: "Kab. "+(x[9:len(x)]).strip() if "kabupaten" in (x).lower() else x)
df_city.to_csv("ind_city_long-lat_clear.csv",index=False)
