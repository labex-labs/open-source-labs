# Moyenne d'une liste transformée

## Problème

Écrivez une fonction appelée `average_by(lst, fn = lambda x: x)` qui prend une liste `lst` et une fonction `fn` en arguments. La fonction `fn` doit être utilisée pour transformer chaque élément de la liste en une valeur. La fonction doit ensuite calculer la moyenne des valeurs transformées et la renvoyer.

Si l'argument `fn` n'est pas fourni, la fonction doit utiliser la fonction identité par défaut, qui renvoie simplement l'élément lui-même.

Votre fonction doit répondre aux exigences suivantes :

- Utiliser `map()` pour transformer chaque élément en la valeur renvoyée par `fn`.
- Utiliser `sum()` pour additionner toutes les valeurs transformées, puis diviser par `len(lst)`.
- Omettez le dernier argument, `fn`, pour utiliser la fonction identité par défaut.

Signature de la fonction : `def average_by(lst, fn = lambda x: x) -> float:`

## Exemple

```python
assert average_by([1, 2, 3, 4, 5]) == 3.0
assert average_by([1, 2, 3, 4, 5], lambda x: x**2) == 11.0
assert average_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda x: x['n']) == 5.0
```
