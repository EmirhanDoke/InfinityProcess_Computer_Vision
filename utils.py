# Copyright 2025 Said Emirhan Döke
# Licensed under the Apache License, Version 2.0

import json
import os
import sys

class Utils:
    
    settings_file = "user_settings.txt"
    
    def __init__(self):
        pass

    @classmethod
    def load_user_settings(cls, setting_name):

        path = Utils.resource_path(Utils.settings_file)

        # Ayarları dosyadan yükle
        if os.path.exists(path):
            with open(path, "r") as file:
                settings = json.load(file)

                return settings[setting_name]
            
    @classmethod
    def resource_path(cls, relative_path):
        try:
            base_path = sys._MEIPASS  # pyinstaller'ın geçici klasörü
        except Exception:
            base_path = os.path.abspath(".")  # normal çalışma
        return os.path.join(base_path, relative_path)