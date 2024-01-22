from models.Person import Person
from components import avatar
from helpers import io
from nicegui import ui

def content(room) -> None:
    people = io.get_people_in_room(f'{io.get_data_directory()}\\{room.name}') 

    with ui.card():
        ui.label(room.name)
        ui.separator()
        for p in people:
            avatar.content(Person(p))