# -*- coding=utf-8 -*-
# @TIME     : 2019/6/25 16:01
# @Author   : ziooooo
# @File     : ziojson.py


class JsonObjError(Exception):
    def __init__(self):
        self.args = ['json obj error']


IGNORE_PROPERTY_NAMES = []


def filter_unusable_type(value):
    return type(value).__name__ == 'type' or type(value).__name__ == 'function' or type(value).__name__ == 'method'


def filter_property(name):
    condition1 = 1 - name.startswith('__')  # 过滤系统属性
    condition2 = 1 - (name in IGNORE_PROPERTY_NAMES)  # 过滤需要忽略的属性
    return condition1 and condition2


def make_json_obj(value):
    if filter_unusable_type(value):
        try:
            raise JsonObjError
        except JsonObjError as e:
            print('Error: %s\nType: %s\nValue: %s' % (e, type(value).__name__, value))
    elif isinstance(value, (str, int, float, bool)) or value == None:
        return value
    elif isinstance(value, (tuple, set, list)):
        value = list(value)
        res = []
        for item in value:
            res.append(make_json_obj(item))
        return res
    elif isinstance(value, dict):
        res = {}
        for item in value.keys():
            if not isinstance(item, str):
                continue
            res[item] = make_json_obj(value[item])
        return res
    else:  # 处理自定义类的实例
        pnames = list(filter(filter_property, dir(value)))
        res = {}
        for item in pnames:
            obj = getattr(value, item)
            if 1 - filter_unusable_type(obj):
                res[item] = make_json_obj(obj)
        return res


import json


def make_json_str(value):
    return json.dumps(make_json_obj(value))
