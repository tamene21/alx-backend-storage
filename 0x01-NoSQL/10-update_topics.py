#!/usr/bin/env python3
'''A script to change a name'''
import pymongo


def update_topics(mongo_collection, name, topics):
    '''A function to update a topic'''
    return mongo_collection({
            "name": name
            },
            {
                "$set": {
                    "topics": topics
                    }
                })
