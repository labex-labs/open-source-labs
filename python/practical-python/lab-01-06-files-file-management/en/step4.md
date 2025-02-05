# Exercise 1.26: File Preliminaries

First, try reading the entire file all at once as a big string:

```python
>>> with open('portfolio.csv', 'rt') as f:
        data = f.read()

>>> data
'name,shares,price\n"AA",100,32.20\n"IBM",50,91.10\n"CAT",150,83.44\n"MSFT",200,51.23\n"GE",95,40.37\n"MSFT",50,65.10\n"IBM",100,70.44\n'
>>> print(data)
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
>>>
```

In the above example, it should be noted that Python has two modes of output. In the first mode where you type `data` at the prompt, Python shows you the raw string representation including quotes and escape codes. When you type `print(data)`, you get the actual formatted output of the string.

Although reading a file all at once is simple, it is often not the most appropriate way to do it---especially if the file happens to be huge or if contains lines of text that you want to handle one at a time.

To read a file line-by-line, use a for-loop like this:

```python
>>> with open('portfolio.csv', 'rt') as f:
        for line in f:
            print(line, end='')

name,shares,price
"AA",100,32.20
"IBM",50,91.10
...
>>>
```

When you use this code as shown, lines are read until the end of the file is reached at which point the loop stops.

On certain occasions, you might want to manually read or skip a _single_ line of text (e.g., perhaps you want to skip the first line of column headers).

```python
>>> f = open('portfolio.csv', 'rt')
>>> headers = next(f)
>>> headers
'name,shares,price\n'
>>> for line in f:
    print(line, end='')

"AA",100,32.20
"IBM",50,91.10
...
>>> f.close()
>>>
```

`next()` returns the next line of text in the file. If you were to call it repeatedly, you would get successive lines. However, just so you know, the `for` loop already uses `next()` to obtain its data. Thus, you normally wouldn't call it directly unless you're trying to explicitly skip or read a single line as shown.

Once you're reading lines of a file, you can start to perform more processing such as splitting. For example, try this:

```python
>>> f = open('portfolio.csv', 'rt')
>>> headers = next(f).split(',')
>>> headers
['name', 'shares', 'price\n']
>>> for line in f:
    row = line.split(',')
    print(row)

['"AA"', '100', '32.20\n']
['"IBM"', '50', '91.10\n']
...
>>> f.close()
```

_Note: In these examples, `f.close()` is being called explicitly because the `with` statement isn't being used._
