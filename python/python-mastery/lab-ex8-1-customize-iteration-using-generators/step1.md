# A Simple Generator

If you ever find yourself wanting to customize iteration, you should always think generator functions. They're easy to write---simply make a function that carries out the desired iteration logic and uses `yield` to emit values.

For example, try this generator that allows you to iterate over a range of numbers with fractional steps (something not supported by the `range()` builtin):

```python
>>> def frange(start,stop,step):
        while start < stop:
            yield start
            start += step

>>> for x in frange(0, 2, 0.25):
        print(x, end=' ')

0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
>>>
```

Iterating on a generator is a one-time operation. For example, here's what happen if you try to iterate twice:

```python
>>> f = frange(0, 2, 0.25)
>>> for x in f:
        print(x, end=' ')

0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
>>> for x in f:
        print(x, end=' ')

>>>
```

If you want to iterate over the same sequence, you need to recreate the generator by calling `frange()` again. Alternative, you could package everything into a class:

```python
>>> class FRange:
        def __init__(self, start, stop, step):
            self.start = start
            self.stop = stop
            self.step = step
        def __iter__(self):
            n = self.start
            while n < self.stop:
                yield n
                n += self.step

>>> f = FRange(0, 2, 0.25)
>>> for x in f:
        print(x, end=' ')

0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
>>> for x in f:
        print(x, end=' ')

0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
>>>
```
