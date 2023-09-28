import math
"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    list = []

    def check_prime(n):
        prime = 1

        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                prime = 0
                break
            else:
                continue

        return prime

    counter = 0
    n = 2

    while counter < number_of_primes:
        if check_prime(n) == 1:
            list.append(n)
            counter += 1
        n += 1

    return list

c = 4
n = 6
[2,3,5]


print(primes(20))

#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                   # 53, 59, 61, 67, 71]
