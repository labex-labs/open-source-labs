# Création d'un tableau enregistrement

Un tableau enregistrement est une sous-classe de ndarray qui permet d'accéder aux champs par attribut au lieu d'index. Nous pouvons créer un tableau enregistrement à l'aide de la fonction `np.rec.array`.

```python
# Crée un tableau enregistrement
recordarr = np.rec.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
```
