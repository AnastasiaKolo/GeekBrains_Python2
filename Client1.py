from socket import *
import time


s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8888))
tm = s.recv(1024)
s.close()
print("Текущее время: %s" % tm.decode('ascii'))
# в цикле
for i in range(5):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 8888))
    tm = s.recv(1024)
    s.close()
    print("Текущее время: %s" % tm.decode('ascii'))
    time.sleep(i)