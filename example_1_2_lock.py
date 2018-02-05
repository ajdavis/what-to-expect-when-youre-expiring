# Part 1, example 2: don't take any locks.
import sys
import threading

print(sys.version)

lock = threading.Lock()


class C(object):
    def __del__(self):
        print('getting lock')
        with lock:
            print('releasing lock')


c = C()
with lock:
    del c
