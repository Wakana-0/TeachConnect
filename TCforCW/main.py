from PyQt5 import uic
from loguru import logger
from datetime import datetime
from .ClassWidgets.base import PluginBase, SettingsBase, PluginConfig  # 导入CW的基类
import sys
from PyQt5.QtWidgets import QHBoxLayout
from qfluentwidgets import ImageLabel, LineEdit
import socket
import json
import threading

# 自定义小组件
WIDGET_CODE = 'widget_test.ui'
WIDGET_NAME = 'TCforCW'
WIDGET_WIDTH = 245



class Plugin(PluginBase):
    def __init__(self, cw_contexts, method):
        super().__init__(cw_contexts, method)
        # 新增服务器实例变量
        self.server = None
        # 其他初始化代码...

    def execute(self):  # 自启动执行部分
        self.plugin_dir = self.cw_contexts['PLUGIN_PATH']
        ipdrss = socket.gethostbyname(socket.gethostname()) #获取本机IP地址
        
        # 创建服务器实例并保存为成员变量
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("0.0.0.0", 11223))
        self.server.listen()
        self.server.setblocking(False)  # 非阻塞模式
        print("开始接收消息")

    def update(self, cw_contexts):  # 自动更新部分
        try:
            # 非阻塞方式检查连接
            conn, addr = self.server.accept()
            print(f"客户端 {addr} 已连接")
            with conn:
                data = conn.recv(1024)
                if data:
                    try:
                        msg = json.loads(data.decode("utf-8"))
                        name = msg.get("name", "未知")
                        message = msg.get("message", "无内容")
                        
                        self.method.send_notification(
                            state=4,
                            title=name,
                            subtitle=" ",
                            content=message,
                            icon=f'{self.plugin_dir}\img\Favicon.png',
                            duration=5000
                        )
                    except json.JSONDecodeError:
                        print("接收到无法解析的消息")
                    except Exception as e:
                        print(f"处理消息时发生错误: {e}")
        except BlockingIOError:
            pass  # 没有新连接时正常继续
        except Exception as e:
            print(f"接收消息时发生错误: {e}")
