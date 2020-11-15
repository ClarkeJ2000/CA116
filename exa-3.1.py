#!/usr/bin/env python


n = input()
a = '*' + (n * '*') + '*'
b = '*' + ((n / 2) * ' ') + '*' + ((n / 2) * ' ') + '*' + '\n'

p = (n / 2) * b

print a
print (n / 2) * b
print a
print (n / 2) * b - 1
print b
print a
