# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 21:45:10 2020

@author: William Walah
@desc: A RESTful API script, build with flask to do necesity prep & work to process PMB UNPAR data
"""

from flask import Flask, request, jsonify
from flask_jsonpify import jsonpify
import os
import pandas as pd
import json
import pickle
import numpy as np
from sklearn.preprocessing import normalize

os.chdir("D:\\Kuliah\\Semester 7\\Prosi 2\\Data")
app = Flask(__name__)

@app.route('/pmdk/all/province')
def getAllProvinceParticipant():
    df_res = pd.read_csv(".\\PMDK\\Result\\pmdk_all_school_province_participants.csv",index_col=0)
    result = df_res.to_json(orient="index")
    return result

@app.route('/pmdk/<year>/city_reg')
def getCityRegencyParticipants(year):
    year = str(year)
    df_res = pd.read_csv(".\\PMDK\\Result\\"+year+"\\pmdk_"+year+"_school_city-reg_participants.csv",index_col=0)
    result = df_res.to_json(orient="index")
    return result

@app.route('/indonesia_city')
def getIndonesiaCity():
    df_city = pd.read_csv("ind_city_long-lat_clear.csv",index_col=0)
    result = df_city.to_json(orient="index")
    parse_res = json.loads(result)
    json_data = json.dumps(parse_res)
    return json_data

@app.route('/pmdk/trend')
def getTrend():
    if(request.args['tipe'] == 'all'):
        df = pd.read_csv('.\\PMDK\\Result\\pmdk_allYear_trend.csv',index_col=0)
        return df.to_json(orient='index')
    else:
        return None

@app.route('/school_list/<jalur>/<year>/<city>', methods=['GET'])
def getSchoolList(jalur,year,city):
    try:
        df = pd.read_csv(".\\..\\Result\\school_list\\"+jalur+"\\"+year+"\\"+city+".csv")
        i = 0
        while(i<10):
            df = df.append(df.copy())
            i=i+1
        return jsonify({"data": (df.to_dict('records'))}), 200
    except:
        return jsonify({"msg":"Error happened"}), 400
    
@app.route('/test', methods=['GET'])
def test():
    dummy = [{
                    "no": 1,
                    "jenis": "meja",
                    "desc": "meja indah",
                    "tgl_terbit": "2020-08-08T00:00:00Z",
                    "tgl_expire": "2021-08-08T00:00:00Z",
                },
                {
                    "no": 2,
                    "jenis": "meja",
                    "desc": "meja indah",
                    "tgl_terbit": "2020-08-08T00:00:00Z",
                    "tgl_expire": "2021-08-08T00:00:00Z",
                },
                {
                    "no": 3,
                    "jenis": "meja",
                    "desc": "meja indah",
                    "tgl_terbit": "2020-08-08T00:00:00Z",
                    "tgl_expire": "2021-08-08T00:00:00Z",
                },
                {
                    "no": 4,
                    "jenis": "meja",
                    "desc": "meja indah",
                    "tgl_terbit": "2020-08-08T00:00:00Z",
                    "tgl_expire": "2021-08-08T00:00:00Z",
                },
                {
                    "no": 5,
                    "jenis": "meja",
                    "desc": "meja indah",
                    "tgl_terbit": "2020-08-08T00:00:00Z",
                    "tgl_expire": "2021-08-08T00:00:00Z",
                }]
    return jsonify({"data": dummy}), 200
    
if __name__ == "__main__":
    app.run()