# Méthode format()

Il existe une méthode `format()` qui peut appliquer un formatage à des arguments positionnels ou nommés.

```python
>>> '{nom:>10s} {actions:10d} {prix:10.2f}'.format(nom='IBM', actions=100, prix=91.1)
'       IBM        100      91,10'
>>> '{:>10s} {:10d} {:10.2f}'.format('IBM', 100, 91.1)
'       IBM        100      91,10'
>>>
```

Franchement, `format()` est un peu verbeux. Je préfère les `f-strings`.
