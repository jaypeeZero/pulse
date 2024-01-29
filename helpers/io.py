import json
import os
from helpers import events
from helpers import errors

from pydispatch import dispatcher

def get_rooms(path):
    for _, dirs, _ in os.walk(path):
        return set(dirs)

def get_people_in_room(path):
    for _, _, files in os.walk(path):
        return set(files) - {"room.json"}

def get_json_file(filename):
    with open(filename) as file:
        return json.load(file)

def write_json_file(filename, content):
    with open(filename, 'w') as file:
        json.dump(content, file)
    
def delete_json_file(folder, filename):
    file_path = os.path.join(folder, filename)
    print(f'File path to delete is {file_path}')

    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        dispatcher.send( signal=events.GENERAL_ERROR, message=f'{errors.FILE_NOT_FOUND} when attempting to delete {filename} from {folder}' )