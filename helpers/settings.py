from pydispatch import dispatcher

from helpers import io
from helpers import events

SETTINGS_FILE = 'settings.json'
SETTINGS_NAME = 'name'
SETTINGS_ID = 'unique_identifier'
SETTINGS_CURRENT_LOCATION = 'current_location'
SETTINGS_DATA_FOLDER = 'data_folder'

_settings_loaded = False
_current_settings = {}

def get_settings():
    """Get all the settings."""
    global _settings_loaded

    _settings_loaded = True
    return io.get_json_file(SETTINGS_FILE)

def ensure_settings_loaded():
    """Load the settings into memory if they aren't already."""
    global _settings_loaded, _current_settings

    if (not _settings_loaded):
        _current_settings = get_settings()
        _settings_loaded = True

        if (_current_settings[SETTINGS_ID] == "" or _current_settings[SETTINGS_ID] == None):
            dispatcher.send( events.GENERAL_ERROR, message="Cannot find a unique id in your settings.json" )

def save_settings(data):
    """Write the provided settings to file, overwriting the entire settings file that exists."""
    global _settings_loaded

    io.write_json_file(SETTINGS_FILE, data)
    _settings_loaded = False

def unset_my_location():
    global _current_settings
    ensure_settings_loaded()
    # TODO : find my .json file in that room and remove it
    old_location = get_my_location()

    if (old_location != "" and old_location != None):
        print(f'Deleting json file for me from {old_location}')
        io.delete_json_file(f'{get_data_folder()}\\{old_location}', f'{get_my_id()}.json')

    _set_property_by_name(SETTINGS_CURRENT_LOCATION, None)

#####################################
# Property Specific Code
#####################################

def _get_property_by_name(prop_name):
    global _current_settings
    ensure_settings_loaded()
    return _current_settings[prop_name]

def _set_property_by_name(prop_name, value):
    global _current_settings
    ensure_settings_loaded()
    _current_settings[prop_name] = value
    save_settings(_current_settings)

def get_my_location():
    return _get_property_by_name(SETTINGS_CURRENT_LOCATION)

def get_data_folder():
    return _get_property_by_name(SETTINGS_DATA_FOLDER)

def get_my_name():
    return _get_property_by_name(SETTINGS_NAME)

def get_my_id():
    return _get_property_by_name(SETTINGS_ID)

def set_my_location(location):
    my_id = get_my_id()

    io.write_json_file(f'{get_data_folder()}\\{location}\\{my_id}.json', {
        "name": get_my_name()
    })
    _set_property_by_name(SETTINGS_CURRENT_LOCATION, location)
    dispatcher.send( signal=events.USER_JOINED_LOCATION, user_identifier=my_id, location=location )