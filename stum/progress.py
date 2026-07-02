# -*- coding: utf-8 -*-
"""
进度显示模块 - 管理安装/下载时的进度条和状态信息显示

本模块功能:
- 进度条始终固定在终端底部
- 状态信息像日志一样在上方实时输出
- 支持与minecraft-launcher-lib库配合使用
"""

# 全局变量：记录当前进度条内容，用于清除和重绘
total_size = 0
last_progress_line = ""


def show_status(status):
    """
    显示状态信息（像日志一样换行输出）

    参数:
        status (str): 状态信息内容
    """
    global last_progress_line
    # 先清除进度条行
    if last_progress_line:
        print(f"\r{' ' * len(last_progress_line)}", end="\r")
    # 输出状态信息（自动换行）
    print(f"[状态] {status}")
    # 重新输出进度条到底部
    if last_progress_line:
        print(last_progress_line, end="", flush=True)


def show_progress(current):
    """
    显示进度条（固定在终端底部）

    参数:
        current (int): 当前已完成的进度值
    """
    global total_size, last_progress_line
    if total_size <= 0:
        return

    # 计算进度百分比
    percent = int((current / total_size) * 100)
    bar_len = 20
    filled = int(bar_len * percent / 100)
    bar = "▦" * filled + "▬" * (bar_len - filled)
    progress_line = f"[进度] [{bar}] {percent}%"

    # 清除旧进度条，输出新进度条
    if last_progress_line:
        print(f"\r{' ' * len(last_progress_line)}", end="\r")
    print(progress_line, end="", flush=True)
    last_progress_line = progress_line


def set_max(m):
    """
    设置进度条最大值

    参数:
        m (int): 总进度大小
    """
    global total_size
    total_size = m


def get_callback():
    """
    获取minecraft-launcher-lib所需的回调函数字典

    返回:
        dict: 包含setStatus、setProgress、setMax的回调字典
    """
    return {
        "setStatus": show_status,
        "setProgress": show_progress,
        "setMax": set_max
    }
