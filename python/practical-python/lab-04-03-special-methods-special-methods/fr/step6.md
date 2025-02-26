# Méthodes liées

Une méthode qui n'a pas encore été appelée par l'opérateur d'appel de fonction `()` est connue sous le nom de _méthode liée_. Elle opère sur l'instance à partir de laquelle elle est issue.

```python
>>> s = stock.Stock('GOOG', 100, 490.10)
>>> s
<Stock object at 0x590d0>
>>> c = s.cost
>>> c
<bound method Stock.cost of <Stock object at 0x590d0>>
>>> c()
49010.0
>>>
```

Les méthodes liées sont souvent à l'origine d'erreurs non évidentes dues à la négligence. Par exemple :

```python
>>> s = stock.Stock('GOOG', 100, 490.10)
>>> print('Cost : %0.2f' % s.cost)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: float argument required
>>>
```

Ou un comportement trompeur difficile à déboguer.

```python
f = open(filename, 'w')
...
f.close     # Oups, rien n'a été fait du tout. `f` est toujours ouvert.
```

Dans les deux cas, l'erreur est causée par l'oubli d'inclure les parenthèses finales. Par exemple, `s.cost()` ou `f.close()`.
