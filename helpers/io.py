import json
import os

def get_rooms(path):
    for _, dirs, _ in os.walk(path):
        return set(dirs)

def get_people_in_room(path):
    for _, _, files in os.walk(path):
        return set(files) - {"room.json"}

def get_data_directory():
    return "Example_Data_Structure"

def get_json_file(filename):
    with open(filename) as file:
        return json.load(file)

def write_json_file(filename, content):
    with open(filename, 'w') as file:
        json.dump(content, file)