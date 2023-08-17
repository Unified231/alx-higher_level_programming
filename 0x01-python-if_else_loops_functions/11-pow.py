#!/usr/bin/python3

def pow(a, b):
  result = 1
  while b > 0:
    if b % 2 == 1:
      result *= a
    b //= 2
    a *= a
  return result

