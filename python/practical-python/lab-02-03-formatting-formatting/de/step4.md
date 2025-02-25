# format()-Methode

Es gibt eine Methode `format()`, die Formatierung auf Argumente oder Schlüsselwortargumente anwenden kann.

```python
>>> '{name:>10s} {shares:10d} {price:10.2f}'.format(name='IBM', shares=100, price=91.1)
'       IBM        100      91.10'
>>> '{:>10s} {:10d} {:10.2f}'.format('IBM', 100, 91.1)
'       IBM        100      91.10'
>>>
```

Ehrlich gesagt, `format()` ist etwas umständlich. Ich ziehe f-Strings vor.
