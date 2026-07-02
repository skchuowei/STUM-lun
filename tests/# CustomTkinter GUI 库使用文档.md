# CustomTkinter GUI 库使用文档

## 简介

CustomTkinter 是 Python 的 UI 库，基于 Tkinter 封装，提供了**现代化的扁平化外观**。

### 特点
- 内置暗色/亮色主题
- 组件丰富，开箱即用
- 跨平台（Windows/macOS/Linux）
- API 简单，学习成本低

### 安装

```bash
pip install customtkinter
```

---

## 快速开始

### 基础窗口

```python
import customtkinter as ctk

app = ctk.CTk()
app.title("我的应用")
app.geometry("400x300")
app.mainloop()
```

---

## 常用组件

| 组件 | 类名 | 用途 |
|------|------|------|
| 标签 | `CTkLabel` | 显示文字 |
| 按钮 | `CTkButton` | 点击操作 |
| 输入框 | `CTkEntry` | 单行输入 |
| 文本框 | `CTkTextbox` | 多行文本/日志 |
| 进度条 | `CTkProgressBar` | 显示进度 |
| 下拉菜单 | `CTkOptionMenu` | 选项选择 |
| 复选框 | `CTkCheckBox` | 多选 |
| 开关 | `CTkSwitch` | 开关 |
| 滑块 | `CTkSlider` | 数值调节 |
| 框架 | `CTkFrame` | 容器 |
| 标签页 | `CTkTabview` | 分页 |
| 可滚动框架 | `CTkScrollableFrame` | 滚动区域 |

---

## 完整示例：STUM 启动器 GUI

```python
import customtkinter as ctk
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class STUMGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("STUM - Minecraft 启动器")
        self.geometry("500x550")

        # 标题
        self.title_label = ctk.CTkLabel(
            self, text="STUM Launcher",
            font=("微软雅黑", 28, "bold")
        )
        self.title_label.pack(pady=20)

        # 设置区域
        self.settings_frame = ctk.CTkFrame(self)
        self.settings_frame.pack(pady=10, padx=20, fill="x")

        self.version_menu = ctk.CTkOptionMenu(
            self.settings_frame,
            values=["1.21.11", "1.20.4", "1.19.2"]
        )
        self.version_menu.grid(row=0, column=1, padx=10, pady=10)

        # 按钮区域
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=10)

        self.install_btn = ctk.CTkButton(
            self.button_frame, text="下载安装",
            width=150, command=self.install_minecraft
        )
        self.install_btn.grid(row=0, column=0, padx=10)

        self.launch_btn = ctk.CTkButton(
            self.button_frame, text="启动游戏",
            width=150, command=self.launch_game
        )
        self.launch_btn.grid(row=0, column=1, padx=10)

        # 进度条
        self.progress = ctk.CTkProgressBar(self, width=400)
        self.progress.pack(pady=10)
        self.progress.set(0)

        # 日志框
        self.log_box = ctk.CTkTextbox(
            self, width=460, height=200,
            font=("Consolas", 11)
        )
        self.log_box.pack(pady=5, padx=20)

    def log(self, message):
        self.log_box.insert("end", f"> {message}\n")
        self.log_box.see("end")
        self.update()

    def install_minecraft(self):
        def task():
            for i in range(11):
                import time
                time.sleep(0.3)
                self.progress.set(i / 10)
                self.log(f"下载中... {i * 10}%")
            self.log("下载完成！")

        threading.Thread(target=task, daemon=True).start()

    def launch_game(self):
        self.log("启动游戏...")
        self.progress.start()


if __name__ == "__main__":
    app = STUMGUI()
    app.mainloop()
```

---

## 主题配置

```python
# 外观模式
ctk.set_appearance_mode("dark")    # 暗色
ctk.set_appearance_mode("light")   # 亮色
ctk.set_appearance_mode("system")  # 跟随系统

# 颜色主题
ctk.set_default_color_theme("blue")
ctk.set_default_color_theme("green")
ctk.set_default_color_theme("dark-blue")
```

---

## 布局管理

```python
# pack - 顺序排列
widget.pack(pady=10, padx=10, fill="x", side="left")

# grid - 网格排列
widget.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

# place - 绝对定位
widget.place(x=100, y=50, relx=0.5, rely=0.5, anchor="center")
```

---

## 最佳实践

1. **耗时操作放线程** - `threading.Thread(target=task, daemon=True).start()`
2. **使用网格布局** - 比 pack 更好控制
3. **分离UI和逻辑** - 业务代码独立于界面
4. **添加日志** - 方便调试
5. **使用状态栏** - 给用户明确反馈