def eat():
    return 'eaten'


def inc(x):
    return x + 1


def set_func():
    return set("1234")


def zero_division(x):
    return 1 / x


def raise_exc():
    raise SystemExit(1)  # raises SystemExit(1) exception


def match_func():
    raise ValueError("Exception 123 raised")


if __name__ == "__main__":
    eat()
    print(inc(4))
