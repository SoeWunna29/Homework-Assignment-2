def g(x):
    return x


def f(x):
    return x


def intsct(f, x):
    g(x)
    if f(x) == g(x):
        return True
    else:
        return False


print(intsct(f, 10))
