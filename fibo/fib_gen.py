from decor.decor import decor


@decor
def fib_gen(count):
    fib_num1 = 0
    fib_num2 = 1
    for i in range(count):
        fib_num1, fib_num2 = fib_num2, fib_num1 + fib_num2
        yield fib_num2
