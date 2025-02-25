# Trier une liste en fonction d'indexes

## Problème

Écrivez une fonction `sort_by_indexes(lst, indexes, reverse=False)` qui prend deux listes en arguments et renvoie une nouvelle liste triée en fonction des index de la deuxième liste. La fonction devrait avoir les paramètres suivants :

- `lst` : Une liste d'éléments à trier.
- `indexes` : Une liste d'entiers représentant les index souhaités pour trier la `lst`.
- `reverse` : Un paramètre booléen optionnel qui, lorsqu'il est défini sur `True`, trie la liste dans l'ordre inverse.

La fonction devrait renvoyer une nouvelle liste triée en fonction des index de la deuxième liste.

## Exemple

```python
a = ['oeufs', 'pain', 'oranges', 'confiture', 'pommes', 'lait']
b = [3, 2, 6, 4, 1, 5]
sort_by_indexes(a, b) # ['pommes', 'pain', 'oeufs', 'confiture', 'lait', 'oranges']
sort_by_indexes(a, b, True)
# ['oranges', 'lait', 'confiture', 'oeufs', 'pain', 'pommes']
```
