# Special Challenge Project

In [Exercise 2.5](ex2_5.md), we created a class `RideData` that
stored all of the bus data in columns, but actually presented the data
to a user as a sequence of dictionaries. It saved a lot of memory
through various forms of magic.

Can you generalize that idea? Specifically, can you make a general
purpose function `read_csv_as_columns()` that works like this:

```python
>>> data = read_csv_as_columns('ctabus.csv', types=[str, str, str, int])
>>> data
<__main__.DataCollection object at 0x102b45048>
>>> len(data)
577563
>>> data[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> data[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>> data[2]
{'route': '6', 'date': '01/01/2001', 'daytype': 'U', 'rides': 6048}
>>>
```

This function is supposed to be general purpose--you can give it any file and
a list of the column types and it will read the data. The data is read into
a class `DataCollection` that stores the data as columns internally. The data
presents itself as a sequence of dictionaries when accessed however.

Try using this function with the string interning trick in the last part. How
much memory does it take to store all of the ride data now? Can you still use
this function with your earlier CTA analysis code?
