# Check if a Number is Even

Write a function `is_even(num)` that takes in a number as an argument and returns `True` if the number is even and `False` if the number is odd. To check whether a number is even or odd, you can use the modulo (`%`) operator. If a number is even, it will have no remainder when divided by 2. If a number is odd, it will have a remainder of 1 when divided by 2.

```python
def is_even(num):
  return num % 2 == 0
```

```python
is_even(3) # False
```
