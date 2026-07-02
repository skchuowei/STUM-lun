# STUM-lun

> **项目状态**：目前项目处于前期，暂无 GUI，一些功能还没有实现。代码和文档会持续迭代更新，欢迎关注。

STUM-Lun 全称 **Start Up Minecraft Launcher**，一个基于 Python 的 Minecraft 启动器，UI 设计参考 PCL。

## 项目简介

**STUM** = Simple Minecraft Utility Manager

一款轻量级的 Minecraft 启动器和安装工具，支持原版游戏下载，以及 Forge、Fabric、Quilt 等主流 Mod 加载器的安装。

---

## 项目结构

```
stum/
├── stum/                         # 主包目录
│   ├── __init__.py               # 包初始化
│   ├── config.py                 # 配置模块
│   ├── progress.py               # 进度显示模块
│   ├── installer.py              # 安装模块
│   ├── launcher.py               # 启动模块
│   └── Minecraft_Modpack_inst.py # 模组包安装模块
├── tests/                        # 测试目录
│   ├── __init__.py
│   ├── STUM_GUI_tests.py
│   ├── unittest_guide.md
│   └── modder/                   # 模组开发测试
│       ├── __init__.py
│       ├── demo_download.py
│       ├── mod_dev_pack_manager.py
│       └── test_mod_dev_pack.py
├── scripts/                      # 脚本目录
│   ├── seve.py
│   ├── seves1.py
│   └── Global_File_Manager.py
├── learn/                        # 学习示例
│   └── 1class.py
├── docs/                         # 文档目录
├── main.py                       # 主入口文件
├── requirements.txt              # 依赖列表
└── README.md                     # 说明文档
```

---

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 启动程序

```bash
python main.py
```

### 3. 交互命令

程序启动后，在终端输入命令进行操作：

| 命令 | 说明 |
|------|------|
| `download_mc` | 下载并安装 Minecraft |
| `launch` | 启动 Minecraft |
| `up_path` | 更新 Minecraft 安装路径 |
| `up_version` | 切换 Minecraft 版本 |
| `mod_loader` | 安装 Mod 加载器 |
| `exit` | 退出程序 |

---

## 功能特性

- **版本安装**：支持下载并安装原版 Minecraft
- **Mod 加载器**：支持 Forge、Fabric、Quilt 等主流加载器
- **进度显示**：实时展示操作进度，进度条固定于底部
- **参数自定义**：可自定义 JVM 内存参数与启动选项
- **用户配置**：支持自定义玩家 ID、UUID 等用户信息

---

## 配置文件

编辑 `stum/config.py` 修改默认配置：

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| `MINECRAFT_PATH` | Minecraft 安装目录 | `./minecraft` |
| `MINECRAFT_VERSION` | 默认游戏版本 | `1.20.1` |
| `JVM_MAX_MEMORY` | JVM 最大内存 | `4` (GB) |
| `JVM_INIT_MEMORY` | JVM 初始内存 | `2` (GB) |
| `USER_PLAYER_ID` | 玩家显示名称 | `Player` |
| `USER_PLAYER_UUID` | 玩家 UUID | 随机生成 |
| `DEFAULT_MOD_LOADER` | 默认 Mod 加载器 | `None` |

---

## 许可证

[GPL-2.0 License](LICENSE)

---

## 开发随笔

本项目最初受到 MCMod 社区的启发，曾设想在启动器中嵌入一套专为 Minecraft 模组开发设计的工具链（IDE），以降低新手入门门槛。然而在深入了解后发现，当前 MCMod 开发社区资源分散、门槛较高，新手往往难以上手。正是基于这一观察，我萌生了一个更大的愿景：**打造一个包容、开放、友好的 MCMod 开发社区**，让每一位对模组开发感兴趣的玩家都能轻松参与、共同成长。

我深知仅凭一人之力难以完成这个目标，因此未来计划创建开发者交流群。不过就现阶段而言，时机尚早。如果你对这个项目感兴趣，欢迎持续关注开发进度。

> **关于我**：我目前还是一名初中生，精力和时间有限，开发进度可能较慢，还请见谅。你也可以关注我的 B 站动态了解最新消息：
>
> **B 站昵称**：平行世界的小熊
