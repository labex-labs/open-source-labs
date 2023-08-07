# Making it Easier To Choose

One problem with using inheritance is the added complexity of picking
different classes to use (e.g., remembering the names, using the right
`import` statements, etc.). A factory function can simplify this. Add
a function `create_formatter()` to your `tableformat.py` file that
allows a user to more easily make a formatter by specifying a format such as `'text'`, `'csv'`, or `'html'`. For example:

```python
>>> from tableformat import create_formatter, print_table
>>> formatter = create_formatter('html')
>>> print_table(portfolio, ['name','shares','price'], formatter)
<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
>>>
```

**Discussion**

The `TableFormatter` class in this exercise is an example of something known
as an "Abstract Base Class." It's not something that's meant to be used directly.
Instead, it's serving as a kind of interface specification for a program component--in
this case the various output formats. Essentially, the code that produces the table
will be programmed against the abstract base class with the expectation that a user
will provide a suitable implementation. As long as all of the required methods
have been implemented, it should all just "work" (fingers crossed).
