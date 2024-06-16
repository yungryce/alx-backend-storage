#!/usr/bin/env python3
"""
This module have a utility function that list all document
"""
import pymongo


def list_all(mongo_collection):
    """
    list all collections
    """
    return [doc for doc in mongo_collection.find()]
