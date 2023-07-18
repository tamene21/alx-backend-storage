#!/usr/bin/env python3
'''Insert a documnet in to a collection'''
import pymongo


def insert_school(mongo_collection, **kwargs):
    '''A function which insert new document'''
    doc = mongo_collection.insert_one(kwargs)
    return doc.id
