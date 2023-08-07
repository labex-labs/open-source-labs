# Exercise 4.1: Objects as Data Structures

In section 2 and 3, we worked with data represented as tuples and dictionaries. For example, a holding of stock could be represented as a tuple like this:

```python
s = ('GOOG',100,490.10)
```

or as a dictionary like this:

```python
s = { 'name'   : 'GOOG',
      'shares' : 100,
      'price'  : 490.10
}
```

You can even write functions for manipulating such data. For example:

```python
def cost(s):
    return s['shares'] * s['price']
```

However, as your program gets large, you might want to create a better sense of organization. Thus, another approach for representing data would be to define a class. Create a file called `stock.py` and define a class `Stock` that represents a single holding of stock. Have the instances of `Stock` have `name`, `shares`, and `price` attributes. For example:

```python
>>> import stock
>>> a = stock.Stock('GOOG',100,490.10)
>>> a.name
'GOOG'
>>> a.shares
100
>>> a.price
490.1
>>>
```

Create a few more `Stock` objects and manipulate them. For example:

```python
>>> b = stock.Stock('AAPL', 50, 122.34)
>>> c = stock.Stock('IBM', 75, 91.75)
>>> b.shares * b.price
6117.0
>>> c.shares * c.price
6881.25
>>> stocks = [a, b, c]
>>> stocks
[<stock.Stock object at 0x37d0b0>, <stock.Stock object at 0x37d110>, <stock.Stock object at 0x37d050>]
>>> for s in stocks:
     print(f'{s.name:>10s} {s.shares:>10d} {s.price:>10.2f}')

... look at the output ...
>>>
```

One thing to emphasize here is that the class `Stock` acts like a factory for creating instances of objects. Basically, you call it as a function and it creates a new object for you. Also, it must be emphasized that each object is distinct---they each have their own data that is separate from other objects that have been created.

An object defined by a class is somewhat similar to a dictionary--just with somewhat different syntax. For example, instead of writing `s['name']` or `s['price']`, you now write `s.name` and `s.price`.
