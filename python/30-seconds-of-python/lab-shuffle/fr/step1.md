# Mélanger une liste

Écrivez une fonction `shuffle(lst)` qui prend une liste en entrée et renvoie une nouvelle liste avec les mêmes éléments dans un ordre aléatoire. Votre fonction devrait utiliser l'algorithme de Fisher-Yates pour mélanger les éléments de la liste.

L'algorithme de Fisher-Yates fonctionne comme suit :

1. Commencez par le dernier élément de la liste.
2. Générez un index aléatoire entre 0 et l'index actuel.
3. Échangez l'élément à l'index actuel avec l'élément à l'index aléatoire.
4. Passez à l'élément suivant de la liste et répétez les étapes 2-3 jusqu'à ce que tous les éléments aient été mélangés.

Votre fonction ne devrait pas modifier la liste d'origine. Au lieu de cela, elle devrait créer une nouvelle liste avec les éléments mélangés.

Vous pouvez supposer que la liste d'entrée contiendra au moins un élément.

```python
from copy import deepcopy
from random import randint

def shuffle(lst):
  temp_lst = deepcopy(lst)
  m = len(temp_lst)
  while (m):
    m -= 1
    i = randint(0, m)
    temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
  return temp_lst
```

```python
foo = [1, 2, 3]
shuffle(foo) # [2, 3, 1], foo = [1, 2, 3]
```
