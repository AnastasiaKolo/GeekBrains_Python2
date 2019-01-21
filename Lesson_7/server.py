# -*- coding: utf8 -*-
# Продолжаем работу над проектом «Мессенджер»:
# Реализовать обработку нескольких клиентов на сервере, используя функцию select.
# Клиенты должны общаться в «общем чате»: каждое сообщение участника отправляется всем,
# подключенным к серверу.
# Реализовать функции отправки/приема данных на стороне клиента. Чтобы упростить разработку
# на данном этапе, пусть клиентское приложение будет либо только принимать, либо только
# отправлять сообщения в общий чат. Эти функции надо реализовать в рамках отдельных скриптов.


from socket import *
import time
import json
import argparse
import logging
import server_log_config

serv_log = logging.getLogger('server')





def recv_message(client, addr):
    data = client.recv(1024)
    serv_log.info("Сообщение %s было отправлено клиентом: %s" % (data.decode('utf-8'), str(addr)))
    json_mess = {}
    try:
        json_mess = json.loads(data.decode('utf-8'))
        serv_log.info("Сообщение: Action=%s длиной %s байт" % (str(json_mess["action"]),
                                                               str(len(data))))
    except json.decoder.JSONDecodeError:
        serv_log.critical("Сообщение от клиента не распознано %s" % data.decode('utf-8'))
    return json_mess


def server_communicate(s: socket):
    client, addr = s.accept()
    serv_log.info("Получен запрос на соединение от %s" % str(addr))
    msg_from_client = recv_message(client, addr)
    server_response(msg_from_client, client)


def server_response(incoming_msg):
    # парсим сообщение клиента и формируем ответ сервера
    # ответ сервера будет выслан всем
    # ответ вида:
    # presense = клиент ... вошел в чат
    # msg = сообщение от клиента ...
    try:
        client_msg = json.loads(incoming_msg.decode('utf-8'))
        serv_log.info("Сообщение: Action=%s длиной %s байт" % (str(client_msg["action"]),
                                                               str(len(incoming_msg))))
    except json.decoder.JSONDecodeError:
        serv_log.critical("Сообщение от клиента не распознано %s" % incoming_msg.decode('utf-8'))


    json_resp = {}
    if client_msg["action"] == 'presence':
        json_resp = {
            "response": 200,
            "time": time.time(),
            "alert": "Подтверждаю"
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


def read_requests(r_clients, all_clients):
    # Чтение запросов из списка клиентов
    # может быть сообщение о входе в чат (presense)
    # или текстовое сообщение всем в чате
    requests = {}      # Словарь запросов от клиентов  вида {сокет: запрос}
    for sock in r_clients:
        try:
            data = sock.recv(1024).decode('ascii')
            requests[sock] = data
            print("sock = ", sock)
            print("requests[sock] = ", requests[sock])
        except:
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)
    return requests


def write_responses(requests, w_clients, all_clients):
    # ответ сервера клиентам, от которых были запросы
    for sock in w_clients:
        if sock in requests:
            try:
                # Подготовить и отправить ответ сервера
                resp = requests[sock].encode('ascii')
                # Эхо-ответ сделаем чуть непохожим на оригинал
                test_len = sock.send(resp.upper())
            except:                 # Сокет недоступен, клиент отключился
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                all_clients.remove(sock)


def parse_args():
    parser = argparse.ArgumentParser(description='Server App')
    parser.add_argument("-p", action="store", dest="port", type=int, default=7777,
                        help="enter port number, default is 7777")
    parser.add_argument("-a", action="store", dest="addr", type=str, default='0.0.0.0',
                        help="enter IP address, default is 0.0.0.0")
    return parser.parse_args()


def mainloop():
    #Основной цикл обработки запросов клиентов
    args = parse_args()
    port = args.port
    clients = []
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', port))
    s.listen(5)
    s.settimeout(0.2)  # Таймаут для операций с сокетом
    serv_log.info("Запущено прослушивание порта %s" % str(port))
    # while True:
    #     server_communicate(s)
    while True:
        try:
            conn, addr = s.accept()  # Проверка подключений
        except OSError as e:
            pass  # timeout вышел
        else:
            print("Получен запрос на соединение от %s" % str(addr))
            clients.append(conn)
        finally:
            # Проверить наличие событий ввода-вывода
            wait = 0
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass  # Ничего не делать, если какой-то клиент отключился

            requests = read_requests(r, clients)  # Сохраним запросы клиентов
            write_responses(requests, w, clients)  # Выполним отправку ответов клиентам


# Entry point
if __name__ == '__main__':
    mainloop()
