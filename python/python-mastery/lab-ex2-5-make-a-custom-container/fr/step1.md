# Croissance des listes

Les listes Python sont hautement optimisées pour effectuer des opérations `append()`. Chaque fois qu'une liste croît, elle prend un bloc de mémoire plus grand que ce qu'elle a réellement besoin, avec l'attente que plus de données seront ajoutées à la liste plus tard. Si de nouveaux éléments sont ajoutés et que de l'espace est disponible, l'opération `append()` stocke l'élément sans allouer plus de mémoire.

Expérimentez cette fonctionnalité des listes en utilisant la fonction `sys.getsizeof()` sur une liste et en ajoutant quelques autres éléments.

```python
>>> import sys
>>> items = []
>>> sys.getsizeof(items)
64
>>> items.append(1)
>>> sys.getsizeof(items)
96
>>> items.append(2)
>>> sys.getsizeof(items)    # Remarquez comment la taille ne diminue pas
96
>>> items.append(3)
>>> sys.getsizeof(items)    # Elle ne diminue toujours pas ici
96
>>> items.append(4)
>>> sys.getsizeof(items)    # Pas encore.
96
>>> items.append(5)
>>> sys.getsizeof(items)    # Remarquez que la taille a sauté
128
>>>
```

Une liste stocke ses éléments par référence. Ainsi, la mémoire requise pour chaque élément est une seule adresse mémoire. Sur une machine 64 bits, une adresse est généralement de 8 octets. Cependant, si Python a été compilé pour 32 bits, elle peut être de 4 octets et les nombres de l'exemple ci-dessus seront la moitié de ceux affichés.
