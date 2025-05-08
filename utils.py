import json
import os

class Utils:
    
    settings_file = "user_settings.txt"
    
    def __init__(self):
        pass

    @classmethod
    def load_user_settings(cls, setting_name):

        # Ayarları dosyadan yükle
        if os.path.exists(cls.settings_file):
            with open(cls.settings_file, "r") as file:
                settings = json.load(file)

                return settings[setting_name]