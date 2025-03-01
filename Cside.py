import socket
import json
import os
from plyer import notification
import pygame


# 初始化pygame的混音器
pygame.mixer.init()

# 播放提示音
def play_notification_sound():
    try:
        sound = pygame.mixer.Sound('sound.mp3')
        sound.play()
    except Exception as e:
        notification.notify(
            title="错误! | Error!",
            message=f"播放音频时发生错误: {e}",
            timeout=4  # 通知显示的时长
        )


def save_to_system_log(name, message):
    log_file = os.path.join(os.getenv("APPDATA"), "MessagingApp", "message_log.txt")
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{name}: {message}\n")


def start_server():
    ipdrss = socket.gethostbyname(socket.gethostname())
    # 弹出提示通知
    notification.notify(
        title="提示 | Notification",
        message=f"正在接收消息，本机IP:{ipdrss}",
        timeout=5  # 通知显示的时长
    )

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(("0.0.0.0", 11223))  # 允许所有IP访问
        server.listen()
        print("开始接收消息")

        while True:
            try:
                # 等待客户端连接
                conn, addr = server.accept()
                print(f"客户端 {addr} 已连接")
                with conn:
                    # 接收消息
                    data = conn.recv(1024)
                    if not data:
                        continue

                    try:
                        # 尝试解析收到的JSON数据
                        msg = json.loads(data.decode("utf-8"))
                        name = msg.get("name", "未知")
                        message = msg.get("message", "无内容")

                        # 使用 plyer 弹出通知
                        notification.notify(
                            title=name,
                            message=message,
                            timeout=10  # 通知显示的时长
                        )
                        print(f"接收到消息: {message}")

                        # 播放通知声音
                        play_notification_sound()

                        # 保存到系统消息日志
                        save_to_system_log(name, message)

                    except json.JSONDecodeError:
                        print("接收到无法解析的消息")
                    except Exception as e:
                        print(f"处理消息时发生错误: {e}")

            except Exception as e:
                print(f"服务器发生错误: {e}")
                # 在发生异常时，服务器仍然继续运行


if __name__ == "__main__":
    start_server()
