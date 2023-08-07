# Exercise 6.4: A Simple Generator

If you ever find yourself wanting to customize iteration, you should always think generator functions. They're easy to write---make a function that carries out the desired iteration logic and use `yield` to emit values.

For example, try this generator that searches a file for lines containing a matching substring:

```python
>>> def filematch(filename, substr):
        with open(filename, 'r') as f:
            for line in f:
                if substr in line:
                    yield line

>>> for line in open('Data/portfolio.csv'):
        print(line, end='')

name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
>>> for line in filematch('Data/portfolio.csv', 'IBM'):
        print(line, end='')

"IBM",50,91.10
"IBM",100,70.44
>>>
```

This is kind of interesting--the idea that you can hide a bunch of custom processing in a function and use it to feed a for-loop. The next example looks at a more unusual case.
