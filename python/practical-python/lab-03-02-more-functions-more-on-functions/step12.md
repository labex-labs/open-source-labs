# Reassignment vs Modifying

Make sure you understand the subtle difference between modifying a value and reassigning a variable name.

```python
def foo(items):
    items.append(42)    # Modifies the input object

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]

# VS
def bar(items):
    items = [4,5,6]    # Changes local `items` variable to point to a different object

b = [1, 2, 3]
bar(b)
print(b)                # [1, 2, 3]
```

_Reminder: Variable assignment never overwrites memory. The name is merely bound to a new value._

This set of exercises have you implement what is, perhaps, the most powerful and difficult part of the course. There are a lot of steps and many concepts from past exercises are put together all at once. The final solution is only about 25 lines of code, but take your time and make sure you understand each part.

A central part of your `report.py` program focuses on the reading of CSV files. For example, the function `read_portfolio()` reads a file containing rows of portfolio data and the function `read_prices()` reads a file containing rows of price data. In both of those functions, there are a lot of low-level "fiddly" bits and similar features. For example, they both open a file and wrap it with the `csv` module and they both convert various fields into new types.

If you were doing a lot of file parsing for real, you'd probably want to clean some of this up and make it more general purpose. That's our goal.

Start this exercise by opening the file called `fileparse.py`. This is where we will be doing our work.
