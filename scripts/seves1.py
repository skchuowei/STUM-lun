import minecraft_launcher_lib as mclib
import subprocess
import os

minecraft_path = r'D:\bing\编程\stum\minecraft'
minecraft_version = '26.1'

options = {
    'username': 'Player',
    'uuid': 'E25B2FAF-A549-40B6-937D-7604A409419E',
    'token': '',
    'jvm_args': ['-Xmx4G', '-Xms2G', '-Dfile.encoding=UTF-8'],
    'launcher_name': 'STUM',
    'launcher_version': '0.0.1'
}

callback = {
    "setStatus": lambda status: print(f"状态: {status}"),
    "setProgress": lambda progress: print(f"进度: {progress}"),
    "setMax": lambda max_size: print(f"总大小: {max_size}")
}

def is_version_installed(version, minecraft_path):
    """检查版本是否已安装（检查版本文件夹或JSON文件）"""
    version_json = os.path.join(minecraft_path, "versions", version, f"{version}.json")
    version_folder = os.path.join(minecraft_path, "versions", version)
    return os.path.isfile(version_json) or os.path.isdir(version_folder)

def install_minecraft():
    """安装 Minecraft 主程序"""
    if is_version_installed(minecraft_version, minecraft_path):
        print(f"⚠️ Minecraft {minecraft_version} 已安装")
    else:
        print(f"开始安装 Minecraft {minecraft_version}...")
        mclib.install.install_minecraft_version(minecraft_version, minecraft_path, callback)
        print("✅ Minecraft 安装完成")

def install_forge():
    """安装 Forge"""
    forge_version = mclib.forge.find_forge_version(minecraft_version)
    if not forge_version:
        print(f"❌ 未找到 Forge {minecraft_version} 对应版本")
        return None
    
    # 获取实际安装后的版本名称
    installed_forge_version = mclib.forge.forge_to_installed_version(forge_version)
    
    # 检查是否已安装
    if is_version_installed(installed_forge_version, minecraft_path):
        print(f"⚠️ Forge {installed_forge_version} 已安装")
        return installed_forge_version
    
    print(f"开始安装 Forge {forge_version}...")
    mclib.forge.install_forge_version(forge_version, minecraft_path, callback)
    print(f"✅ Forge 安装完成")
    return installed_forge_version

def launch_game(version):
    """启动游戏"""
    if not is_version_installed(version, minecraft_path):
        print(f"❌ 版本 {version} 未安装，请先安装")
        return False
    
    print(f"正在启动 Minecraft {version}...")
    
    # 获取启动命令
    cmd = mclib.command.get_minecraft_command(version, minecraft_path, options)
    
    # 启动游戏
    subprocess.run(cmd)
    print("✅ 游戏已关闭")
    return True

if __name__ == "__main__":
    # 安装 Minecraft
    install_minecraft()
    
    # 安装 Forge（返回完整版本号）
    forge_ver = install_forge()
    
    # 启动游戏（使用 Forge 版本）
    if forge_ver:
        launch_game(forge_ver)
    else:
        # 如果没有 Forge，则启动原版
        launch_game(minecraft_version)