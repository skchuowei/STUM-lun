# -*- coding: utf-8 -*-
"""
Minecraft Mod开发包管理器

功能：
- 搜索所有版本的Minecraft Mod开发包
- 下载指定的开发包
- 支持Forge MDK、Fabric Loom、Quilt Loom
"""

import os
import json
import zipfile
import requests
from urllib.parse import urljoin
from typing import List, Dict, Optional, Any
from bs4 import BeautifulSoup


class ModDevPackManager:
    """
    Mod开发包管理器类
    """
    
    # 官方API端点
    MINECRAFT_VERSION_MANIFEST = "https://launchermeta.mojang.com/mc/game/version_manifest.json"
    
    # Forge API
    FORGE_PROMOTIONS_URL = "https://files.minecraftforge.net/net/minecraftforge/forge/promotions_slim.json"
    FORGE_MAVEN_URL = "https://maven.minecraftforge.net/net/minecraftforge/forge/"
    
    # Fabric API
    FABRIC_META_URL = "https://meta.fabricmc.net/v2/versions/loader"
    
    # Quilt API
    QUILT_META_URL = "https://meta.quiltmc.org/v3/versions/loader"
    
    # 请求头，避免被服务器拒绝
    REQUEST_HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    def __init__(self, download_dir: str = None):
        """
        初始化管理器
        
        参数:
            download_dir: 下载目录，默认为当前目录下的downloads文件夹
        """
        if download_dir is None:
            download_dir = os.path.join(os.getcwd(), "downloads")
        self.download_dir = download_dir
        os.makedirs(self.download_dir, exist_ok=True)
    
    def get_minecraft_versions(self) -> List[Dict[str, str]]:
        """
        获取所有Minecraft版本列表
        
        返回:
            版本列表，包含id和类型信息
        """
        try:
            response = requests.get(self.MINECRAFT_VERSION_MANIFEST)
            response.raise_for_status()
            manifest = response.json()
            return manifest.get("versions", [])
        except Exception as e:
            print(f"获取Minecraft版本列表失败: {e}")
            return []
    
    def search_forge_mdk_versions(self, mc_version: str = None) -> List[str]:
        """
        搜索Forge MDK版本
        
        参数:
            mc_version: Minecraft版本号，如"1.20.1"，None表示搜索所有版本
        
        返回:
            Forge MDK版本列表（完整格式，如 "1.20.1-47.1.0"）
        """
        versions = []
        try:
            response = requests.get(self.FORGE_PROMOTIONS_URL, headers=self.REQUEST_HEADERS)
            response.raise_for_status()
            promotions = response.json()
            
            if "promos" in promotions:
                for version_key, forge_version in promotions["promos"].items():
                    if mc_version:
                        if version_key.startswith(mc_version):
                            versions.append(f"{mc_version}-{forge_version}")
                    else:
                        mc_ver = version_key.split("-")[0] if "-" in version_key else version_key
                        versions.append(f"{mc_ver}-{forge_version}")
        except Exception as e:
            print(f"搜索Forge MDK版本失败: {e}")
        
        return sorted(versions)
    
    def search_fabric_loom_versions(self, mc_version: str = None) -> List[str]:
        """
        搜索Fabric Loom版本
        
        参数:
            mc_version: Minecraft版本号，如"1.20.1"，None表示搜索所有版本
        
        返回:
            Fabric Loom版本列表
        """
        versions = []
        try:
            response = requests.get(self.FABRIC_META_URL, headers=self.REQUEST_HEADERS)
            response.raise_for_status()
            fabric_data = response.json()
            
            for mc_data in fabric_data:
                game_version = mc_data.get("gameVersion", "")
                if mc_version and not game_version.startswith(mc_version):
                    continue
                
                for loader in mc_data.get("loaders", []):
                    loader_version = loader.get("version", "")
                    if loader_version:
                        version_str = f"{game_version}-{loader_version}"
                        versions.append(version_str)
        except Exception as e:
            print(f"搜索Fabric Loom版本失败: {e}")
        
        return sorted(list(set(versions)))
    
    def search_quilt_loom_versions(self, mc_version: str = None) -> List[str]:
        """
        搜索Quilt Loom版本
        
        参数:
            mc_version: Minecraft版本号，如"1.20.1"，None表示搜索所有版本
        
        返回:
            Quilt Loom版本列表
        """
        versions = []
        try:
            response = requests.get(self.QUILT_META_URL, headers=self.REQUEST_HEADERS)
            response.raise_for_status()
            quilt_data = response.json()
            
            if isinstance(quilt_data, list):
                for mc_data in quilt_data:
                    game_version = mc_data.get("game_version", "")
                    if mc_version and not game_version.startswith(mc_version):
                        continue
                    
                    loader_version = mc_data.get("loader", {}).get("version", "")
                    if loader_version:
                        version_str = f"{game_version}-{loader_version}"
                        versions.append(version_str)
            elif isinstance(quilt_data, dict):
                for mc_data in quilt_data.get("game_versions", []):
                    game_version = mc_data.get("version", "")
                    if mc_version and not game_version.startswith(mc_version):
                        continue
                    
                    for loader in mc_data.get("loaders", []):
                        loader_version = loader.get("version", "")
                        if loader_version:
                            version_str = f"{game_version}-{loader_version}"
                            versions.append(version_str)
        except Exception as e:
            print(f"搜索Quilt Loom版本失败: {e}")
        
        return sorted(list(set(versions)))
    
    def search_all_dev_packs(self, mc_version: str = None) -> Dict[str, List[str]]:
        """
        搜索所有类型的开发包版本
        
        参数:
            mc_version: Minecraft版本号，如"1.20.1"，None表示搜索所有版本
        
        返回:
            包含各类型开发包版本的字典
        """
        print(f"正在搜索开发包版本，Minecraft版本: {mc_version if mc_version else '全部'}")
        
        return {
            "forge": self.search_forge_mdk_versions(mc_version),
            "fabric": self.search_fabric_loom_versions(mc_version),
            "quilt": self.search_quilt_loom_versions(mc_version)
        }
    
    def get_forge_mdk_download_url(self, forge_version: str) -> Optional[str]:
        """
        获取Forge MDK下载链接
        
        参数:
            forge_version: Forge版本号
        
        返回:
            下载链接，如果获取失败返回None
        """
        try:
            if "-" in forge_version:
                mc_version = forge_version.split("-")[0]
                forge_build = forge_version.split("-")[1]
                
                urls_to_try = [
                    f"https://maven.minecraftforge.net/net/minecraftforge/forge/{forge_version}/forge-{forge_version}-mdk.zip",
                    f"https://files.minecraftforge.net/maven/net/minecraftforge/forge/{forge_version}/forge-{forge_version}-mdk.zip"
                ]
                
                for url in urls_to_try:
                    try:
                        response = requests.head(url, headers=self.REQUEST_HEADERS, allow_redirects=True)
                        if response.status_code == 200:
                            return url
                    except:
                        continue
                
                return urls_to_try[0]
        except Exception as e:
            print(f"获取Forge MDK下载链接失败: {e}")
        
        return None
    
    def get_fabric_loom_download_url(self, loom_version: str) -> Optional[str]:
        """
        获取Fabric Loom下载链接
        
        参数:
            loom_version: Loom版本号
        
        try:
            versions = []
            response = requests.get(self.QUILT_MAVEN_URL)
        try:
            version_url = urljoin(self.FABRIC_MAVEN_URL, loom_version + "/")
            response = requests.get(version_url, headers=self.REQUEST_HEADERS)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, "html.parser")
            
            for link in soup.find_all("a"):
                href = link.get("href")
                if href and href.endswith("-dev.zip"):
                    return urljoin(version_url, href)
        except Exception as e:
            print(f"获取Fabric Loom下载链接失败: {e}")
        
        return None
    
    def get_quilt_loom_download_url(self, loom_version: str) -> Optional[str]:
        """
        获取Quilt Loom下载链接
        
        参数:
            loom_version: Loom版本号
        
        返回:
            下载链接，如果获取失败返回None
        """
        try:
            version_url = urljoin(self.QUILT_MAVEN_URL, loom_version + "/")
            response = requests.get(version_url, headers=self.REQUEST_HEADERS)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, "html.parser")
            
            for link in soup.find_all("a"):
                href = link.get("href")
                if href and href.endswith("-dev.zip"):
                    return urljoin(version_url, href)
        except Exception as e:
            print(f"获取Quilt Loom下载链接失败: {e}")
        
        return None
    
    def download_file(self, url: str, filename: str = None) -> Optional[str]:
        """
        下载文件
        
        参数:
            url: 下载链接
            filename: 保存的文件名，默认为URL中的文件名
        
        返回:
            下载后的文件路径，如果下载失败返回None
        """
        if filename is None:
            filename = os.path.basename(url)
        
        save_path = os.path.join(self.download_dir, filename)
        
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            total_size = int(response.headers.get("content-length", 0))
            downloaded_size = 0
            
            with open(save_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded_size += len(chunk)
                        if total_size > 0:
                            progress = (downloaded_size / total_size) * 100
                            print(f"\r下载进度: {progress:.2f}%", end="")
            
            print(f"\n文件已下载: {save_path}")
            return save_path
        
        except Exception as e:
            print(f"\n下载失败: {e}")
            if os.path.exists(save_path):
                os.remove(save_path)
            return None
    
    def download_dev_pack(self, pack_type: str, version: str) -> Optional[str]:
        """
        下载指定类型和版本的开发包
        
        参数:
            pack_type: 开发包类型 ('forge', 'fabric', 'quilt')
            version: 开发包版本号
        
        返回:
            下载后的文件路径，如果下载失败返回None
        """
        print(f"准备下载 {pack_type} 开发包，版本: {version}")
        
        url = None
        if pack_type == "forge":
            url = self.get_forge_mdk_download_url(version)
        elif pack_type == "fabric":
            url = self.get_fabric_loom_download_url(version)
        elif pack_type == "quilt":
            url = self.get_quilt_loom_download_url(version)
        
        if url:
            print(f"下载链接: {url}")
            return self.download_file(url)
        else:
            print(f"无法获取 {pack_type} {version} 的下载链接")
            return None
    
    def extract_zip(self, zip_path: str, extract_dir: str = None) -> Optional[str]:
        """
        解压ZIP文件
        
        参数:
            zip_path: ZIP文件路径
            extract_dir: 解压目录，默认为下载目录下同名文件夹
        
        返回:
            解压后的目录路径，如果解压失败返回None
        """
        if extract_dir is None:
            extract_dir = zip_path.replace(".zip", "")
        
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)
            print(f"文件已解压到: {extract_dir}")
            return extract_dir
        except Exception as e:
            print(f"解压失败: {e}")
            return None


def main():
    """
    示例用法
    """
    # 创建管理器，指定下载目录
    manager = ModDevPackManager(download_dir="d:/bing/编程/stum/tests/modder/downloads")
    
    # 获取所有Minecraft版本
    print("\n=== 获取Minecraft版本列表 ===")
    mc_versions = manager.get_minecraft_versions()
    if mc_versions:
        print(f"找到 {len(mc_versions)} 个Minecraft版本")
        # 只显示前10个版本
        for version in mc_versions[:10]:
            print(f"  - {version['id']} ({version['type']})")
    
    # 搜索特定版本的开发包
    target_mc_version = "1.20.1"
    print(f"\n=== 搜索 Minecraft {target_mc_version} 的开发包 ===")
    dev_packs = manager.search_all_dev_packs(target_mc_version)
    
    for pack_type, versions in dev_packs.items():
        print(f"\n{pack_type.upper()} 开发包版本:")
        if versions:
            for version in versions[:5]:  # 只显示前5个
                print(f"  - {version}")
            if len(versions) > 5:
                print(f"  ... 还有 {len(versions) - 5} 个版本")
        else:
            print("  未找到版本")
    
    # 示例：下载一个Forge MDK
    if dev_packs["forge"]:
        forge_version = dev_packs["forge"][0]
        print(f"\n=== 下载 Forge MDK {forge_version} ===")
        zip_path = manager.download_dev_pack("forge", forge_version)
        
        if zip_path:
            print("\n=== 解压开发包 ===")
            manager.extract_zip(zip_path)


if __name__ == "__main__":
    main()