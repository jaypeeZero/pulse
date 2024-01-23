from helpers import io

SETTINGS_FILE = 'settings.json'
CURRENT_LOCATION = 'current_location'

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
        print(_current_settings)

def save_settings(data):
    """Write the provided settings to file, overwriting the entire settings file that exists."""
    global _settings_loaded

    io.write_json_file(SETTINGS_FILE, data)
    _settings_loaded = False

#####################################
# Property Specific Code
#####################################

def get_my_location():
    global _current_settings

    ensure_settings_loaded()
    return _current_settings[CURRENT_LOCATION]

def set_my_location(location):
    global _current_settings

    ensure_settings_loaded()
    print(f'old location is {_current_settings[CURRENT_LOCATION]}')
    _current_settings[CURRENT_LOCATION] = location
    save_settings(_current_settings)
    print(f'new location is {location}')