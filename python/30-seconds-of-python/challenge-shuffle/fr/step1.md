# Mélanger une liste

## Problème

Écrivez une fonction `shuffle(lst)` qui prend une liste en entrée et renvoie une nouvelle liste avec les mêmes éléments dans un ordre aléatoire. Votre fonction doit utiliser l'algorithme de Fisher-Yates pour mélanger les éléments de la liste.

L'algorithme de Fisher-Yates fonctionne comme suit :

1. Commencez par le dernier élément de la liste.
2. Générez un indice aléatoire entre 0 et l'indice actuel.
3. Échangez l'élément à l'indice actuel avec l'élément à l'indice aléatoire.
4. Passez à l'élément suivant de la liste et répétez les étapes 2-3 jusqu'à ce que tous les éléments aient été mélangés.

Votre fonction ne doit pas modifier la liste d'origine. Au lieu de cela, elle doit créer une nouvelle liste avec les éléments mélangés.

Vous pouvez supposer que la liste d'entrée contiendra au moins un élément.

## Exemple

```python
foo = [1, 2, 3, 4, 5]
shuffled_foo = shuffle(foo)
print(shuffled_foo) # [3, 1, 4, 5, 2]
print(foo) # [1, 2, 3, 4, 5]
```
