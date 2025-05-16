# Copyright 2025 Said Emirhan Döke
# Licensed under the Apache License, Version 2.0

import tkinter as tk
from main_gui import Application
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from utils import Utils

if __name__ == "__main__":
    root = ttk.Window(themename=Utils.load_user_settings("theme"))
    app = Application(root)
    root.mainloop()