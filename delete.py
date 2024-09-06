#!/usr/bin/python3

def print_numbers(n):
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

def print_numbers_reversed(n):
    for i in range(n, 0, -1):
        print(i, end=" ")
    print()

def print_even_numbers(n):
    for i in range(0, n + 1, 2):
        print(i, end=" ")
    print()

# 1 + 2 + 3 + ... + n
def sum(n):
    result = 0
    for i in range(1, n + 1):
        result = result + i
    return result

# 1 * 2 * 3 * ... * n
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


def sum_of_digits(n):
    """
        Function takes as argument n
        and return the sum of digits
        Example: n = 413, function should return
        8 because 4 + 1 + 3 = 8
    """
    if n < 0:
        n = -n
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total


print(sum_of_digits(-123))