# Part 1, example 1: don't access threadlocals in __del__.
import sys
from time import sleep
import threading

print(sys.version)

local = threading.local()


class C(object):
    def __init__(self):
        print('init')

    def __del__(self):
        local.x = 1
        print('del')


def fn():
    local.c = C()


for i in range(10):
    t = threading.Thread(target=fn)
    t.start()
    t.join()
    sleep(1)
