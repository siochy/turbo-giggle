class FibIter:

    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0
        self.fib_num1 = 0
        self.fib_num2 = 1

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            self.fib_num1, self.fib_num2 = self.fib_num2, self.fib_num1 + self.fib_num2
            return self.fib_num2
        else:
            raise StopIteration
