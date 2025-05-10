import socket
from crypto.crypto import load_key, decrypt_message

key = load_key()
port = 65432

def get_external_ip():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception:
        return "Не удалось определить"

def choose_host():
    print("Выберите режим запуска сервера:")
    print("1. Локально (только на этом устройстве)")
    print("2. Публично (внутрисеть/VPN/внешнее подключение)")
    choice = input("Выбор (1/2): ")

    if choice == "1":
        return "127.0.0.1"
    elif choice == "2":
        ip = get_external_ip()
        print(f"[Server] Внешний IP: {ip}")
        return "0.0.0.0"
    else:
        print("Неверный выбор. Запуск локально по умолчанию.")
        return "127.0.0.1"

host = choose_host()

print("[Server] Запуск сервера...")
print(f"[Server] IP для подключения: {host if host != '0.0.0.0' else get_external_ip()}")
print(f"[Server] Порт: {port}")
print("[Server] Ожидание подключения клиента...")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"[Server] Подключено: {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            decrypted = decrypt_message(data, key)
            print(f"[Client] {decrypted}")
