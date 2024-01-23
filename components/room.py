from models.Person import Person
from components import person
from helpers import io
from helpers import overseer
from nicegui import ui

def content(room) -> None:
    """Display the contents of a room"""
    people = io.get_people_in_room(f'{io.get_data_directory()}\{room.name}') 

    with ui.card():
        ui.label(room.name)
        ui.button('Join 💬', on_click=lambda: overseer.join_person_to_room(room.name))
        ui.separator()
        for p in people:
            person.content(Person(p))