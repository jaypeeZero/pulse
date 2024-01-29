from components import room
from helpers import io
from nicegui import ui

from models.Room import Room
from helpers import settings

def render() -> None:
    rooms()

def re_render_rooms() -> None:
    print("Re rendering rooms")
    rooms.refresh()

@ui.refreshable
def rooms() -> None:
    """Display the contents of the lobby"""
    room_names = io.get_rooms(settings.get_data_folder())
    for r in room_names:
        room.content(Room(r))