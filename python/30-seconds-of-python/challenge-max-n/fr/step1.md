# Défi des n éléments maximaux

## Problème

Écrivez une fonction `max_n(lst, n = 1)` qui prend une liste `lst` et un entier optionnel `n` en arguments et renvoie une liste des `n` éléments maximaux de la liste fournie. Si `n` n'est pas fourni, la fonction devrait renvoyer une liste contenant l'élément maximum de la liste. Si `n` est supérieur ou égal à la longueur de la liste, la fonction devrait renvoyer la liste d'origine triée par ordre décroissant.

Votre tâche est d'implémenter la fonction `max_n()`.

## Exemple

```python
max_n([1, 2, 3]) # [3]
max_n([1, 2, 3], 2) # [3, 2]
max_n([1, 2, 3, 4, 5], 3) # [5, 4, 3]
max_n([1, 2, 3, 4, 5], 6) # [5, 4, 3, 2, 1]
```
