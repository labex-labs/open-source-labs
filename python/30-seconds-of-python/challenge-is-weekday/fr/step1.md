# Vérifiez si une date est un jour de semaine

## Problème

Écrivez une fonction Python appelée `is_weekday()` qui prend une date en entrée et renvoie `True` si c'est un jour de semaine, et `False` si c'est un week-end. Si aucune date n'est fournie, la fonction devrait utiliser la date actuelle.

Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Importez le module `datetime`.
2. Définissez une fonction appelée `is_weekday()` qui prend une date en entrée. Si aucune date n'est fournie, utilisez la date actuelle.
3. Utilisez la méthode `weekday()` du module `datetime` pour obtenir le jour de la semaine sous forme d'un entier. La méthode `weekday()` renvoie un entier compris entre 0 (lundi) et 6 (dimanche).
4. Vérifiez si le jour de la semaine est inférieur ou égal à 4. Si c'est le cas, renvoyez `True`, sinon renvoyez `False`.

## Exemple

Voici quelques exemples de comportement attendu de votre fonction :

```python
from datetime import date

assert is_weekday(date(2022, 11, 11)) == False
assert is_weekday(date(2022, 11, 14)) == True
assert is_weekday(date(2022, 11, 12)) == False
assert is_weekday(date(2022, 11, 13)) == False
```
