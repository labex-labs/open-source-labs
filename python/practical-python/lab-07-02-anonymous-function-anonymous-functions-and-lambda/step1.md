# List Sorting Revisited

Lists can be sorted _in-place_. Using the `sort` method.

```python
s = [10,1,7,3]
s.sort() # s = [1,3,7,10]
```

You can sort in reverse order.

```python
s = [10,1,7,3]
s.sort(reverse=True) # s = [10,7,3,1]
```

It seems simple enough. However, how do we sort a list of dicts?

```python
[{'name': 'AA', 'price': 32.2, 'shares': 100},
{'name': 'IBM', 'price': 91.1, 'shares': 50},
{'name': 'CAT', 'price': 83.44, 'shares': 150},
{'name': 'MSFT', 'price': 51.23, 'shares': 200},
{'name': 'GE', 'price': 40.37, 'shares': 95},
{'name': 'MSFT', 'price': 65.1, 'shares': 50},
{'name': 'IBM', 'price': 70.44, 'shares': 100}]
```

By what criteria?

You can guide the sorting by using a _key function_. The _key
function_ is a function that receives the dictionary and returns the
value of interest for sorting.

```python
def stock_name(s):
    return s['name']

portfolio.sort(key=stock_name)
```

Here's the result.

```python
# Check how the dictionaries are sorted by the `name` key
[
  {'name': 'AA', 'price': 32.2, 'shares': 100},
  {'name': 'CAT', 'price': 83.44, 'shares': 150},
  {'name': 'GE', 'price': 40.37, 'shares': 95},
  {'name': 'IBM', 'price': 91.1, 'shares': 50},
  {'name': 'IBM', 'price': 70.44, 'shares': 100},
  {'name': 'MSFT', 'price': 51.23, 'shares': 200},
  {'name': 'MSFT', 'price': 65.1, 'shares': 50}
]
```
