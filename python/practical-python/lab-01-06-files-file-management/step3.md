# Common Idioms for Writing to a File

Write string data.

```python
with open('outfile', 'wt') as out:
    out.write('Hello World\n')
    ...
```

Redirect the print function.

```python
with open('outfile', 'wt') as out:
    print('Hello World', file=out)
    ...
```

These exercises depend on a file `Data/portfolio.csv`. The file contains a list of lines with information on a portfolio of stocks. It is assumed that you are working in the `practical-python/Work/` directory. If you're not sure, you can find out where Python thinks it's running by doing this:

```python
>>> import os
>>> os.getcwd()
'/Users/beazley/Desktop/practical-python/Work' # Output vary
>>>
```
