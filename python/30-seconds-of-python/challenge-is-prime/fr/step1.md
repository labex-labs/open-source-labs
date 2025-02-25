# Le nombre est premier

## Problème

Écrivez une fonction Python appelée `is_prime(n)` qui prend un entier `n` en entrée et renvoie `True` si le nombre est premier, et `False` sinon. Pour résoudre ce problème, vous devez suivre les règles suivantes :

- Retournez `False` si le nombre est `0`, `1`, un nombre négatif ou un multiple de `2`.
- Utilisez `all()` et `range()` pour vérifier les nombres de `3` à la racine carrée du nombre donné.
- Retournez `True` si aucun nombre ne divise le nombre donné, `False` sinon.

## Exemple

```python
is_prime(11) # True
```
