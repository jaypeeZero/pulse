from components import room
from helpers import io

from models.Room import Room

def render(sender):
    """Render the lobby"""
    content()

def content() -> None:
    """Display the contents of the lobby"""
    room_names = io.get_rooms(io.get_data_directory())
    for r in room_names:
        room.content(Room(r))