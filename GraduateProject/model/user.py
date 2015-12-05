# -*- coding: utf-8 -*-

class User(object):

    TABLE_NAME = 'user'

    class Field(object):
        _id = '_id'
        username = 'username'
        pwdhash = 'pwdhash'
        avatarUrl = 'avatarUrl'
        birthDate = 'birthDate'  # optional
        gender = 'gender'
        regisTime = 'regisTime'
        region = 'region'
        signature = 'signature'  # optional