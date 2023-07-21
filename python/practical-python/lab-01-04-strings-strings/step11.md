# f-Strings

A string with formatted expression substitution.

```python
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> a = f'{name:>10s} {shares:10d} {price:10.2f}'
>>> a
'       IBM        100      91.10'
>>> b = f'Cost = ${shares*price:0.2f}'
>>> b
'Cost = $9110.00'
>>>
```

**Note: This requires Python 3.6 or newer.** The meaning of the format codes
is covered later.

In these exercises, you'll experiment with operations on Python's
string type. You should do this at the Python interactive prompt
where you can easily see the results. Important note:

> In exercises where you are supposed to interact with the interpreter,
> `>>>` is the interpreter prompt that you get when Python wants
> you to type a new statement. Some statements in the exercise span
> multiple lines--to get these statements to run, you may have to hit
> 'return' a few times. Just a reminder that you _DO NOT_ type
> the `>>>` when working these examples.

Start by defining a string containing a series of stock ticker symbols like this:

```python
>>> symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
>>>
```
