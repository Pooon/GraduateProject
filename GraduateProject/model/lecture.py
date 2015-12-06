# -*- coding: utf-8 -*-

class Lecture(object):

	TABLE_NAME = 'lecture'

    class Field(object):
        _id = '_id'
        title = 'title'
        text = 'text'
        price = 'price'
        lectureType = 'lectureType'
        imageId = 'imageId'
        videoId = 'videoId'

    class ContentType(object):
        text = 0
        picture = 1
        video = 2
