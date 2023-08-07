# Exercise 1.32: Using a library function

Python comes with a large standard library of useful functions. One library that might be useful here is the `csv` module. You should use it whenever you have to work with CSV data files. Here is an example of how it works:

```python
>>> import csv
>>> f = open('Data/portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name', 'shares', 'price']
>>> for row in rows:
        print(row)

['AA', '100', '32.20']
['IBM', '50', '91.10']
['CAT', '150', '83.44']
['MSFT', '200', '51.23']
['GE', '95', '40.37']
['MSFT', '50', '65.10']
['IBM', '100', '70.44']
>>> f.close()
>>>
```

One nice thing about the `csv` module is that it deals with a variety of low-level details such as quoting and proper comma splitting. In the above output, you'll notice that it has stripped the double-quotes away from the names in the first column.

Modify your `pcost.py` program so that it uses the `csv` module for parsing and try running earlier examples.
