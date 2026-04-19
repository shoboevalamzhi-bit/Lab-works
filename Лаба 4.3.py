from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_cache(n):
    if n < 0:
        raise ValueError("Число должно быть неотрицательным")
    if n <= 1:
        return n
    return fibonacci_cache(n-1) + fibonacci_cache(n-2)

print(fibonacci_cache(int(input()))) # в задание мой вариант 23 так что я выбрал 3 вариант (f(12)) - ответ: 144