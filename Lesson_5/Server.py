# -*- coding: utf8 -*-
# Для проекта «Мессенджер» реализовать логирование с использованием модуля logging:
# 1. В директории проекта создать каталог log, в котором для клиентской и серверной сторон
#    в отдельных модулях формата client_log_config.py и server_log_config.py создать логгеры;
# 2. В каждом модуле выполнить настройку соответствующего логгера по следующему алгоритму:
# -  Создание именованного логгера;
# -  Сообщения лога должны иметь следующий формат: "<дата-время> <уровень_важности> <имя_модуля> <сообщение>";
# -  Журналирование должно производиться в лог-файл;
# -  На стороне сервера необходимо настроить ежедневную ротацию лог-файлов.
# 3. Реализовать применение созданных логгеров для решения двух задач:
# -  Журналирование обработки исключений try/except. Вместо функции print() использовать журналирование и
#    обеспечить вывод служебных сообщений в лог-файл;
# -  Журналирование функций, исполняемых на серверной и клиентской сторонах при работе мессенджера.

from socket import *
import time
import json
import argparse


def server_response(client_msg, client):
    json_resp = {}
    if client_msg["action"] == 'presence':
        json_resp = {
            "response": 200,
            "time": time.time(),
            "alert": "Подтрерждаю"
        }
    elif client_msg["action"] == 'msg':
        json_resp = {
            "response": 200,
            "time": time.time(),
            "alert": "Сообщение отправлено пользователю " + client_msg["to"]
        }
    msg = json.dumps(json_resp)
    client.send(msg.encode('utf-8'))
    client.close()


def recv_message(client, addr):
    data = client.recv(1024)
    print("Сообщение", data.decode('utf-8'), ", было отправлено клиентом: %s" % str(addr))
    json_mess = {}
    try:
        json_mess = json.loads(data.decode('utf-8'))
        print("Сообщение",
              "Action",  json_mess["action"],
              ' длиной ', len(data), ' байт')
    except json.decoder.JSONDecodeError:
        print("Сообщение от клиента не распознано", data)
    return json_mess


def server_communicate(s: socket):
    client, addr = s.accept()
    print("Получен запрос на соединение от %s" % str(addr))
    msg_from_client = recv_message(client, addr)
    server_response(msg_from_client, client)


def parse_args():
    parser = argparse.ArgumentParser(description='Server App')
    parser.add_argument("-p", action="store", dest="port", type=int, default=7777,
                        help="enter port number, default is 7777")
    parser.add_argument("-a", action="store", dest="addr", type=str, default='0.0.0.0',
                        help="enter IP address, default is 0.0.0.0")
    return parser.parse_args()


def main():
    args = parse_args()
    port = args.port
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', port))
    s.listen(5)
    print("Запущено прослушивание порта %s" % str(port))
    while True:
        server_communicate(s)


# Entry point
if __name__ == '__main__':
    main()