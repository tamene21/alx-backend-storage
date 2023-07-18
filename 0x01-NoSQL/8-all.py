#!/usr/bin/env python3
'''Python function to list all documents'''


def list_all(mongo_collection):
    '''function to list all doc in a collection'''

    if not mongo_collection:
        return []
    documents = mongo_collection.find()
    return [docs for docs in documents]
