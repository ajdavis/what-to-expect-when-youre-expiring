# Part 1, example 1.0: don't access threadlocals in __del__.
# This example works fine.
from time import sleep
import threading

local = threading.local()


class C(object):
    def __init__(self):
        print('init')

    def __del__(self):
        print('del')


def fn():
    local.c = C()


for i in range(4):
    t = threading.Thread(target=fn)
    t.start()
    t.join()
    sleep(1)
