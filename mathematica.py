# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Iterative factorial
def factorial_iter(n):
    fact = 1
    for i in range(2,n+1):
        fact = fact * i
    return fact    

numero = int(input('Enter number'))
fact = factorial_iter(numero)
print(f'The factorial of {numero} is {fact}')

#Recursive factorial
def factorial_recur(n):
    if n <=1:
        return 1
    return n * factorial_recur(n - 1)

def fibbonacci_recur(n):
    if n <= 1:
        return n
    return fibbonacci_recur(n - 1) + fibbonacci_recur(n - 2)    