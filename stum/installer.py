# -*- coding: utf-8 -*-
"""
安装模块 - 处理Minecraft和Mod加载器的安装

本模块功能:
- 安装原版Minecraft
- 安装Forge模组加载器
- 安装Fabric模组加载器
- 安装Quilt模组加载器
"""

import minecraft_launcher_lib as mclib


class McInstall:
    """
    Minecraft安装器类

    用于管理Minecraft游戏本体的安装和Mod加载器的安装
    """

    def __init__(self, minecraft_version, minecraft_path, mod_loader, callback):
        """
        初始化安装器

        参数:
            minecraft_version (str): Minecraft版本号
            minecraft_path (str): Minecraft安装目录路径
            mod_loader (str): Mod加载器类型 ('forge', 'fabric', 'quilt')
            callback (dict): 进度回调函数字典
        """
        self.minecraft_version = minecraft_version
        self.minecraft_path = minecraft_path
        self.mod_loader = mod_loader
        self.callback = callback

    def install_minecraft(self):
        """
        安装原版Minecraft游戏本体

        使用minecraft-launcher-lib库下载并安装指定版本的Minecraft
        """
        mclib.install.install_minecraft_version(
            self.minecraft_version,
            self.minecraft_path,
            self.callback
        )
        print('下载完成')

    def install_mod_loader(self):
        """
        安装Mod加载器（Forge/Fabric/Quilt）

        根据self.mod_loader的类型选择对应的加载器进行安装
        """
        if self.mod_loader == 'forge':
            print('安装mod加载器')
            # 查找Forge版本
            forge_version = mclib.forge.find_forge_version(self.minecraft_version)
            # 获取实际安装的版本名称
            forge_install_version = mclib.forge.forge_to_installed_version(forge_version)
            # 安装Forge
            mclib.forge.install_forge_version(
                forge_install_version,
                self.minecraft_path,
                self.callback
            )
            print('下载完成')

        elif self.mod_loader == 'fabric':
            print('安装mod加载器')
            mclib.fabric.install_fabric(
                self.minecraft_version,
                self.minecraft_path,
                self.callback
            )
            print('下载完成')

        elif self.mod_loader == 'quilt':
            print('安装mod加载器')
            mclib.quilt.install_quilt(
                self.minecraft_version,
                self.minecraft_path,
                self.callback
            )
            print('下载完成')    
    def get_minecraft_version_web(self):
        mc_version = mclib.utils.get_versions()
        for version in mc_version:
            print(f'版本：{version["id"]}\n类型：{version["type"]}发布时间：{version["releaseTime"]}')

