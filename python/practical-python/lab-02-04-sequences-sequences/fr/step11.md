# Fonction `zip()`

La fonction `zip` prend plusieurs séquences et crée un itérateur qui les combine.

```python
columns = ['name','shares', 'price']
values = ['GOOG', 100, 490.1 ]
pairs = zip(columns, values)
# ('name','GOOG'), ('shares',100), ('price',490.1)
```

Pour obtenir le résultat, vous devez itérer. Vous pouvez utiliser plusieurs variables pour déballer les tuples comme montré précédemment.

```python
for column, value in pairs:
  ...
```

Une utilisation courante de `zip` est de créer des paires clé/valeur pour construire des dictionnaires.

```python
d = dict(zip(columns, values))
```
