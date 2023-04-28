# Delayed Function Execution

## Problem

Write a function `delay(fn, ms, *args)` that takes a function `fn`, a time in milliseconds `ms`, and any number of arguments `args`. The function should delay the execution of `fn` by `ms` milliseconds and then invoke it with the provided arguments. The function should return the result of invoking `fn`.

To delay the execution of `fn`, use the `time.sleep()` function. This function takes a number of seconds as an argument, so you will need to convert `ms` to seconds before passing it to `time.sleep()`.

## Example

```py
def add(x, y):
  return x + y

result = delay(add, 2000, 2, 3)
print(result) # Output: 5
```

In the example above, the `add` function is delayed by 2000 milliseconds (2 seconds) before being invoked with the arguments `2` and `3`. The result of the `add` function is then returned and printed to the console.
