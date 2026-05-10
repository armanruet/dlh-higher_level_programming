#!/usr/bin/python3
"""Serialize and Deserialize"""
import json


def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    filename = json.dumps(data)


def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    return json.loads(filename)
