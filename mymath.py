import sys

CONST = 2


def square(x):
    x2 = CONST * x * x
    return x2


if __name__ == "__main__":
    # print(sys.argv)
    x = int(sys.argv[1])
    print(square(x))
