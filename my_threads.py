import time
import threading


def a(msg):
    while True:
        print(f'a--{msg}')
        time.sleep(1)


def b(msg):
    while True:
        print(f'b--{msg}')
        time.sleep(1)


ta = threading.Thread(target=a, args={111})
tb = threading.Thread(target=b, kwargs={'msg': 222})

ta.start()
tb.start()
