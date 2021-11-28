import time


class TimePrinter:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()

        print(self.end - self.start)



with TimePrinter():
    print('test')
print('after')

