# Sum of powers

Write a Python function called `sum_of_powers` that takes in three parameters:

- `end` - an integer representing the end of the range (inclusive)
- `power` - an integer representing the power to which each number in the range should be raised (default value is 2)
- `start` - an integer representing the start of the range (default value is 1)

The function should return the sum of the powers of all the numbers from `start` to `end` (both inclusive).

To solve this problem, you can follow these steps:

1. Use `range()` in combination with a list comprehension to create a list of elements in the desired range raised to the given `power`.
2. Use `sum()` to add the values together.

```python
def sum_of_powers(end, power = 2, start = 1):
  return sum([(i) ** power for i in range(start, end + 1)])
```

```python
sum_of_powers(10) # 385
sum_of_powers(10, 3) # 3025
sum_of_powers(10, 3, 5) # 2925
```
