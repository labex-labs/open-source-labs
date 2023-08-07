# Making it Sane

Using mixins can be a useful tool for framework builders for reducing the amount of code that needs to be written. However, forcing users to remember how to properly compose classes and use multiple inheritance can fry their brains. In [Exercise 3.5](ex3_5.md), you wrote a function `create_formatter()` that made it easier to create a custom formatter. Take that function and extend it to understand a few optional arguments related to the mixin classes. For example:

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('csv', column_formats=['"%s"','%d','%0.2f'])
>>> print_table(portfolio, ['name','shares','price'], formatter)
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44

>>> formatter = create_formatter('text', upper_headers=True)
>>> print_table(portfolio, ['name','shares','price'], formatter)
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
>>>
```

Under the covers the `create_formatter()` function will properly compose the classes and return a proper `TableFormatter` instance.
