# Comparisons

The following comparison / relational operators work with numbers:

```
x < y      Less than
x <= y     Less than or equal
x > y      Greater than
x >= y     Greater than or equal
x == y     Equal to
x != y     Not equal to
```

You can form more complex boolean expressions using

`and`, `or`, `not`

Here are a few examples:

```python
if b >= a and b <= c:
    print('b is between a and c')

if not (b < a or b > c):
    print('b is still between a and c')
```
