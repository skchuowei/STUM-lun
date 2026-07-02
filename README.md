# STUM - Simple Minecraft Utility Manager

一个简单的Minecraft启动器和安装工具，支持Forge、Fabric、Quilt等mod加载器。

## 项目结构

```
stum/
├── stum/                  # 主包目录
│   ├── __init__.py        # 包初始化
│   ├── config.py          # 配置模块
│   ├── progress.py        # 进度显示模块
│   ├── installer.py       # 安装模块
│   └── launcher.py        # 启动模块
├── tests/                 # 测试目录
│   └── __init__.py
├── scripts/               # 脚本目录
│   ├── seve.py
│   ├── seves1.py
│   └── Global_File_Manager.py
├── docs/                  # 文档目录
├── main.py                # 主入口文件
├── requirements.txt       # 依赖列表
└── README.md              # 说明文档
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

运行程序：

```bash
python main.py
```

## 可用命令

- `download_mc` - 下载并安装Minecraft
- `launch` - 启动Minecraft
- `up_path` - 更新Minecraft路径
- `up_version` - 更新Minecraft版本
- `mod_loader` - 安装mod加载器
- `exit` - 退出程序

## 特性

- 支持安装原版Minecraft
- 支持Forge、Fabric、Quilt等mod加载器
- 实时进度显示，进度条固定在底部
- 可自定义JVM参数
- 可自定义用户信息

## 配置

编辑 `stum/config.py` 文件来修改默认配置：

- `MINECRAFT_PATH` - Minecraft安装路径
- `MINECRAFT_VERSION` - 默认Minecraft版本
- `JVM_MAX_MEMORY` - 最大内存(GB)
- `JVM_INIT_MEMORY` - 初始内存(GB)
- `USER_PLAYER_ID` - 玩家ID
- `USER_PLAYER_UUID` - 玩家UUID
- `DEFAULT_MOD_LOADER` - 默认mod加载器

## 许可证

MIT License
