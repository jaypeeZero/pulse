from models.Person import Person
from components import avatar
from nicegui import ui

james = Person(name="James")

def content(room) -> None:
    with ui.card():
        ui.label(room.name)
        ui.separator()
        avatar.content(james)