# Функции сервера:
# принимает сообщение клиента;
# формирует ответ клиенту;
# отправляет ответ клиенту;
# имеет параметры командной строки:
# -p <port> — TCP-порт для работы
# (по умолчанию использует 7777);
# -a <addr> — IP-адрес для прослушивания
# (по умолчанию слушает все доступные адреса).

from socket import *
import time
import json

port = 7777
s = socket(AF_INET, SOCK_STREAM)
s.bind(('' , port))
s.listen( 5 )

while True:
    client, addr = s.accept()
    print("Получен запрос на соединение от %s" % str(addr))
    data = client.recv(1000000)
    print("Сообщение", data.decode('utf-8'), ", было отправлено клиентом: %s" % str(addr))
    msg = "Привет ! Время "+ time.ctime(time.time())
    client.send(msg.encode('utf-8'))
    client.close()