# -*- coding: utf-8 -*-
"""
STUM - Simple Minecraft Utility Manager
主入口文件 - 命令行交互界面

本程序功能:
- 下载并安装Minecraft游戏
- 启动Minecraft游戏
- 安装Mod加载器（Forge/Fabric/Quilt）
- 更新配置信息
"""

from stum.config import (
    MINECRAFT_PATH,
    MINECRAFT_VERSION,
    DEFAULT_MOD_LOADER,
    build_launch_options,
    update_minecraft_path,
    update_minecraft_version
)
from stum.progress import get_callback
from stum.installer import McInstall
from stum.launcher import Launcher


def main():
    """
    主函数 - 命令行交互主循环

    提供交互式命令行界面，支持以下命令:
    - download_mc: 下载安装Minecraft
    - launch: 启动Minecraft
    - mod_loader: 安装Mod加载器
    - up_path: 更新Minecraft路径
    - up_version: 更新Minecraft版本
    - exit: 退出程序
    """
    # 获取进度回调函数
    callback = get_callback()
    # 构建启动选项
    launch_options = build_launch_options()

    while True:
        # 获取用户输入
        ad_input = input('ps>')
        match ad_input:
            case 'download_mc':
                # 下载安装Minecraft
                installer = McInstall(
                    MINECRAFT_VERSION,
                    MINECRAFT_PATH,
                    DEFAULT_MOD_LOADER,
                    callback
                )
                installer.install_minecraft()

            case 'launch':
                # 启动Minecraft
                launcher = Launcher(
                    MINECRAFT_PATH,
                    MINECRAFT_VERSION,
                    launch_options
                )
                launcher.launch()

            case 'exit':
                # 退出程序
                print("程序已退出")
                break

            case 'up_path':
                # 更新Minecraft路径
                new_path = input('STUM/up/path>')
                update_minecraft_path(new_path)

            case 'up_version':
                # 更新Minecraft版本
                new_version = input('STUM/up/version>')
                update_minecraft_version(new_version)

            case 'mod_loader':
                # 安装Mod加载器
                installer = McInstall(
                    MINECRAFT_VERSION,
                    MINECRAFT_PATH,
                    DEFAULT_MOD_LOADER,
                    callback
                )
                installer.install_mod_loader()

            case _:
                # 未知命令
                print("未知命令！可用命令：download_mc、launch、exit、up_path、up_version")


if __name__ == "__main__":
    main()
