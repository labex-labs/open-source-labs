# Dictionary Formatierung

Sie können die `format_map()`-Methode verwenden, um die Zeichenkettenformatierung auf ein Wörterbuch von Werten anzuwenden:

```python
>>> s = {
    'name': 'IBM',
   'shares': 100,
    'price': 91.1
}
>>> '{name:>10s} {shares:10d} {price:10.2f}'.format_map(s)
'       IBM        100      91.10'
>>>
```

Es verwendet die gleichen Codes wie `f-Strings`, nimmt jedoch die Werte aus dem angegebenen Wörterbuch.
