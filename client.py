import socket
from crypto.crypto import load_key, encrypt_message

key = load_key()

# Ввод IP и порта
host = input("Введите IP-адрес сервера: ").strip()
port_input = input("Введите порт (по умолчанию 65432): ").strip()
port = int(port_input) if port_input else 65432

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f"[Client] Подключено к {host}:{port}. Введите сообщение:")
        while True:
            msg = input("> ")
            if msg.lower() in ["exit", "quit"]:
                print("[Client] Завершение...")
                break
            encrypted = encrypt_message(msg, key)
            s.sendall(encrypted)
except Exception as e:
    print(f"[Ошибка] Не удалось подключиться: {e}")
