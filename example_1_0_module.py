# Part 1, example 0: don't access modules or globals in __del__.
import sys

print(sys.version)


class C(object):
    def __del__(self):
        sys.stdout.write('foo\n')


z = C()
