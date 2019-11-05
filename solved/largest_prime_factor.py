# https://projecteuler.net/problem=3

# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

possible_primes = []
num = 600851475143


def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True


def factor_out_prime(x, bignum):
    while True:
        if bignum % x != 0:
            return bignum
        bignum = bignum / x


count = 2
while True:
    if count > num:
        break
    if num % count == 0 and is_prime_number(count):
        possible_primes.append(count)
        num = factor_out_prime(count, num)
    count = count + 1

print(possible_primes)
print(max(possible_primes))

