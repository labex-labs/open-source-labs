# Making Objects Comparable with `__eq__`

In Python, when you use the `==` operator to compare two objects, Python actually calls the `__eq__` special method. By default, this method compares the identities of objects, which means it checks if they are stored at the same memory address, rather than comparing their contents.

Let's take a look at an example. Suppose we have a `Stock` class, and we create two `Stock` objects with the same values. Then we try to compare them using the `==` operator. Here's how you can do it in the Python interpreter:

First, start the Python interpreter by running the following command in your terminal:

```bash
python3
```

Then, in the Python interpreter, execute the following code:

```python
>>> import stock
>>> a = stock.Stock('GOOG', 100, 490.1)
>>> b = stock.Stock('GOOG', 100, 490.1)
>>> a == b
False
```

As you can see, even though the two `Stock` objects `a` and `b` have the same values for their attributes (`name`, `shares`, and `price`), Python considers them different objects because they are stored at different memory locations.

To fix this issue, we can implement the `__eq__` method in our `Stock` class. This method will be called every time the `==` operator is used on objects of the `Stock` class.

Now, open the `stock.py` file again. Inside the `Stock` class, add the following `__eq__` method:

```python
def __eq__(self, other):
    return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                         (other.name, other.shares, other.price))
```

Let's break down what this method does:

1. First, it uses the `isinstance` function to check if the `other` object is an instance of the `Stock` class. This is important because we only want to compare `Stock` objects with other `Stock` objects.
2. If `other` is a `Stock` object, it then compares the attributes (`name`, `shares`, and `price`) of both the `self` object and the `other` object.
3. It returns `True` only if both objects are `Stock` instances and their attributes are identical.

After adding the `__eq__` method, your complete `Stock` class should look like this:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"

    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                             (other.name, other.shares, other.price))
```

Now, let's test our improved `Stock` class. Start the Python interpreter again:

```bash
python3
```

Then, run the following code in the Python interpreter:

```python
>>> import stock
>>> a = stock.Stock('GOOG', 100, 490.1)
>>> b = stock.Stock('GOOG', 100, 490.1)
>>> a == b
True
>>> c = stock.Stock('GOOG', 200, 490.1)
>>> a == c
False
```

Great! Now our `Stock` objects can be properly compared based on their content, rather than their memory addresses.

The `isinstance` check in the `__eq__` method is crucial. It ensures that we are only comparing `Stock` objects. If we didn't have this check, comparing a `Stock` object with something that is not a `Stock` object might raise errors.

When you're done testing, you can exit the Python interpreter by running the following command:

```python
>>> exit()
```
