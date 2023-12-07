import json
import os


def loadRequiredExp(app):
    json_url = os.path.join(app.static_folder, 'data/required_exp.json')
    with open(json_url, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def loadWhaleData(app):
    json_url = os.path.join(app.static_folder, 'data/whale_data.json')
    with open(json_url, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data