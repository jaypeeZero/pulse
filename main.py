from models.Room import Room
from components import room
from helpers import io
from nicegui import ui

# TODO : Figure out ordering
room_names = io.get_rooms(io.get_data_directory())
for r in room_names:
    room.content(Room(r))

ui.run(native=True, port=8788)