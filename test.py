import state_objects as so


def bin_(x):
    return bin(x).split("0b")[1]


def print_(x, y, o):
    if o:
        print(f"{x} or {y}", x or y, bool(x or y), bin_(x), bin_(y), bin_(x or y), sep="\t\t\t\t")
    else:
        print(f"{x} |  {y}", x | y, bool(x | y), bin_(x), bin_(y), bin_(x | y), sep="\t\t\t\t")


def foo(x, y, z):
    print(x + y + z)


if __name__ == "__main__":
    print(([0] * 5 + [180] * 5) * 4)
    print_(0, 0, True)
    print_(0, 4, True)
    print_(3, 0, True)
    print_(3, 4, True)
    print_(0, 0, False)
    print_(0, 4, False)
    print_(3, 0, False)
    print_(3, 4, False)
    print(str(False).lower(), str(True).lower())
    list_a = [1, 2, 3, 4]
    list_b = list_a.copy()
    list_b.reverse()
    print(list_a, list_b)
    x_ = [so.ss(so.cm[i], [so.bla]) for i in range(4)]
    print(x_, "\n", [x_[0][0], x_[1][0], x_[2][0], x_[3][0], x_[0][1], x_[1][1], x_[2][1], x_[3][1]])
    print("" or "Hello")
    print(None or "World")
    if None:
        print("None is true")
    else:
        print("None is false")
    val = None
    dict_ = {"lol": "no"}
    if val:
        dict_["k"] = val
    print(dict_)
    v = ["999", "888", "777"]
    vc = v.copy()
    for i in range(len(vc)):
        vc[i] = f"{vc[i]}_alt"
    print(v)
    print(vc)
    p1 = [2, 5, 9]
    p2 = [3, 4]
    foo(*p1)
    foo(1, *p2)
    foo(*p2, 6)
    p3 = [*p2, 22]
    foo(*p3)

    r_1 = None or None
    print(r_1)
    r_2 = 1 or 2
    print(r_2)
    r_3 = 71 | 99
    print(r_3)
    r_4 = 71 & 99
    print(r_4)
