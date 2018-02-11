# Part 0, example 1: reference cycle delays __del__.
class C(object):
    def __del__(self):
        print('del')


def fn():
    d = {'c': C()}
    d['d'] = d  # Create a cycle.


fn()
print('shutting down')
