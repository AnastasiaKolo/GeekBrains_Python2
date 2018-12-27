# -*- coding: utf8 -*-
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
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Server App')
    parser.add_argument("-p", action="store", dest="port", type=int, default=7777,
                        help="enter port number, default is 7777")
    parser.add_argument("-a", action="store", dest="addr", type=str, default='*',
                        help="enter IP address, default is *")
    return parser.parse_args()

def main():
    args = parse_args()
    port = args.port
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', port))
    s.listen(5)
    print("Запущено прослушивание порта %s" % str(port))
    while True:
        client, addr = s.accept()
        print("Получен запрос на соединение от %s" % str(addr))
        while True:
            data = client.recv(1024)
            print("Сообщение", data.decode('utf-8'), ", было отправлено клиентом: %s" % str(addr))
            msg = "Время "+ time.ctime(time.time())
            client.send(msg.encode('utf-8'))
        client.close()



# Entry point
if __name__ == '__main__':
    main()