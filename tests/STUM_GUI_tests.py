# -*- coding: utf-8 -*-
"""
STUM GUI 测试模块
"""
import sys
import os
import customtkinter as ctk


app = ctk.CTk()
app.title('STUM Launcher')
app.geometry('800x400')
label_text_1 = ctk.CTkLabel(app,text = 'STUM Launcher',font=('Arial', 18))
label_text_1.pack(pady=10)
app.mainloop()