import os

def get_rooms(path):
    for _, dirs, _ in os.walk(path):
        return set(dirs)

def get_people_in_room(path):
    # TODO : This should filter out room.json
    for _, _, files in os.walk(path):
        return set(files) - {"room.json"}

def get_data_directory():
    return "Example_Data_Structure"