#!/usr/bin/python
"""Print all possible different combinations of two digits in ascending order.
	The two digits must be different - 01 and 10 are considered identical."""
for i in range(1, 10):
  for j in range(i + 1, 10):
    if i != j:
      print(i, j, end=", ")
print()

