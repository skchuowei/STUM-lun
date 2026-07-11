# -*- coding: utf-8 -*-
"""
配置模块 - 存储和管理所有配置项

本模块包含:
- Minecraft路径和版本配置
- JVM内存参数配置
- 用户信息配置
- Mod加载器配置
- 配置更新函数
"""

import os

# Minecraft相关配置
MINECRAFT_PATH = 'D:\\bing\\编程\\stum\\minecraft'
MINECRAFT_VERSION = '1.21.11'

# JVM参数配置（单位：GB）
JVM_MAX_MEMORY = '4'
JVM_INIT_MEMORY = '1'

# 用户信息配置
USER_PLAYER_ID = 'pin'
USER_PLAYER_UUID = 'E25B2FAF-A549-40B6-937D-7604A409419E'

# Mod加载器配置（可选值: forge, fabric, quilt）
DEFAULT_MOD_LOADER = 'forge'


def build_jvm_args():
    """
    构建JVM参数列表

    返回:
        list: JVM参数列表，包含最大内存、初始内存和编码设置
    """
    jvm_max = f'-Xmx{JVM_MAX_MEMORY}G'
    jvm_init = f'-Xms{JVM_INIT_MEMORY}G'
    return [jvm_max, jvm_init, '-Dfile.encoding=UTF-8']


def build_launch_options():
    """
    构建Minecraft启动选项字典

    返回:
        dict: 包含用户名、UUID、token、JVM参数、启动器信息的字典
    """
    return {
        'username': USER_PLAYER_ID,
        'uuid': USER_PLAYER_UUID,
        'token': "",
        'jvm_args': build_jvm_args(),
        'launcher_name': 'stum',
        'launcher_version': '0.0.1',
    }


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



