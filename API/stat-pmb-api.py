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
import matplotlib as mpl
import matplotlib.cm as cm
import math
import scipy.stats as stats

os.chdir("F:\\Kuliah\\Semester 7\\Prosi 2\\Data")
app = Flask(__name__)

def createRGBAinteger(color_map,value):
#    rgba = color_map.to_rgba(value)
    rgba = color_map(value)
    return (math.ceil(255*rgba[0]),math.ceil(255*rgba[1]),math.ceil(255*rgba[2]),1)

@app.route('/pmdk/all/province')
def getAllProvinceParticipant():
    df_res = pd.read_csv(".\\PMDK\\Result\\pmdk_all_province_participants.csv",index_col=0)
    result = df_res.to_json(orient="index")
    return result

@app.route('/pmdk/<year>/city_reg')
def getCityRegencyParticipants(year):
    year = str(year)
    #year="2018"
    df_res = pd.read_csv(".\\PMDK\\Result\\"+year+"\\pmdk_"+year+"_school_city-reg_participants.csv",index_col=0)
#    df_res['total_normalized'] = (normalize([np.array(df_res.total)]))[0] #
#    df_res['total_normalized'] = np.log(df_res.total) #log
#    df_res['total_normalized'] = np.clip(df_res.total.values,a_min=0,a_max=300) #clip
    df_res['total_normalized'] = stats.zscore(df_res.total) #z-score
#    norm = mpl.colors.Normalize(vmin=0, vmax=max(df_res['total']))
    cmap = cm.Reds
#    m = cm.ScalarMappable(norm=norm, cmap=cmap)
#    df_res['color'] = df_res['total_normalized'].apply(lambda x: createRGBAinteger(m,x))
    df_res['color'] = df_res['total_normalized'].apply(lambda x: createRGBAinteger(cmap,x))
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
        df = pd.read_csv('.\\PMDK\\Result\\trends\\pmdk_allYear_trend.csv',index_col=0)
        return df.to_json(orient='index')
    else:
        return None

@app.route('/school_list/<jalur>/<year>/<city>', methods=['GET'])
def getSchoolList(jalur,year,city):
    try:
        df = pd.read_csv(".\\..\\Result\\school_list\\"+jalur+"\\"+year+"\\"+city+".csv")
        return jsonify({"data": (df.to_dict('records'))}), 200
    except:
        return jsonify({"msg":"Error happened"}), 400
    
if __name__ == "__main__":
    app.run()