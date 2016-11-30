#!/usr/bin/env python
#coding:utf-8

from api import app
import utils
#导入自定义的各种配置参数，最终参数以字典形式返回
config = utils.get_config('api')

#将自定义的配置文件全部加载到全局的配置文件(app.config),可以在任意地方调用
app.config.update(config)

#print app.config
utils.write_log('web').info("just a test")
utils.write_log('api').error("just a test")


if __name__ == "__main__":
    app.run(host=app.config['bind'],port=int(app.config['port']),debug=True)
