import os
import json
import pygame
from tkinter import filedialog as fd, messagebox as mb
from tkinter import ttk
import io

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

USER_JSON_PATH = "users.json"
current_user = {"name": None}


# Globale Verwaltung der Buttons und Auswahl

# def login_user(username, password):
#     # if not os.path.exists(USER_JSON_PATH):
#     #     mb.showerror("Fehler", "Benutzerdaten nicht gefunden.")
#     #     return False

#     # user = db.get_users(username)
#     if 'id' in user and user['password'] == password:
#         current_user["name"] = user['username']
#         current_user["id"] = user['id']
#     else:
#         mb.showerror("Login fehlgeschlagen", "Falscher Benutzername oder Passwort.")







def rearrange_buttons(frame):
    columns_per_row = 4
    for index, (_, button) in enumerate(sound_buttons):
        row = index // columns_per_row
        col = index % columns_per_row
        button.grid(row=row, column=col, padx=5, pady=5, sticky='ew')
        frame.grid_columnconfigure(col, weight=1)
