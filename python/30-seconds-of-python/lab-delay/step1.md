# Delayed Function Execution

Write a function `delay(fn, ms, *args)` that takes a function `fn`, a time in milliseconds `ms`, and any number of arguments `args`. The function should delay the execution of `fn` by `ms` milliseconds and then invoke it with the provided arguments. The function should return the result of invoking `fn`.

To delay the execution of `fn`, use the `time.sleep()` function. This function takes a number of seconds as an argument, so you will need to convert `ms` to seconds before passing it to `time.sleep()`.

```python
from time import sleep

def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)
```

```python
delay(lambda x: print(x), 1000, 'later') # prints 'later' after one second
```
