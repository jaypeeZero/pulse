from models.Person import Person
from components import person
from helpers import io
from helpers import overseer
from helpers import settings
from nicegui import ui

def content(room) -> None:
    """Display the contents of a room"""
    people = io.get_people_in_room(f'{settings.get_data_folder()}\\{room.name}') 

    with ui.card():
        ui.label(room.name)

        if (room.name != settings.get_my_location()):
            ui.button('Join 💬', on_click=lambda: overseer.transition_person_to_location(room.name))

        ui.separator()
        for p in people:
            person.content(Person(p))