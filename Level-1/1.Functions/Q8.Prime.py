import time
from functools import lru_cache


@lru_cache()
def find_prime_number(end):
    """"This method print prime num till the upper limit that is entered."""
    start_time = time.time()
    print("Prime Number that are in range are:", end=" ")
    for val in range(2, end+1):
        flag = 0
        for n in range(2, val):
            if (val % n) == 0:
                flag = 1
        if flag == 0:
            print(val, end=" ")
    print("\nTime taken: %s seconds" % (time.time() - start_time))


end = int(input("Enter the ending point: "))
find_prime_number(end)
