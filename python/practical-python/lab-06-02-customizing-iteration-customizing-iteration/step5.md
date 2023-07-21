# Exercise 6.6: Using a generator to produce data

If you look at the code in Exercise 6.5, the first part of the code is producing
lines of data whereas the statements at the end of the `while` loop are consuming
the data. A major feature of generator functions is that you can move all
of the data production code into a reusable function.

Modify the code in Exercise 6.5 so that the file-reading is performed by
a generator function `follow(filename)`. Make it so the following code
works:

```python
>>> for line in follow('Data/stocklog.csv'):
          print(line, end='')

... Should see lines of output produced here ...
```

Modify the stock ticker code so that it looks like this:

```python
if __name__ == '__main__':
    for line in follow('Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```
