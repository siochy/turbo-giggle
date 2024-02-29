import time


def decor(func):
    def insider(arg):
        start_func = time.time()
        func(arg)
        end_func = time.time()
        func_time = start_func - end_func
        print(f'''Function {str(func.__name__)} is running by argument {arg}
with time {func_time}s
and resulting type {str(type(func(arg)))}''')
        return func(arg)
    return insider
