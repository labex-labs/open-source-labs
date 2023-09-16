# Exercise 3.11: Module imports

In section 3, we created a general purpose function `parse_csv()` for parsing the contents of CSV datafiles.

Now, we're going to see how to use that function in other programs. First, start in a new shell window. Navigate to the folder where you have all your files. We are going to import them.

Start Python interactive mode.

```shell
$ python3
Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Once you've done that, try importing some of the programs you previously wrote. You should see their output exactly as before. Just to emphasize, importing a module runs its code.

```python
>>> import bounce
... watch output ...
>>> import mortgage
... watch output ...
>>> import report
... watch output ...
>>>
```

If none of this works, you're probably running Python in the wrong directory. Now, try importing your `fileparse` module and getting some help on it.

```python
>>> import fileparse
>>> help(fileparse)
... look at the output ...
>>> dir(fileparse)
... look at the output ...
>>>
```

Try using the module to read some data:

```python
>>> portfolio = fileparse.parse_csv('/home/labex/project/portfolio.csv',select=['name','shares','price'], types=[str,int,float])
>>> portfolio
... look at the output ...
>>> pricelist = fileparse.parse_csv('/home/labex/project/prices.csv',types=[str,float], has_headers=False)
>>> pricelist
... look at the output ...
>>> prices = dict(pricelist)
>>> prices
... look at the output ...
>>> prices['IBM']
106.28
>>>
```

Try importing a function so that you don't need to include the module name:

```python
>>> from fileparse import parse_csv
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv', select=['name','shares','price'], types=[str,int,float])
>>> portfolio
... look at the output ...
>>>
```
