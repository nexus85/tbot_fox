import functools


def add_n(n):
    def decorator(f):
        @functools.wraps(f)
        def wraper(*args, **kwargs):
            result = f(*args, **kwargs)
            return result + n
        return wraper
    return decorator()



@add_n(2)
def my_sum(a,b):
    return a + b


my_sum(1,2)