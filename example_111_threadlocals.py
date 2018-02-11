# Part 1, example 1: don't access threadlocals in __del__.
# In Python 2.6, this example leaks every second C object.
from time import sleep
import threading

local = threading.local()


class C(object):
    def __init__(self):
        print('init')

    def __del__(self):
        # Access "local" while it's being updated in "fn".
        local.x = 1
        print('del')


def fn():
    local.c = C()


for i in range(4):
    t = threading.Thread(target=fn)
    t.start()
    t.join()
    sleep(1)
