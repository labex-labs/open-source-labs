# Dépacage de tuples

Pour utiliser le tuple ailleurs, vous pouvez extraire ses parties dans des variables.

```python
name, shares, price = s
print('Coût', shares * price)
```

Le nombre de variables à gauche doit correspondre à la structure du tuple.

```python
name, shares = s     # ERREUR
Traceback (most recent call last):
...
ValueError: too many values to unpack
```
