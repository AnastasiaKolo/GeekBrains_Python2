# 1. Реализовать простое клиент-серверное взаимодействие
# по протоколу JIM (JSON instant messaging):
# клиент отправляет запрос серверу;
# сервер отвечает соответствующим кодом результата.
# Клиент и сервер должны быть реализованы в виде
# отдельных скриптов, содержащих соответствующие функции.
# Функции клиента: сформировать presence-сообщение;
# отправить сообщение серверу;
# получить ответ сервера;
# разобрать сообщение сервера;
# параметры командной строки скрипта
# client.py <addr> [<port>]:
# addr — ip-адрес сервера;
# port — tcp-порт на сервере, по умолчанию 7777.

from socket import *
import time

port = 7777
host = 'localhost'
s = socket(AF_INET, SOCK_STREAM)
try:
    s.connect((host, port))
except ConnectionRefusedError:
    print("Сервер %s недоступен по порту %s" % (host, port))
msg = 'Привет, сервер'
s.send(msg.encode('utf-8'))
data = s.recv(1000000)
print("Сообщение от сервера: ", data.decode('utf-8'), ' длиной ', len(data), ' байт')
msg = 'ЙЦУКЕНГШЩЩ'
s.send(msg.encode('utf-8'))
data = s.recv(1000000)
print("Сообщение от сервера: ", data.decode('utf-8'), ' длиной ', len(data), ' байт')

# в цикле
for i in range(5):
    s.send(msg.encode('utf-8'))
    data = s.recv(1000000)
    print("Сообщение от сервера: ", data.decode('utf-8'), ' длиной ', len(data), ' байт')
    time.sleep(i)
s.close()
