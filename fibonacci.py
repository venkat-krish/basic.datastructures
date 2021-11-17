# Method 1: using memoization
from typing import Dict, Generator
from functools import lru_cache

memo: Dict[int, int] = {0: 0, 1: 1}


# Define the fibonacci method
def fib(n):
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


# Method 2: Use inbuilt memoization, LRU cache-Least Recently Used
@lru_cache(maxsize=1000)
def fib1(n):
    if n < 2:  # Base case, return the same n
        return n
    return fib1(n - 1) + fib1(n - 2)  # recursive case


# Method 3: Simple performant solution
def fib2(n: int) -> int:
    if n == 0: return n # special case
    last: int = 0 # initially set to fib(0)
    next: int = 1 # initially set to fib(1)

    for _ in range(1, n):
        last, next = next, last + next
    return next

# Method 4: Generator approach
def fib3(n : int) -> Generator[int, None, None]:
    yield 0 # special case
    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next # Main generation step


if __name__ == '__main__':
    # print(fib(50))
    # print(fib1(50))
    # print(fib2(20))
    for i in fib3(50):
        print(i)
