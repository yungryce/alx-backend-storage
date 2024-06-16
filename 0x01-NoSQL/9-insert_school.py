#!/usr/bin/env python3
"""
This module have a utility function that insert documents
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into the school collection.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The MongoDB collection where the document will be inserted.
    **kwargs: Arbitrary keyword arguments representing the fields and values of the document.

    Returns:
    ObjectId: The ID of the newly inserted document.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
