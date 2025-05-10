#!/bin/bash

echo "[*] Установка виртуального окружения..."
python3 -m venv venv
source venv/bin/activate

echo "[*] Установка зависимостей Python..."
pip install --upgrade pip
pip install cryptography

echo "[*] Установка NGROK..."
if [ ! -f "ngrok" ]; then
  wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.zip
  unzip ngrok-stable-linux-arm64.zip
  chmod +x ngrok
fi

echo "[*] Введите ваш NGROK токен (получить можно на https://dashboard.ngrok.com/get-started/your-authtoken):"
read NGROK_TOKEN
./ngrok authtoken $NGROK_TOKEN

echo "[*] Запуск NGROK TCP туннеля на порт 12345..."
./ngrok tcp 12345 > /dev/null &
sleep 3

NGROK_URL=$(curl -s http://127.0.0.1:4040/api/tunnels | grep -o 'tcp://[^"]*')
echo "[*] Ваш сервер доступен по адресу: $NGROK_URL"

echo "[*] Запуск сервера..."
python server.py
