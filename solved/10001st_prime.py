# https://projecteuler.net/problem=7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

print("starting...")


def is_prime_number(x):
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return False
    else:
        return False
    return True


prime_count = 1
prime_num = 2
while True:
    if is_prime_number(prime_num):
        if prime_count == 10001:    # Change this number if you want to find a different prime number
            break
        prime_count = prime_count + 1
    prime_num = prime_num + 1
print(prime_num)
