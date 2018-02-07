# Part 1, example 2: don't take any locks. Use a cleanup thread.
import atexit
import gc
import sys
import threading
from time import sleep

print(sys.version)

lock = threading.Lock()


class C(object):
    def __del__(self):
        print('getting lock')
        cleanup_tasks.append('doing cleanup task that requires lock')


exiting = False
cleanup_tasks = []


def cleanup():
    while not exiting:
        sleep(1)
        while True:
            try:
                task = cleanup_tasks.pop()
            except IndexError:
                break

            with lock:
                print(task)


thread = threading.Thread(target=cleanup)
thread.setDaemon(True)
thread.start()


def stop_cleanup_thread():
    global exiting
    exiting = True
    thread.join(10)  # Try for 10 seconds.


atexit.register(stop_cleanup_thread)

c = C()
with lock:
    del c
