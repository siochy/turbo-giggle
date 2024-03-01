from random import randint
from fibo.fib_gen import fib_gen
from fibo.fib_iter import FibIter
from decor.decor import decor
from cronos import cronos


def show_fib():
    """Shows list of fibonacci with random number with showing info
    about time, number in generator, name and type of it."""
    num_random = randint(1, 50)
    fibo = list(fib_gen(num_random))
    for number in fibo:
        print(number)


if __name__ == '__main__':
    show_fib()
