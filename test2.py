# -*- coding=utf-8 -*-
# @TIME     : 2019/6/26 16:47
# @Author   : ziooooo
# @File     : test2.py

from ziojson import make_json_str
from ziojson import IGNORE_PROPERTY_NAMES


class User():
    def __init__(self, name, age, gender, friends, pet):
        self.name = name
        self.age = age
        self.gender = gender
        self.friends = friends
        self.pet = pet

    def say_hellow(self):
        print('hello,i m', self.name)


class Pet():
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':

    user = User(name='Tom', age=15, gender='man', friends=['Jerry', 'Rose'], pet=Pet('Dog'))
    user.id = 1
    user.other = {'job': 'Programmer', 'hobby': 'guitar'}

    print('\n----- single obj -----\n')
    print(make_json_str(user))
    print('\n----- obj list -----\n')
    print(make_json_str([user, user, user]))
