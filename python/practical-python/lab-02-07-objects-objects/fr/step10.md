# Tout est un objet

Les nombres, les chaînes de caractères, les listes, les fonctions, les exceptions, les classes, les instances, etc. sont tous des objets. Cela signifie que tous les objets qui peuvent être nommés peuvent être passés comme des données, placés dans des conteneurs, etc., sans aucune restriction. Il n'y a pas de _types spéciaux_ d'objets. Parfois, on dit que tous les objets sont "de première classe".

Un exemple simple :

```python
>>> import math
>>> items = [abs, math, ValueError ]
>>> items
[<fonction intégrée abs>,
  <module'math' (builtin)>,
  <type 'exceptions.ValueError'>]
>>> items[0](-45)
45
>>> items[1].sqrt(2)
1.4142135623730951
>>> try:
        x = int('not a number')
    except items[2]:
        print('Échoué!')
Échoué!
>>>
```

Ici, `items` est une liste contenant une fonction, un module et une exception. Vous pouvez directement utiliser les éléments de la liste à la place des noms originaux :

```python
items[0](-45)       # abs
items[1].sqrt(2)    # math
except items[2]:    # ValueError
```

Avec un grand pouvoir vient une grande responsabilité. Juste parce que vous pouvez le faire ne signifie pas que vous devriez.

Dans cet ensemble d'exercices, nous examinons quelques-uns des pouvoirs issus des objets de première classe.
