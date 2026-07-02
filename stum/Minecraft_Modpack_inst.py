#Minecraft Modpack Installation Module
#mc整合包安装模块
'''
CureForge格式说明;
1.后缀名：.zip
2.
Modrinth格式说明：
1.后缀名：.mrpack
2.唯一强制文件：压缩包根目录必须存在 modrinth.index.json（UTF-8），无此文件则不是合法 mrpack
3.mrpack 内部不存放任何 mod jar，只存下载索引；
pack.mrpack
├─ modrinth.index.json       # 【强制】整合包主清单，所有下载、版本、加载器信息
├─ overrides/                # 【通用覆盖，可选】客户端+服务端共用文件
│  ├─ config/
│  ├─ mods/                  # 极少用，一般mod走线上索引，这里放离线内置mod
│  ├─ resourcepacks/
│  ├─ shaderpacks/
│  ├─ saves/
│  ├─ datapacks/
│  ├─ scripts/
│  ├─ options.txt
│  └─ 其他 .minecraft 根目录文件
├─ client-overrides/         # 【可选】仅客户端安装时复制，服务器忽略
│  └─ 目录结构同 .minecraft
└─ server-overrides/         # 【可选】仅服务器部署时复制，客户端启动器直接跳过
   └─ 目录结构同 .minecraft
'''
