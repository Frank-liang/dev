#!/usr/bin/env python
#coding:utf-8
from flask import Flask,request
from . import app
import utils
import json,time,traceback,hashlib

@app.route('/api/login',methods=['GET'])
def login():
    try:
        username = request.args.get('username',None)
        passwd = request.args.get('passwd',None)
        passwd = hashlib.md5(passwd).hexdigest()
        if not (username and passwd):
            return json.dumps({'code':1,'errmsg':"need username and passwd"})
        result = app.config['db'].get_one_result('user',['id','username','password','r_id','is_lock'],{'username':username})
        if not result:
            return json.dumps({'code':2,'errmsg':'user id not exit'})
        if result['is_lock'] == 1:
            return json.dumps({'code':3,'errmsg':'user is locked'})
        if passwd == result['password']:
            data = {'last_login': time.strftime('%Y-%m-%d %H:%M:%S')}
            app.config['db'].execute_update_sql('user',data,{'username': username})
            token = utils.get_validate(result['username'],result['id'],result['r_id'],app.config['password_key'])
            utils.write_log('api').info("%s login success" % username)
            return json.dumps({'code':0,'authorization': token})
        else:
            return json.dumps({'code':5,'errmsg':"passwd is wrong"})
    except:
        utils.write_log('api').error("login error: %s" % traceback.format_exc())
        return json.dumps({'code':6,'errmsg':"login fail"})
