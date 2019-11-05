# https://projecteuler.net/problem=10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

#TODO Runtime takes too long. Fix that
def is_prime_number(x):
    for y in range(2, x):
        if not (x % y):
            return False
    return True


sum = 2
count = 1
prime_num = 3
while True:
    if is_prime_number(prime_num):
        if not prime_num < 2000000:
            break
        print(prime_num)
        sum = sum + prime_num
    prime_num = prime_num + 2
print(sum)