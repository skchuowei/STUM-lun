# -*- coding: utf-8 -*-
"""
Mod开发包下载演示脚本
"""

import sys
sys.path.insert(0, 'd:/bing/编程/stum/tests/modder')

from mod_dev_pack_manager import ModDevPackManager


def main():
    """演示下载流程"""
    print("=== Minecraft Mod开发包下载演示 ===")
    
    # 创建管理器
    manager = ModDevPackManager(download_dir="d:/bing/编程/stum/tests/modder/downloads")
    
    # 获取Minecraft版本列表
    print("\n1. 获取Minecraft版本列表...")
    mc_versions = manager.get_minecraft_versions()
    if mc_versions:
        print(f"   成功获取 {len(mc_versions)} 个版本")
        print(f"   最新版本: {mc_versions[0]['id']}")
    
    # 搜索开发包
    target_version = "1.20.1"
    print(f"\n2. 搜索 Minecraft {target_version} 的开发包...")
    dev_packs = manager.search_all_dev_packs(target_version)
    
    if dev_packs["forge"]:
        # 获取第一个Forge版本
        forge_version = dev_packs["forge"][0]
        print(f"\n3. 准备下载 Forge MDK {forge_version}")
        
        # 获取下载链接
        url = manager.get_forge_mdk_download_url(forge_version)
        if url:
            print(f"   下载链接: {url}")
            
            # 下载文件
            print("\n4. 开始下载...")
            zip_path = manager.download_file(url)
            
            if zip_path:
                print("\n5. 下载完成！")
                print(f"   文件位置: {zip_path}")
                
                # 解压文件
                print("\n6. 解压文件...")
                extract_dir = manager.extract_zip(zip_path)
                if extract_dir:
                    print(f"   解压完成: {extract_dir}")
        else:
            print("   无法获取下载链接")
    else:
        print("   未找到Forge开发包版本")


if __name__ == "__main__":
    main()