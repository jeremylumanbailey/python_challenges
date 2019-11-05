# https://projecteuler.net/problem=5
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def evenly_divisible(x):
    for i in range(1, 21):
        if x % i == 0:
            continue
        else:
            return False
    return True

num = 40

while True:
    if evenly_divisible(num):
        print()
        print("smallest positive number is", num)
        break
    # print(num)
    num = num + 20