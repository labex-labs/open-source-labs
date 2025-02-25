# Vérifiez si deux listes ont le même contenu

Écrivez une fonction `have_same_contents(a, b)` qui prend deux listes en arguments et renvoie `True` si elles ont le même contenu, `False` sinon. La fonction doit vérifier si les deux listes contiennent les mêmes éléments, quelle que soit leur ordre.

Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Utilisez `set()` sur la combinaison des deux listes pour trouver les valeurs uniques.
2. Itérez dessus avec une boucle `for` en comparant le `count()` de chaque valeur unique dans chaque liste.
3. Retournez `False` si les comptages ne correspondent pas pour un élément quelconque, `True` sinon.

```python
def have_same_contents(a, b):
  for v in set(a + b):
    if a.count(v)!= b.count(v):
      return False
  return True
```

```python
have_same_contents([1, 2, 4], [2, 4, 1]) # True
```
