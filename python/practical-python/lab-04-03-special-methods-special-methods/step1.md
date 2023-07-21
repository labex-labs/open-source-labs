# Introduction

Classes may define special methods. These have special meaning to the
Python interpreter. They are always preceded and followed by
`__`. For example `__init__`.

```python
class Stock(object):
    def __init__(self):
        ...
    def __repr__(self):
        ...
```

There are dozens of special methods, but we will only look at a few specific examples.
