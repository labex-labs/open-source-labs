# String Formatierung

Eine Möglichkeit, Zeichenketten in Python 3.6+ zu formatieren, sind `f-Strings`.

```python
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> f'{name:>10s} {shares:>10d} {price:>10.2f}'
'       IBM        100      91.10'
>>>
```

Der Teil `{expression:format}` wird ersetzt.

Es wird häufig mit `print` verwendet.

```python
print(f'{name:>10s} {shares:>10d} {price:>10.2f}')
```
