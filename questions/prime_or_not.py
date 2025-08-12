import math

input = 7


def isprime(num):
    if num <= 1:
        return False
    # for i in range(2, num):
    for i in range(2, int(math.sqrt(num) + 1)):
        print(i)
        if num % i == 0:
            return False
    return True


print(isprime(input))
