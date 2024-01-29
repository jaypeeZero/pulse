from components import lobby
from helpers import commands
from helpers import events
from helpers import errors
from helpers import settings
from pydispatch import dispatcher
from nicegui import ui

# Set up connections for handling events
dispatcher.connect( lobby.render, signal=commands.RENDER_LOBBY, sender=dispatcher.Any )
dispatcher.connect( lobby.re_render_rooms, signal=events.USER_JOINED_LOCATION, sender=dispatcher.Any )
dispatcher.connect( lobby.re_render_rooms, signal=events.USER_LEFT_LOCATION, sender=dispatcher.Any )
dispatcher.connect( errors.display_error, signal=events.GENERAL_ERROR, sender=dispatcher.Any )

def __init__():
    settings.unset_my_location() # User isn't in a room on app startup
    dispatcher.send(signal=commands.RENDER_LOBBY)

def transition_person_to_location(location):
    """Move a person into a room. A side effect of this is making them leave their current room if they are in one."""
    my_location = settings.get_my_location()

    if (my_location != "" and my_location is not None):
        settings.unset_my_location()

    settings.set_my_location(location)