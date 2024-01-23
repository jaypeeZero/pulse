from components import lobby
from helpers import commands
from helpers import events
from helpers import settings
from pydispatch import dispatcher
from nicegui import ui

# TODO : When app first loads, user shouldn't be in any room. Clear any settings on exit and enter?

# Set up connections
dispatcher.connect( lobby.render, signal=commands.RENDER_LOBBY, sender=dispatcher.Any )
dispatcher.connect( settings.set_my_location, signal=events.USER_JOINED_ROOM, sender=dispatcher.Any )

def render_lobby():
    """Show everything"""
    dispatcher.send( signal=commands.RENDER_LOBBY )

def join_person_to_room(room):
    """Move a person into a room. A side effect of this is making them leave their current room if they are in one."""
    my_location = settings.get_my_location()
    if (my_location != "" and my_location is not None):
        make_person_leave_room(settings.get_my_location())

    dispatcher.send( signal=events.USER_JOINED_ROOM, location=room)

def make_person_leave_room(room):
    """Make a person leave a room.  Used as a side effect of joining a room."""
    dispatcher.send( signal=events.USER_LEFT_ROOM, location=room)