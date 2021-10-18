import sys

CONST = 2


def square(x, c=CONST):
    x2 = c * x * x
    return x2

def cube(x, const=CONST):
    x3 = const * x ** 3
    return x3



if __name__ == "__main__":
    if len(sys.argv) > 1:
        x = int(sys.argv[1])
        print(square(x))
        print(square(x, c=4))
    else:
        print("Usage: python mymath.py arg")
