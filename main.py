from models.Room import Room
from components import room
from nicegui import ui

# TODO : get a list of rooms and their people
rooms = [Room("Main Room")]

room.content(rooms[0])

ui.run(native=True, port=8788)