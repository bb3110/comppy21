import sys

CONST = 2


def square(x):
    x2 = CONST * x * x
    return x2

def cube(x):
    x3 = CONST * x ** 3
    return x3



if __name__ == "__main__":
    x = int(sys.argv[1])
    print(square(x))
