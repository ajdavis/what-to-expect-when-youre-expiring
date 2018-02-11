# Part 1, example 2.3: don't take any locks. Use a cleanup thread.
# Proves even PyPy can use this technique, eventually.
import atexit
import gc
import threading
from time import sleep

lock = threading.Lock()


class C(object):
    def __del__(self):
        print('del')
        cleanup_tasks.append('cleanup task that needs lock')


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
    gc.collect()
    exiting = True
    # Try for 10 seconds. Failure won't block shutdown: thread is daemonic.
    thread.join(10)


atexit.register(stop_cleanup_thread)

c = C()
with lock:
    c = None
