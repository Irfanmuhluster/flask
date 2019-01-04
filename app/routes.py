import socket
import json
import random
import datetime
import requests
import urllib

# from datetime import datetime
from flask import abort, make_response, request, session, flash
from flask import render_template, redirect, url_for, escape, jsonify, Response
from app import app

# app.debug = True
# app.config['DEBUG'] = True

# ini tipenya masih string
tfmt = '%Y-%m-%dT%H:%M:%S.%fZ'


@app.route('/')
def welcome():
    # jika session username terdaftar maka ke index.html
    return "Ini halaman utama webserver"


@app.route('/coba')
def coba():
    ''' mendapatkan json dari link '''
    # baca json
    #url = "http://192.168.1.126:8086/query?q=select+last(neto)+from+jcamp.autogen.lve"
    #response = urllib.urlopen(url)
    #data = json.loads(response.read())
    #data2 = json.dumps(data['results'][0]['series'][0])
    #tittle = json.dumps(data['results'][0]['series'][0]['name'])
    # data3 = data['results'][0]['series'][0]['values']
    # data3.headers['Access-Control-Allow-Origin'] = '*'
    retDate = datetime.datetime.now().strftime(tfmt)
    retVal = random.randint(1, 1000)
    d2dict = {}
    d2dict['values'] = [[retDate, retVal]]
    data2 = json.dumps(d2dict)
    resp = Response(data2, status=200, mimetype='application/json')
    # resp.headers
    # return jsonify(data3)
    return resp


@app.route('/coba2')
def coba2():
    ''' mendapatkan json dari link '''
    # baca json
    url = "http://192.168.1.126:8086/query?q=select+neto+from+jcamp.autogen.lve+order+by+time+desc+limit+10"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    data2 = json.dumps(data['results'][0]['series'][0])
    # data3 = data['results'][0]['series'][0]['values']
    # data3.headers['Access-Control-Allow-Origin'] = '*'
    resp = Response(data2, status=200, mimetype='application/json')
    # resp.headers
    # return jsonify(data3)
    return resp
