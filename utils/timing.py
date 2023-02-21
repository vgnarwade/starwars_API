import time

def timeit(func):

    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time() - start

        print(f"Total time execution : {end}")

        return result
    return wrapper