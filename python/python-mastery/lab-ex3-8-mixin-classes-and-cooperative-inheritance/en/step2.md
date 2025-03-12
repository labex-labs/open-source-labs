# Implementing Mixin Classes for Formatting

In this step, we're going to learn about mixin classes. Mixin classes are a really useful technique in Python. They allow you to add extra functionality to classes without changing their original code. This is great because it helps keep your code modular and easy to manage.

## What Are Mixin Classes?

A mixin is a special type of class. Its main purpose is to provide some functionality that can be inherited by another class. However, a mixin is not meant to be used on its own. You don't create an instance of a mixin class directly. Instead, you use it as a way to add specific features to other classes in a controlled and predictable way. This is a form of multiple inheritance, where a class can inherit from more than one parent class.

Now, let's implement two mixin classes in our `tableformat.py` file. First, open the file in the editor. You can do this by running the following commands in your terminal:

```bash
cd ~/project
code tableformat.py
```

Once the file is open, add the following class definitions at the end of the file, but before any existing functions.

```python
class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)
```

This `ColumnFormatMixin` class provides column formatting functionality. The `formats` class variable is a list that holds format codes. These codes are used to format the data in each column. The `row()` method takes the row data, applies the format codes to each element in the row, and then passes the formatted row data to the parent class using `super().row(rowdata)`.

Next, add another mixin class that makes table headers appear in uppercase:

```python
class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])
```

This `UpperHeadersMixin` class transforms the header text to uppercase. It takes the list of headers, converts each header to uppercase, and then passes the modified headers to the parent class's `headings()` method using `super().headings()`.

## Using the Mixin Classes

Let's test our new mixin classes. We'll run some Python code to see how they work.

```python
python3 -c "
from tableformat import TextTableFormatter, ColumnFormatMixin, portfolio, print_table

class PortfolioFormatter(ColumnFormatMixin, TextTableFormatter):
    formats = ['%s', '%d', '%0.2f']

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

When you run this code, you should see nicely formatted output. The price column will have consistent decimal places because of the formatting provided by the `ColumnFormatMixin`.

```
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

Now, let's try the `UpperHeadersMixin`. Run the following code:

```python
python3 -c "
from tableformat import TextTableFormatter, UpperHeadersMixin, portfolio, print_table

class PortfolioFormatter(UpperHeadersMixin, TextTableFormatter):
    pass

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

This code should display the headers in uppercase.

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

## Understanding Cooperative Inheritance

Notice that in our mixin classes, we use `super().method()`. This is called "cooperative inheritance". In cooperative inheritance, each class in the inheritance chain works together. When a class calls `super().method()`, it's asking the next class in the chain to perform its part of the task. This way, a chain of classes can each add their own behavior to the overall process.

The order of inheritance is very important. When we define `class PortfolioFormatter(ColumnFormatMixin, TextTableFormatter)`, Python looks for methods first in `ColumnFormatMixin`, and then in `TextTableFormatter`. So, when `super().row()` is called in the `ColumnFormatMixin`, it refers to `TextTableFormatter.row()`.

We can even combine both mixins. Run the following code:

```python
python3 -c "
from tableformat import TextTableFormatter, ColumnFormatMixin, UpperHeadersMixin, portfolio, print_table

class PortfolioFormatter(ColumnFormatMixin, UpperHeadersMixin, TextTableFormatter):
    formats = ['%s', '%d', '%0.2f']

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

This code will give us both uppercase headers and formatted numbers.

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

In the next step, we'll make these mixins easier to use by enhancing the `create_formatter()` function.
