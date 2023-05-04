# Average 

Write a function called `average` that takes in two or more numbers and returns their average. Your function should follow these guidelines:

- Use `sum()` to sum all of the `args` provided, divide by `len()`.
- The function should be able to handle any number of arguments.
- The function should return a float.

```py
def average(*args):
  return sum(args, 0.0) / len(args)
```

```py
average(*[1, 2, 3]) # 2.0
average(1, 2, 3) # 2.0
```
