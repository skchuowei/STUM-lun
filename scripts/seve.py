import minecraft_launcher_lib as mclib

# 使用字符串类型的版本号
minecraft_version = '26.1'

# 查找 Forge 版本
forge_version = mclib.forge.find_forge_version(minecraft_version)

if forge_version:
    print(f"✅ 找到 Forge 版本: {forge_version}")
    print("开始安装 Forge...")
    mclib.forge.install_forge_version(forge_version, r'D:\bing\编程\stum\minecraft')
    print("✅ Forge 安装完成")
else:
    print(f"❌ 未找到 Forge {minecraft_version} 对应版本")

