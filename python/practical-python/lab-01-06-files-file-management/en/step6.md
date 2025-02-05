# Exercise 1.28: Other kinds of "files"

What if you wanted to read a non-text file such as a gzip-compressed datafile? The builtin `open()` function won't help you here, but Python has a library module `gzip` that can read gzip compressed files.

Try it:

```python
>>> import gzip
>>> with gzip.open('portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')

... look at the output ...
>>>
```

Note: Including the file mode of `'rt'` is critical here. If you forget that, you'll get byte strings instead of normal text strings.
