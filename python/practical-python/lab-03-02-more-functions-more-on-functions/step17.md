# Exercise 3.7: Picking a different column delimiter

Although CSV files are pretty common, it's also possible that you could encounter a file that uses a different column separator such as a tab or space. For example, the file `Data/portfolio.dat` looks like this:

```csv
name shares price
"AA" 100 32.20
"IBM" 50 91.10
"CAT" 150 83.44
"MSFT" 200 51.23
"GE" 95 40.37
"MSFT" 50 65.10
"IBM" 100 70.44
```

The `csv.reader()` function allows a different column delimiter to be given as follows:

```python
rows = csv.reader(f, delimiter=' ')
```

Modify your `parse_csv()` function so that it also allows the delimiter to be changed.

For example:

```python
>>> portfolio = parse_csv('Data/portfolio.dat', types=[str, int, float], delimiter=' ')
>>> portfolio
[{'price': '32.20', 'name': 'AA', 'shares': '100'}, {'price': '91.10', 'name': 'IBM', 'shares': '50'}, {'price': '83.44', 'name': 'CAT', 'shares': '150'}, {'price': '51.23', 'name': 'MSFT', 'shares': '200'}, {'price': '40.37', 'name': 'GE', 'shares': '95'}, {'price': '65.10', 'name': 'MSFT', 'shares': '50'}, {'price': '70.44', 'name': 'IBM', 'shares': '100'}]
>>>
```
