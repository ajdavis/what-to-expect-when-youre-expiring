# Part 1, example 2: don't take any locks. Deadlocks in PyPy as well as CPython.
import gc
import sys
import threading

print(sys.version)

lock = threading.Lock()


class C(object):
    def __del__(self):
        print('getting lock')
        with lock:
            print('doing cleanup task that requires lock')


c = C()
with lock:
    gc.collect()
    del c
