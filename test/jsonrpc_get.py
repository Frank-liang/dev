#!/usr/bin/env python
#coding:utf-8

from __future__ import unicode_literals
import json
import requests

headers = {'content-type':'application/json'}
url = 'http://127.0.0.1:5001/api'

data = {
    'jsonrpc' : '2.0',
    'method': 'App.users',
    'id': '1',
    'params':{
        'name': 'pc',
        'age': '18'
    }
}

r = requests.post(url, headers=headers,json=data)
print r.status_code
res = json.loads(r.text)
print res
print res['result']
