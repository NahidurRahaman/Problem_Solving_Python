from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n: int):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(50))  
