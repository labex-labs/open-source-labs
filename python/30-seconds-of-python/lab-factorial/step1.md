# Factorial

Write a function `factorial(num)` that takes a non-negative integer `num` as an argument and returns its factorial. The function should use recursion to calculate the factorial. If `num` is less than or equal to `1`, return `1`. Otherwise, return the product of `num` and the factorial of `num - 1`. The function should throw an exception if `num` is a negative or a floating-point number.

```py
def factorial(num):
  if not ((num >= 0) and (num % 1 == 0)):
    raise Exception("Number can't be floating point or negative.")
  return 1 if num == 0 else num * factorial(num - 1)
```

```py
factorial(6) # 720
```
