# -*- coding: utf8 -*-
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
import argparse
import json


def presence():  # сформировать presence-сообщение;
    pass


def send_message():  # отправить сообщение серверу;
    pass


def get_response():  # получить ответ сервера;
    pass


def parse_message():  # разобрать сообщение сервера;
    pass


# получить и обработать параметры командной строки
def parse_args():
    parser = argparse.ArgumentParser(description='Client App')
    parser.add_argument("-a", action="store", dest="addr", type=str, default='localhost',
                        help="enter IP address, default is localhost")
    parser.add_argument("-p", action="store", dest="port", type=int, default=7777,
                        help="enter port number, default is 7777")
    return parser.parse_args()


def main():
    args = parse_args()
    port = args.port
    host = args.addr
    print("Попытка соединения с %s по порту %s" % (host, port))
    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.connect((host, port))
    except ConnectionRefusedError:
        print("Сервер %s недоступен по порту %s" % (host, port))
    msg = 'Привет, сервер'
    s.send(msg.encode('utf-8'))
    data = s.recv(1024)
    print("Сообщение от сервера: ", data.decode('utf-8'), ' длиной ', len(data), ' байт')
    # в цикле
    for i in range(5):
        msg = 'Попытка ' + str(i)
        s.send(msg.encode('utf-8'))
        data = s.recv(1024)
        print("Сообщение от сервера: ", data.decode('utf-8'), ' длиной ', len(data), ' байт')
        time.sleep(i)
    s.close()


# Entry point
if __name__ == '__main__':
    main()
