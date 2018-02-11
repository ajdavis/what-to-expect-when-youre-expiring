# Part 1, example 0.0: don't access modules or globals in __del__.
# "z" is destroyed after "sys" is set to None.
import sys


class C(object):
    def __del__(self):
        sys.stdout.write('del\n')


z = C()
