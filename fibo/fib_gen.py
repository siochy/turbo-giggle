from lesson_2.decor.decor import decor


@decor
def fib_gen(count):
    """Generate Fibonacci sequence.
    Fibonacci numbers with loop and
    decorator that shows time of process,
    argument and type"""
    fib_num1 = 0
    fib_num2 = 1
    for i in range(count):
        fib_num1, fib_num2 = fib_num2, fib_num1 + fib_num2
        yield fib_num1
