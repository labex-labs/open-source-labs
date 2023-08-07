# Making a Parsing Utility Function

Create a new file `reader.py`. In that file, define a
utility function `read_csv_as_dicts()` that reads a file of CSV
data into a list of dictionaries where the user specifies
the type conversions for each column.

Here is how it should work:

```python
>>> import reader
>>> portfolio = reader.read_csv_as_dicts('portfolio.csv', [str,int,float])
>>> for s in portfolio:
         print(s)

{'name': 'AA', 'shares': 100, 'price': 32.2}
{'name': 'IBM', 'shares': 50, 'price': 91.1}
{'name': 'CAT', 'shares': 150, 'price': 83.44}
{'name': 'MSFT', 'shares': 200, 'price': 51.23}
{'name': 'GE', 'shares': 95, 'price': 40.37}
{'name': 'MSFT', 'shares': 50, 'price': 65.1}
{'name': 'IBM', 'shares': 100, 'price': 70.44}
>>>
```

Or, if you wanted to read the CTA data:

```python
>>> rows = reader.read_csv_as_dicts('ctabus.csv', [str,str,str,int])
>>> len(rows)
577563
>>> rows[0]
{'daytype': 'U', 'route': '3', 'rides': 7354, 'date': '01/01/2001'}
>>>
```
