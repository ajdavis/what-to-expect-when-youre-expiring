# Part 0, example 0: deleted right away (in CPython).
import sys

print(sys.version)


class C(object):
    def __del__(self):
        print('del')


def fn():
    c = C()


fn()
print('after fn')
