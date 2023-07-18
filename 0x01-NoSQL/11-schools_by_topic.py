#!/usr/bin/env python3
'''Printing a list of schools to learn python'''
import pymongo


def schools_by_topic(mongo_collection, topic):
    '''A function which return a list of schools'''
    return mongo_collection.find({"topics: {"$in":[topics]}})
