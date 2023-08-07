# Introduction

Consider the following function.

```python
def add(x, y):
    def do_add():
        print('Adding', x, y)
        return x + y
    return do_add
```

This is a function that returns another function.

```python
>>> a = add(3,4)
>>> a
<function do_add at 0x6a670>
>>> a()
Adding 3 4
7
```
