# Part 1, example 2.0: don't take any locks.
# This deadlocks in CPython.
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
