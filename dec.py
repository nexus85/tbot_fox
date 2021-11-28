import time

def timer(f):
    def wrapper():
        start = time.time()
        f()
        end = time.time()
        print(end-start)
    return wrapper





@timer
def long():
    for val in range(50000000):
        a = val * 2



long()

