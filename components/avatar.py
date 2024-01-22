from nicegui import ui

def content(person_data) -> None:
    with ui.card():
        ui.label(person_data.name)