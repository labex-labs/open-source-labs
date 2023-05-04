# Check if a Number is Odd

Write a function called `is_odd` that takes a single integer as an argument and returns `True` if the number is odd, and `False` if the number is even. Your function should perform the following steps:

1. Use the modulo (`%`) operator to check whether the number is even or odd.
2. If the number is odd, return `True`. If the number is even, return `False`.

```py
def is_odd(num):
  return num % 2 != 0
```

```py
is_odd(3) # True
```
