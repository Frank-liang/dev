#coding:utf-8
from flask import request
from . import app,jsonrpc
from auth import auth_login
import json ,traceback
import utils
#权限的增删改查

@jsonrpc.method('power.create')

@auth_login
def create(auth_info,**kwargs):
    username = auth_info["username"]
    if '1' not in auth_info['r_id']:
        return json.dumps({'code':1,'errmsg':'you not admin,no power'})
    try:
        data = request.get_json()['params']
        #if not utils.check_name(data['name']):
        #    return json.dumps({'code':1, 'errmsg':'name must be string or num'})
        app.config['db'].execute_insert_sql('power',data) 
        utils.write_log('api').info('create power %s success' % username)
        return json.dumps({'code':0,'result':'create %s success ' % data['name']})
    except:
        utils.write_log('api').error('create power error :%s' % traceback.format_exc())
        return json.dumps({'code':1,'errmsg':'create power failed'})

@jsonrpc.method('power.delete')
@auth_login
def delete(auth_info,**kwargs):
    username = auth_info['username']
    if '1' not in auth_info['r_id']:
        return json.dumps({'code':1,'errmsg':'you not admin, no power'})
    try:
        data = request.get_json()['params']
        where = data.get('where',None)
        if not where:
            return json.dumps({'code':1,'errmag':'must need a condition'})
        result = app.config['db'].get_one_result('power',['name'],where) 
        if not result:
            return json.dumps({'code':1,'errmag':'data not exits'})
        app.config['db'].execute_delete_sql('power', where) 
        utils.write_log('api').info('%s delete power success' %username)
        return json.dumps({'code':0,'result':'delete power success'})
    except:
        utils.write_log('api').error('delete power error:%s' %traceback.format_exc())
        return json.dumps({'code':1,'errmsg':'delete power failed'})
