# A coroutine example

Getting started with coroutines can be a little tricky. Here is an
example program that performs the same task as
[Exercise 8.2](ex8_2.md), but with coroutines. Take this program
and copy it into a file called `cofollow.py`.

```python
# cofollow.py
import os
import time

# Data source
def follow(filename,target):
    with open(filename,'r') as f:
        f.seek(0,os.SEEK_END)
        while True:
            line = f.readline()
            if line != '':
                target.send(line)
            else:
                time.sleep(0.1)

# Decorator for coroutine functions
from functools import wraps

def consumer(func):
    @wraps(func)
    def start(*args,**kwargs):
        f = func(*args,**kwargs)
        f.send(None)
        return f
    return start

# Sample coroutine
@consumer
def printer():
    while True:
        item = yield     # Receive an item sent to me
        print(item)

# Example use
if __name__ == '__main__':
    follow('stocklog.csv',printer())
```

Run this program and make sure produces output.. Make sure you understand how the different pieces are hooked together.
