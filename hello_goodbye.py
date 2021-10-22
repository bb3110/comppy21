#hello_goodbye.py
import time


def hello():
    time.sleep(1)
    print("Hello")


@profile
def goodbye():
    time.sleep(2)
    print("Goodbye")


@profile
def main():
    hello()
    goodbye()


if __name__ == "__main__":
    main()
