# Exercise 2.6: Dictionaries as a container

A dictionary is a useful way to keep track of items where you want to look up items using an index other than an integer. In the Python shell, try playing with a dictionary:

```python
>>> prices = { }
>>> prices['IBM'] = 92.45
>>> prices['MSFT'] = 45.12
>>> prices
... look at the result ...
>>> prices['IBM']
92.45
>>> prices['AAPL']
... look at the result ...
>>> 'AAPL' in prices
False
>>>
```

The file `prices.csv` contains a series of lines with stock prices. The file looks something like this:

```csv
"AA",9.22
"AXP",24.85
"BA",44.85
"BAC",11.27
"C",3.72
...
```

Write a function `read_prices(filename)` that reads a set of prices such as this into a dictionary where the keys of the dictionary are the stock names and the values in the dictionary are the stock prices.

To do this, start with an empty dictionary and start inserting values into it just as you did above. However, you are reading the values from a file now.

We'll use this data structure to quickly lookup the price of a given stock name.

A few little tips that you'll need for this part. First, make sure you use the `csv` module just as you did before---there's no need to reinvent the wheel here.

```python
>>> import csv
>>> f = open('prices.csv', 'r')
>>> rows = csv.reader(f)
>>> for row in rows:
        print(row)


['AA', '9.22']
['AXP', '24.85']
...
[]
>>>
```

The other little complication is that the `prices.csv` file may have some blank lines in it. Notice how the last row of data above is an empty list---meaning no data was present on that line.

There's a possibility that this could cause your program to die with an exception. Use the `try` and `except` statements to catch this as appropriate. Thought: would it be better to guard against bad data with an `if`-statement instead?

Once you have written your `read_prices()` function, test it interactively to make sure it works:

```python
>>> prices = read_prices('prices.csv')
>>> prices['IBM']
106.28
>>> prices['MSFT']
20.89
>>>
```
