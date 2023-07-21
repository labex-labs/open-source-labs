# Doc Strings

It's good practice to include documentation in the form of a
doc-string. Doc-strings are strings written immediately after the
name of the function. They feed `help()`, IDEs and other tools.

```python
def read_prices(filename):
    '''
    Read prices from a CSV file of name,price data
    '''
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

A good practice for doc strings is to write a short one sentence
summary of what the function does. If more information is needed,
include a short example of usage along with a more detailed
description of the arguments.
