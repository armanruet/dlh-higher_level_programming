#!/usr/bin/python3
"""Wring a function that returns the
JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """function for returning object"""
    return json.dumps(my_obj)
