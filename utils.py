#!/bin/env python
#coding:utf-8
import os, os.path
import time, json
import base64
import hashlib
import traceback
import ConfigParser
import logging,logging.config

work_dir = os.path.dirname(os.path.realpath(__file__))

def get_config(section=''):
    config = ConfigParser.ConfigParser()
    service_conf = os.path.join(work_dir,'conf/service.conf')
    config.read(service_conf)
    config_items = dict(config.items('common')) if config.has_section('common') else {}
    print config_items
    if section and config.has_section(section):
        config_items.update(config.items(section))
    return config_items    

def write_log(loggername):
    log_conf = os.path.join(work_dir,'conf/logger.conf')
    logging.config.fileConfig(log_conf)
    logger = logging.getLogger(loggername)
    return logger
