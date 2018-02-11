# Part 1, example 2.1: don't take any locks.
# Deadlocks in PyPy as well as CPython.
import gc
import threading

lock = threading.Lock()


class C(object):
    def __del__(self):
        print('getting lock')
        with lock:
            print('cleanup task that needs lock')


c = C()
with lock:
    c = None
    gc.collect()
