# -*- coding: utf-8 -*-
"""
Mod开发包管理器测试脚本
"""

import sys
sys.path.insert(0, 'd:/bing/编程/stum/tests/modder')

from mod_dev_pack_manager import ModDevPackManager


def test_minecraft_versions():
    """测试获取Minecraft版本列表"""
    print("=== 测试获取Minecraft版本列表 ===")
    manager = ModDevPackManager()
    versions = manager.get_minecraft_versions()
    
    if versions:
        print(f"成功获取到 {len(versions)} 个Minecraft版本")
        print("最新的5个版本:")
        for v in versions[:5]:
            print(f"  - {v['id']} ({v['type']})")
        return True
    else:
        print("获取版本列表失败")
        return False


def test_search_dev_packs():
    """测试搜索开发包"""
    print("\n=== 测试搜索开发包 ===")
    manager = ModDevPackManager()
    
    test_version = "1.20.1"
    print(f"搜索 Minecraft {test_version} 的开发包...")
    
    packs = manager.search_all_dev_packs(test_version)
    
    for pack_type, versions in packs.items():
        print(f"\n{pack_type.upper()}: {len(versions)} 个版本")
        if versions:
            print(f"  示例版本: {versions[:3]}")
    
    return True


def test_download_url():
    """测试获取下载链接"""
    print("\n=== 测试获取下载链接 ===")
    manager = ModDevPackManager()
    
    forge_version = "1.20.1-47.4.10"
    url = manager.get_forge_mdk_download_url(forge_version)
    
    if url:
        print(f"Forge MDK {forge_version} 的下载链接:")
        print(f"  {url}")
        return True
    else:
        print(f"无法获取 Forge MDK {forge_version} 的下载链接")
        return False


def main():
    """运行所有测试"""
    print("=== Mod开发包管理器测试 ===")
    
    test_minecraft_versions()
    test_search_dev_packs()
    test_download_url()
    
    print("\n=== 测试完成 ===")


if __name__ == "__main__":
    main()