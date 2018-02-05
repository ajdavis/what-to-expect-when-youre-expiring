# Part 0, example 2: stored traceback delays __del__.
import sys
import traceback


print(sys.version)


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
        #exc_type = exc_val = exc_tb = None


fn()
print('after fn')
