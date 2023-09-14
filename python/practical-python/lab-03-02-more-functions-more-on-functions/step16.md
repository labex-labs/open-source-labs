# Exercise 3.6: Working without Headers

Some CSV files don't include any header information. For example, the file `prices.csv` looks like this:

```csv
"AA",9.22
"AXP",24.85
"BA",44.85
"BAC",11.27
...
```

Modify the `parse_csv()` function `/home/labex/project/fileparse_3.6.py` so that it can work with such files by creating a list of tuples instead. For example:

```python
>>> prices = parse_csv('prices.csv', types=[str,float], has_headers=False)
>>> prices
[('AA', 9.22), ('AXP', 24.85), ('BA', 44.85), ('BAC', 11.27), ('C', 3.72), ('CAT', 35.46), ('CVX', 66.67), ('DD', 28.47), ('DIS', 24.22), ('GE', 13.48), ('GM', 0.75), ('HD', 23.16), ('HPQ', 34.35), ('IBM', 106.28), ('INTC', 15.72), ('JNJ', 55.16), ('JPM', 36.9), ('KFT', 26.11), ('KO', 49.16), ('MCD', 58.99), ('MMM', 57.1), ('MRK', 27.58), ('MSFT', 20.89), ('PFE', 15.19), ('PG', 51.94), ('T', 24.79), ('UTX', 52.61), ('VZ', 29.26), ('WMT', 49.74), ('XOM', 69.35)]
>>>
```

To make this change, you'll need to modify the code so that the first line of data isn't interpreted as a header line. Also, you'll need to make sure you don't create dictionaries as there are no longer any column names to use for keys.

Here's a solution in `/home/labex/project` directory.