# Understanding Code Duplication

Let's start by looking at the current code in the `reader.py` file. In programming, examining existing code is an important step to understand how things work and identify areas for improvement. You can open the `reader.py` file in the WebIDE. There are two ways to do this. You can click on the file in the file explorer, or you can run the following commands in the terminal. These commands first navigate to the project directory and then display the contents of the `reader.py` file.

```bash
cd ~/project
cat reader.py
```

When you look at the code, you'll notice there are two functions. Functions in Python are blocks of code that perform a specific task. Here are the two functions and what they do:

1. `csv_as_dicts()`: This function takes CSV data and converts it into a list of dictionaries. A dictionary in Python is a collection of key - value pairs, which is useful for storing data in a structured way.
2. `csv_as_instances()`: This function takes CSV data and converts it into a list of instances. An instance is an object created from a class, which is a blueprint for creating objects.

Now, let's take a closer look at these two functions. You'll see that they are quite similar. Both functions follow these steps:

- First, they initialize an empty `records` list. A list in Python is a collection of items that can be of different types. Initializing an empty list means creating a list with no items in it, which will be used to store the processed data.
- Then, they use `csv.reader()` to parse the input. Parsing means analyzing the input data to extract meaningful information. In this case, `csv.reader()` helps us read the CSV data row by row.
- They handle the headers in the same way. Headers in a CSV file are the first row that usually contains the names of the columns.
- After that, they loop through each row in the CSV data. A loop is a programming construct that allows you to execute a block of code multiple times.
- For each row, they process it to create a record. This record can be either a dictionary or an instance, depending on the function.
- They append the record to the `records` list. Appending means adding an item to the end of the list.
- Finally, they return the `records` list, which contains all the processed data.

This duplication of code is a problem for several reasons. When code is duplicated:

- It becomes harder to maintain. If you need to make a change to the code, you have to make the same change in multiple places. This takes more time and effort.
- Any changes must be implemented in multiple places. This increases the chance that you might forget to make the change in one of the places, leading to inconsistent behavior.
- It also increases the chance of introducing bugs. Bugs are errors in the code that can cause it to behave unexpectedly.

The only real difference between these two functions is how they convert a row into a record. This is a classic situation where a higher - order function can be very useful. A higher - order function is a function that can take another function as an argument or return a function as a result.

Let's look at some sample usage of these functions to better understand how they work. The following code shows how to use `csv_as_dicts()` and `csv_as_instances()`:

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

In the next step, we'll create a higher - order function to eliminate this code duplication. This will make the code more maintainable and less error - prone.
