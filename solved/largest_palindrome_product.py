# https://projecteuler.net/problem=4
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

digit = 999
second_digit = 999
palindromes = []


def is_palindrome(number):
    # Calling reverse function
    s = str(number)
    rev = s[::-1]

    # Checking if both string are equal or not
    if s == rev:
        return True
    return False


# TODO show what two 3-digit numbers actually create the largest palindrome. Probably could change it so that it only
# returns the max in temp_list
def compute_palindrome(num, constant):
    temp_list = []
    for x in range(num, 1, -1):
            if is_palindrome(x * constant):
                temp_list.append(x * constant)
                break
    return temp_list


while True:
    if second_digit == 0:
        break
    palindromes.extend(compute_palindrome(digit, second_digit))
    second_digit = second_digit - 1

print(max(palindromes))
