# Understanding Code Duplication

Let's begin by examining the current code in `reader.py`. Open the file in the WebIDE by clicking on it in the file explorer or by running:

```bash
cd ~/project
cat reader.py
```

Looking at the code, you can see two functions:

1. `csv_as_dicts()`: Converts CSV data into a list of dictionaries
2. `csv_as_instances()`: Converts CSV data into a list of instances

Notice how similar these functions are. Both functions:

- Initialize an empty `records` list
- Use `csv.reader()` to parse the input
- Handle the headers in the same way
- Loop through each row in the CSV data
- Process each row to create a record (a dictionary or an instance)
- Append the record to the `records` list
- Return the `records` list

This duplication is problematic because:

- It makes the code harder to maintain
- Any changes must be implemented in multiple places
- It increases the chance of introducing bugs

The only real difference between these functions is how they convert a row into a record. This is a perfect case for a higher-order function.

Let's examine sample usage to better understand these functions:

```python
# Example of using csv_as_dicts
with open('portfolio.csv') as f:
    portfolio = csv_as_dicts(f, [str, int, float])
print(portfolio[0])  # {'name': 'AA', 'shares': 100, 'price': 32.2}

# Example of using csv_as_instances
class Stock:
    @classmethod
    def from_row(cls, row):
        return cls(row[0], int(row[1]), float(row[2]))

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

with open('portfolio.csv') as f:
    portfolio = csv_as_instances(f, Stock)
print(portfolio[0].name, portfolio[0].shares, portfolio[0].price)  # AA 100 32.2
```

In the next step, we'll create a higher-order function to eliminate this duplication.
