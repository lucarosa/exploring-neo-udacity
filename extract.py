"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    haz_dict = {'N': False, 'Y': True}

    neos = []
    with open(neo_csv_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            tmp = {}
            tmp['designation'] = row[3]
            tmp['name'] = row[4] if row[4] else None
            tmp['diameter'] = float(row[15]) if row[15] else None
            tmp['hazardous'] = haz_dict.get(row[7])
            neo = NearEarthObject(**tmp)
            neos.append(neo)

    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    approaches = []
    with open(cad_json_path, 'r') as file:
        data = json.load(file)
        for ca in data['data']:
            tmp = {}
            tmp['designation'] = ca[0]
            tmp['time'] = ca[3]
            tmp['distance'] = float(ca[4])
            tmp['velocity'] = float(ca[7])
            approach = CloseApproach(**tmp)
            approaches.append(approach)
    return approaches
