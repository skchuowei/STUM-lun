'''
全局文件管理器
将所有文件操作都集中在这个模块中，方便管理和维护，及当前选择的示例
'''
import os
import shutil
import minecraft_launcher_lib as mclib
from config import *

def update_minecraft_path(new_path):
    """
    更新Minecraft安装路径

    参数:
        new_path (str): 新的Minecraft路径
    """
    global MINECRAFT_PATH
    MINECRAFT_PATH = new_path


def update_minecraft_version(new_version):
    """
    更新Minecraft版本号

    参数:
        new_version (str): 新的Minecraft版本号
    """
    global MINECRAFT_VERSION
    MINECRAFT_VERSION = new_version
def change_dist(dak,gh,f):
    dak[gh] = f
    return 0
def cover_dist(y_dist,x_dist):
    x_dist.clear()
    x_dist = y_dist
    return 0
