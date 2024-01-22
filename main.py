from components import room
from nicegui import ui

room.content()

ui.run(native=True, port=8788)