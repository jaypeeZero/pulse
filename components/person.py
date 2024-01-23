from nicegui import ui

def content(person_data) -> None:
    """Display the contents of a person"""
    with ui.card():
        ui.label(person_data.name)