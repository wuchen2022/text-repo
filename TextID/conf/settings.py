# -*- coding: utf-8 -*-
# @Time : 2023/2/12/012 16:27
# @Author : WuChen
# @File : settings.py.py
# @Software : PyCharm
import os
import configparser

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, 'settings.cfg')


def Create():
    if not os.path.exists(CONFIG_PATH):
        config = configparser.ConfigParser()
        # print(type(config))
        config['path'] = {'text_dir': ''}
        config['star_id'] = {'text_id': '', 'command_id': '', 'express_id': ''}
        config['remove'] = {'state': ''}
        config['excel_path'] = {'path': ''}
        with open(CONFIG_PATH, 'w') as f:
            config.write(f)


def ReadExcelPath():
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH, encoding='utf-8-sig')
    path = config.get('excel_path', 'path')
    return path


def ModifyExcelPath(path):
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH, encoding='utf-8-sig')
    config.set('excel_path', 'path', path)
    with open(CONFIG_PATH, 'w', encoding='utf-8-sig') as f:
        config.write(f)


def Read():
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH, encoding='utf-8-sig')
    USER_DATA_DIR = config.get('path', 'text_dir')
    return USER_DATA_DIR


def Modify(path):
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH, encoding='utf-8-sig')
    config.set('path', 'text_dir', path)
    with open(CONFIG_PATH, 'w', encoding='utf-8-sig') as f:
        config.write(f)


def ReadID():
    start_id = {}
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH, encoding='utf-8-sig')
    start_id['text_id'] = config.get('star_id', 'text_id')
    start_id['command_id'] = config.get('star_id', 'command_id')
    start_id['express_id'] = config.get('star_id', 'express_id')
    return start_id


def ModifyID(dic):
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH, encoding='utf-8-sig')
    config.set('star_id', 'text_id', dic.get('text_id'))
    config.set('star_id', 'command_id', dic.get('command_id'))
    config.set('star_id', 'express_id', dic.get('express_id'))
    with open(CONFIG_PATH, 'w', encoding='utf-8-sig') as f:
        config.write(f)


def ReadDuplicateRemoval():
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH, encoding='utf-8-sig')
    state = config.get('remove', 'state')
    return state


def ModifyDuplicateRemoval(state):
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH, encoding='utf-8-sig')
    config.set('remove', 'state', state)
    with open(CONFIG_PATH, 'w', encoding='utf-8-sig') as f:
        config.write(f)
