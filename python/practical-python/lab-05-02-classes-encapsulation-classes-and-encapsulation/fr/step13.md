# Exercice 5.7 : Propriétés et mutateurs

Modifiez l'attribut `shares` de sorte que la valeur soit stockée dans un attribut privé et qu'une paire de fonctions de propriété soit utilisée pour s'assurer qu'elle est toujours définie sur une valeur entière. Voici un exemple du comportement attendu :

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> s = Stock('GOOG',100,490.10)
>>> s.shares = 50
>>> s.shares = 'un grand nombre'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: valeur entière attendue
>>>
```
