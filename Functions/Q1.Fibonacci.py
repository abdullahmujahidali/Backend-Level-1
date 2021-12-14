import time
from functools import lru_cache


@lru_cache(maxsize=1000)
def fibonacci_series(size):
    if size == 0:
        return 0
    if size == 1 or size == 2:
        return 1
    if size > 2:
        return fibonacci_series(size-1) + fibonacci_series(size-2)


size = int(input("Enter how many times you want to use the function: "))
for iterator in range(size):
    start_time = time.time()
    iteration = int(input("Enter a number to find the Fibonacci series : "))
    for i in range(iteration):
        a = fibonacci_series(i)
        print(a, end=" ")
    print("\nTime taken: %s seconds" % (time.time() - start_time))
    print("\n-----------------------\n")
