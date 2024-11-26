# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def factorial(n):
    fact = 1
    for i in range(2,n+1):
        fact = fact * i
    return fact    

numero = int(input('Enter number'))
fact = factorial(numero)
print(f'The factorial of {numero} is {fact}')