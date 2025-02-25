# Aplatir une liste

## Problème

Écrivez une fonction Python appelée `flatten(lst)` qui prend une liste de listes en argument et renvoie une liste aplatie. La fonction ne devrait aplatir la liste qu'une seule fois, ce qui signifie que toute liste imbriquée dans la liste d'origine devrait être aplatie, mais toute liste imbriquée dans ces listes imbriquées devrait rester inchangée.

Pour résoudre ce problème, vous pouvez utiliser une compréhension de liste pour extraire chaque valeur des sous-listes dans l'ordre.

## Exemple

```python
flatten([[1, 2, 3, 4], [5, 6, 7, 8]]) # [1, 2, 3, 4, 5, 6, 7, 8]
```
