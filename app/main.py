def eat():
    return 'eaten'


def inc(x):
    return x + 1


def raise_exc():
    raise SystemExit(1)  # raises SystemExit(1) exception


def zero_division(x):
    return 1 / x


if __name__ == "__main__":
    eat()
    print(inc(4))
