# Part 1, example 0.1: don't access modules or globals in __del__.
# This example works by accident, because the global C is named "c" not "z".
import sys


class C(object):
    def __del__(self):
        sys.stdout.write('del\n')


c = C()
