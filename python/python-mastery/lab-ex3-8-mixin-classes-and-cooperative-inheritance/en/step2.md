# Implementing Mixin Classes for Formatting

In this step, we'll introduce mixin classes - a powerful Python technique for adding functionality to classes without altering their original code.

## What Are Mixin Classes?

A mixin is a class that provides functionality to be inherited by another class, but isn't meant to be instantiated on its own. Mixins are a way to use multiple inheritance in a controlled, predictable manner.

Let's implement two mixin classes in our `tableformat.py` file. Open the file in the editor:

```bash
cd ~/project
code tableformat.py
```

Add the following class definitions at the end of the file (before any existing functions):

```python
class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)
```

This mixin provides column formatting functionality. The `formats` class variable holds format codes, and the `row()` method applies these formats to the row data before passing it to the parent class.

Now add another mixin class that makes table headers appear in uppercase:

```python
class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])
```

This mixin transforms header text to uppercase before passing it to the parent class's `headings()` method.

## Using the Mixin Classes

Let's test our new mixin classes. Run the following Python code:

```python
python3 -c "
from tableformat import TextTableFormatter, ColumnFormatMixin, portfolio, print_table

class PortfolioFormatter(ColumnFormatMixin, TextTableFormatter):
    formats = ['%s', '%d', '%0.2f']

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

You should see nicely formatted output with consistent decimal places in the price column:

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

Now let's try the `UpperHeadersMixin`:

```python
python3 -c "
from tableformat import TextTableFormatter, UpperHeadersMixin, portfolio, print_table

class PortfolioFormatter(UpperHeadersMixin, TextTableFormatter):
    pass

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

This should display the headers in uppercase:

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

Notice the use of `super().method()` in our mixins. This is called "cooperative inheritance" - each class in the inheritance chain cooperates by properly calling the next class's method. This allows a chain of classes to each add their own behavior.

The order of inheritance is critical. When we define `class PortfolioFormatter(ColumnFormatMixin, TextTableFormatter)`, Python looks for methods first in `ColumnFormatMixin`, then in `TextTableFormatter`. When `super().row()` is called in the mixin, it refers to `TextTableFormatter.row()`.

We can even combine both mixins:

```python
python3 -c "
from tableformat import TextTableFormatter, ColumnFormatMixin, UpperHeadersMixin, portfolio, print_table

class PortfolioFormatter(ColumnFormatMixin, UpperHeadersMixin, TextTableFormatter):
    formats = ['%s', '%d', '%0.2f']

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

This gives us both uppercase headers and formatted numbers:

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
