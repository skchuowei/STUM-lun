# -*- coding: utf-8 -*-
"""
启动模块 - 处理Minecraft游戏的启动

本模块功能:
- 构建Minecraft启动命令
- 执行Minecraft游戏启动
"""

import subprocess
import minecraft_launcher_lib as mclib


class Launcher:
    """
    Minecraft启动器类

    用于管理Minecraft游戏的启动过程
    """

    def __init__(self, minecraft_path, minecraft_version, launch_options):
        """
        初始化启动器

        参数:
            minecraft_path (str): Minecraft安装目录路径
            minecraft_version (str): Minecraft版本号
            launch_options (dict): 启动选项字典，包含用户名、UUID、JVM参数等
        """
        self.minecraft_path = minecraft_path
        self.minecraft_version = minecraft_version
        self.launch_options = launch_options

    def launch(self):
        """
        启动Minecraft游戏

        使用minecraft-launcher-lib库生成启动命令，
        然后通过subprocess执行启动游戏
        """
        # 使用minecraft-launcher-lib生成启动命令
        command = mclib.command.get_minecraft_command(
            self.minecraft_path,
            self.minecraft_version,
            self.launch_options
        )
        try:
            # 执行启动命令
            subprocess.run(command)
        except subprocess.CalledProcessError as e:
            print(f"启动Minecraft游戏时出错: {e}")
        else:
            print("Minecraft游戏启动成功")
