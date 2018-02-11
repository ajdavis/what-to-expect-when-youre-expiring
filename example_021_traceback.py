# Part 0, example 2.1: stored traceback delays __del__.
# Clear the local references to avoid reference cycle.
import sys
import traceback


class C(object):
    def __del__(self):
        print('del')


def fn():
    c = C()
    try:
        1 / 0
    except Exception:
        exc_type, exc_val, exc_tb = sys.exc_info()
        traceback.print_tb(exc_tb, file=sys.stdout)
        exc_type = exc_val = exc_tb = None


fn()
print('shutting down')
