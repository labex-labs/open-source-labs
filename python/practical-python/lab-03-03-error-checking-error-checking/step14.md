# Exercise 3.8: Raising exceptions

The `parse_csv()` function you wrote in the last section allows
user-specified columns to be selected, but that only works if the
input data file has column headers.

Modify the code so that an exception gets raised if both the `select`
and `has_headers=False` arguments are passed. For example:

```python
>>> parse_csv('Data/prices.csv', select=['name','price'], has_headers=False)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fileparse.py", line 9, in parse_csv
    raise RuntimeError("select argument requires column headers")
RuntimeError: select argument requires column headers
>>>
```

Having added this one check, you might ask if you should be performing
other kinds of sanity checks in the function. For example, should you
check that the filename is a string, that types is a list, or anything
of that nature?

As a general rule, it’s usually best to skip such tests and to just
let the program fail on bad inputs. The traceback message will point
at the source of the problem and can assist in debugging.

The main reason for adding the above check is to avoid running the code
in a non-sensical mode (e.g., using a feature that requires column
headers, but simultaneously specifying that there are no headers).

This indicates a programming error on the part of the calling code.
Checking for cases that "aren't supposed to happen" is often a good idea.
