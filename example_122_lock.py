# Part 1, example 2.2: don't take any locks. Use a cleanup thread.
import atexit
import threading
from time import sleep

lock = threading.Lock()
cleanup_tasks = []
exiting = False


class C(object):
    def __del__(self):
        print('del')
        cleanup_tasks.append('cleanup task that needs lock')


def cleanup():
    while not exiting:
        sleep(1)
        while True:
            try:
                task = cleanup_tasks.pop()
            except IndexError:
                break

            with lock:
                # Execute the cleanup task that needs lock.
                print(task)


thread = threading.Thread(target=cleanup)
thread.setDaemon(True)
thread.start()


def stop_cleanup_thread():
    global exiting
    exiting = True
    # Try for 10 seconds. Failure won't block shutdown: thread is daemonic.
    thread.join(10)


atexit.register(stop_cleanup_thread)

c = C()
with lock:
    c = None
