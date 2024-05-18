#!/usr/bin/python3
"""minimum operations"""
def minOperations(n):
  if n == 1:
    return 0
  elif n % 2 == 0:
    return minOperations(n//2) + 1
  else:
    return min(minOperations(n-1), minOperations(n+1)) + 1
print(minOperations(9))
