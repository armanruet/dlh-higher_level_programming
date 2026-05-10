#!/usr/bin/python3
"""Converting CSV Data to JSON Format"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts a CSV file to JSON format and writes to data.json"""
    try:
        with open(csv_filename, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)  # converts each row into a dictionary

        with open("data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
