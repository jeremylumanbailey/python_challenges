# https://projecteuler.net/problem=10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.


# TODO Works but runtime takes over a minute
def is_prime_number(primeList,x):
    for i in primeList:
        if x % i == 0:
            return False
    return True


listSum = [2]
prime_num = 3

while True:
    if is_prime_number(listSum, prime_num):
        if not prime_num < 2000000:
            break
        listSum.append(prime_num)
    prime_num = prime_num + 2
sum = sum(listSum)
print(sum)
