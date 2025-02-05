# Exercise 2.1: Tuples

At the interactive prompt, create the following tuple that represents the above row, but with the numeric columns converted to proper numbers:

```python
>>> t = (row[0], int(row[1]), float(row[2]))
>>> t
('AA', 100, 32.2)
>>>
```

Using this, you can now calculate the total cost by multiplying the shares and the price:

```python
>>> cost = t[1] * t[2]
>>> cost
3220.0000000000005
>>>
```

Is math broken in Python? What's the deal with the answer of 3220.0000000000005?

This is an artifact of the floating point hardware on your computer only being able to accurately represent decimals in Base-2, not Base-10. For even simple calculations involving base-10 decimals, small errors are introduced. This is normal, although perhaps a bit surprising if you haven't seen it before.

This happens in all programming languages that use floating point decimals, but it often gets hidden when printing. For example:

```python
>>> print(f'{cost:0.2f}')
3220.00
>>>
```

Tuples are read-only. Verify this by trying to change the number of shares to 75.

```python
>>> t[1] = 75
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
```

Although you can't change tuple contents, you can always create a completely new tuple that replaces the old one.

```python
>>> t = (t[0], 75, t[2])
>>> t
('AA', 75, 32.2)
>>>
```

Whenever you reassign an existing variable name like this, the old value is discarded. Although the above assignment might look like you are modifying the tuple, you are actually creating a new tuple and throwing the old one away.

Tuples are often used to pack and unpack values into variables. Try the following:

```python
>>> name, shares, price = t
>>> name
'AA'
>>> shares
75
>>> price
32.2
>>>
```

Take the above variables and pack them back into a tuple

```python
>>> t = (name, 2*shares, price)
>>> t
('AA', 150, 32.2)
>>>
```
