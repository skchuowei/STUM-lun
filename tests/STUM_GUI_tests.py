# -*- coding: utf-8 -*-
"""
STUM GUI 测试模块
"""
import sys
import os
import  customtkinter as ctk
import stum.launcher as launcher
from stum.config import (
    MINECRAFT_PATH,
    MINECRAFT_VERSION,
    DEFAULT_MOD_LOADER,
    build_launch_options,
    update_minecraft_path,
    update_minecraft_version
)
#变量



#
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
class launcher_test(ctk.CTk, launcher.Launcher):
    def __init__(self):
        super().__init__()
        self.minecraft_path = MINECRAFT_PATH,
        self.minecraft_version = MINECRAFT_VERSION,
        