# Exercise 1.14: String concatenation

Although string data is read-only, you can always reassign a variable
to a newly created string.

Try the following statement which concatenates a new symbol "GOOG" to
the end of `symbols`:

```python
>>> symbols = symbols + 'GOOG'
>>> symbols
'AAPL,IBM,MSFT,YHOO,SCOGOOG'
>>>
```

Oops! That's not what you wanted. Fix it so that the `symbols` variable holds the value `'AAPL,IBM,MSFT,YHOO,SCO,GOOG'`.

```python
>>> symbols = ?
>>> symbols
'AAPL,IBM,MSFT,YHOO,SCO,GOOG'
>>>
```

Add `'HPQ'` to the front the string:

```python
>>> symbols = ?
>>> symbols
'HPQ,AAPL,IBM,MSFT,YHOO,SCO,GOOG'
>>>
```

In these examples, it might look like the original string is being
modified, in an apparent violation of strings being read only. Not
so. Operations on strings create an entirely new string each
time. When the variable name `symbols` is reassigned, it points to the
newly created string. Afterwards, the old string is destroyed since
it's not being used anymore.
