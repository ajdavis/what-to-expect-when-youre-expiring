# Part 0, example 0: deleted right away (in CPython).
class C(object):
    def __del__(self):
        print('del')


def fn():
    c = C()


fn()
print('after fn')
