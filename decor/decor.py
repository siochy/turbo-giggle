import time


def decor(func):
    """Decorator that shows name, argument, type and result of function."""
    def insider(arg):
        start_func = time.time()
        end_func = time.time()
        func_time = start_func - end_func
        message = f'''Function {str(func.__name__)} is running by argument {arg}
                    with time {func_time}s
                    and resulting type {str(type(func(arg)))}
                    Result:
                    {list(func(arg))}'''
        return message
    return insider
