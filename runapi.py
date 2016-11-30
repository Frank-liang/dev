#!/usr/bin/env python
#coding:utf-8

from api import app
import utils
import db
#导入自定义的各种配置参数，最终参数以字典形式返回
config = utils.get_config('api')

#将自定义的配置文件全部加载到全局的配置文件(app.config),可以在任意地方调用
app.config.update(config)
app.config['db'] = db.Cursor(config)
print app.config

#print app.config


if __name__ == "__main__":
    app.run(host=app.config['bind'],port=int(app.config['port']),debug=False)
