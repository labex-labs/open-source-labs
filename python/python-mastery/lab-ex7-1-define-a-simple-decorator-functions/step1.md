# Your First Decorator

To start with decorators, write a _very_ simple decorator function that simply prints out a message each time a function is called. Create a file `logcall.py` and define the following function:

```python
# logcall.py

def logged(func):
    print('Adding logging to', func.__name__)
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

Now, make a separate file `sample.py` and apply it to a few function definitions:

```python
# sample.py

from logcall import logged

@logged
def add(x,y):
    return x+y

@logged
def sub(x,y):
    return x-y
```

Test your code as follows:

```python
>>> import sample
Adding logging to add
Adding logging to sub
>>> sample.add(3,4)
Calling add
7
>>> sample.sub(2,3)
Calling sub
-1
>>>
```
