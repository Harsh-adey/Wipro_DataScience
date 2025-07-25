"""Write a program to accept two numbers as command line arguments 
and display their sum."""
import sys
def sum1(a,b):
    return a+b

a=int(sys.argv[1])
b=int(sys.argv[2])
print(sum1(a,b))

""" Write a program to accept a welcome message through command line
 arguments and display the file name along with the welcome message.
"""
import sys
def wel_fun(str1):
    return str1

arg = sys.argv[1]
name = sys.argv[0]
message = wel_fun(arg)
print(f"The file name is: {name}")
print(f"Welcome: {message}")

""" Write a program to accept 10 numbers through command line
 arguments and calculate the sum of prime numbers among them."""

import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


if len(sys.argv) != 11:
    print("Usage: python sum_primes.py num1 num2 num3 ... num10")
    sys.exit(1)

num = list(map(int, sys.argv[1:]))
prime_sum = sum(num for i in num if is_prime(num))
print("Sum of prime numbers:", prime_sum)
