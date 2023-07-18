#!/usr/bin/env python3
'''print average score'''


def top_students(mongo_collection):
    '''A function which print to scores'''
    students = mongo_collection.aggregate(
            [
                {
                    '$project': {
                        '_id': 1,
                        'name': 1,
                        'averageScore': {
                            '$avg': {
                                '$avg': '$topics.score',
                                },
                            },
                        'topics': 1,
                        }
                    }
                {
                    '$sort': {'averageScore': -1},
                        },
                ]
            )
    return students
