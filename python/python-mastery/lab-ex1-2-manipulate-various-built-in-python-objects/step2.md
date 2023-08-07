# Part 2 : String Manipulation

Define a string containing a series of stock ticker symbols like this:

```python
>>> symbols = 'AAPL IBM MSFT YHOO SCO'
```

Now, let's experiment with different string operations:

## Extracting individual characters and substrings

Strings are arrays of characters. Try extracting a few characters:

```python
>>> symbols[0]
'A'
>>> symbols[1]
'A'
>>> symbols[2]
'P'
>>> symbols[-1]        # Last character
'O'
>>> symbols[-2]        # 2nd from last character
'C'
>>>
```

Try taking a few slices:

```python
>>> symbols[:4]
'AAPL'
>>> symbols[-3:]
'SCO'
>>> symbols[5:8]
'IBM'
>>>
```

## Strings as read-only objects

Strings are read-only. Verify this by trying to change the first character of `symbols` to a lower-case 'a'.

```python
>>> symbols[0] = 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
```

## String concatenation

Although string data is read-only, you can always reassign a variable to a newly created string.\
Try the following statement which concatenates a new symbol "GOOG" to the end of `symbols`:

```python
>>> symbols += ' GOOG'
>>> symbols
... look at the result ...
```

Now, try adding "HPQ" to the beginning of `symbols` like this:

```python
>>> symbols = 'HPQ ' + symbols
>>> symbols
... look at the result ...
```

It should be noted in both of these examples, the original string `symbols` is _NOT_ being modified "in place." Instead, a completely new string is created. The variable name `symbols` is just bound to the result. Afterwards, the old string is destroyed since it's not being used anymore.

## Membership testing (substring testing)

Experiment with the `in` operator to check for substrings. At the interactive prompt, try these operations:

```python
>>> 'IBM' in symbols
True
>>> 'AA' in symbols
True
>>> 'CAT' in symbols
False
>>>
```

Make sure you understand why the check for "AA" returned `True`.

## String Methods

At the Python interactive prompt, try experimenting with some of the string methods.

```python
>>> symbols.lower()
'hpq aapl ibm msft yhoo sco goog'
>>> symbols
'HPQ AAPL IBM MSFT YHOO SCO GOOG'
```

Remember, strings are always read-only. If you want to save the result of an operation, you need to place it in a variable:

```python
>>> lowersyms = symbols.lower()
>>> lowersyms
'hpq aapl ibm msft yhoo sco goog'
>>>
```

Try some more operations:

```python
>>> symbols.find('MSFT')
13
>>> symbols[13:17]
'MSFT'
>>> symbols = symbols.replace('SCO','')
>>> symbols
'HPQ AAPL IBM MSFT YHOO  GOOG'
>>>
```
