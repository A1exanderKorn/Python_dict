import math


def foo_0(x):
    if(x[4] == 1992):
        return 8
    if(x[4] == 2004):
        return foo_0_1(x)
    else:
        return foo_0_0(x)


def foo_0_0(x):
    if(x[3] == 'GRACE'):
        return 4
    if(x[3] == 'JSON'):
        return foo_0_0_1(x)
    else:
        return foo_0_0_0(x)


def foo_0_0_0(x):
    if(x[0] == 2002):
        return 0
    else:
        return foo_0_0_0_0(x)


def foo_0_0_0_0(x):
    if(x[1] == 1970):
        return 1
    if(x[1] == 1983):
        return 2
    else:
        return 3


def foo_0_0_1(x):
    if(x[2] == 'RHTML'):
        return 5
    if(x[2] == 'DYLAN'):
        return 6
    else:
        return 7


def foo_0_1(x):
    if(x[1] == 1970):
        return 9
    if(x[1] == 1983):
        return 10
    if(x[1] == 1979):
        return 11


def main(n):
    return foo_0(n)
