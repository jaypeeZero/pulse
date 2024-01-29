from nicegui import ui

FILE_NOT_FOUND = 'File not found'

def display_error(message):
    print(message)
    ui.notification(message)