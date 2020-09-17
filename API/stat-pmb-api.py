# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 21:45:10 2020

@author: William Walah
@desc: A RESTful API script, build with flask to do necesity prep & work to process PMB UNPAR data
"""

from flask import Flask
from flask_jsonpify import jsonpify
import os
import pandas as pd
import json
import pickle
import numpy as np
from sklearn.preprocessing import normalize

os.chdir("D:\\Kuliah\\Semester 7\\Prosi 2\\Data")
os.getcwd()
df_perolehan_pmdk = pd.read_excel("PMDK\\Data_Perolehan_Nilai_PMDK_2013_2017.xlsx") #taking too long time to load lol
df_pmdk_participant = pd.read_excel("PMDK\\03_Data_Peminat_PMDK_2013_2018.xlsx")
with open('dict_province_code_name.pickle', 'rb') as handle:
    dict_province_codename = pickle.load(handle)
app = Flask(__name__)
dict_correcting = dict({'D.K.I. Jakarta': 'Jakarta Raya',
                                  'Jakarta':'Jakarta Raya', 
                                  'D.I. Yogyakarta':'Yogyakarta', 
                                  'Bangka Belitung':'Kepulauan Bangka Belitung',
                                  'Irian Jaya Barat':'Papua Barat',
                                  'Irian Jaya':'Papua'})

@app.route('/test')
def hello_world():
    df_perolehan_pmdk.fillna({'F_STATUS_DITERIMA_FINAL':-1},inplace=True)
    res = df_perolehan_pmdk.groupby(by="F_STATUS_DITERIMA_FINAL").count()[["V_TAHUN"]]
    result = res.values.tolist()
    JSON_data = jsonpify(result)
    return JSON_data

@app.route('/pmdk/all')
def getAllProvinceParticipant():
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
    result = df_res.to_json(orient="index")
    parsed = json.loads(result)
    #result = (df_res['V_TAHUN'].to_dict())
    JSON_data = json.dumps(parsed)
    return JSON_data
    