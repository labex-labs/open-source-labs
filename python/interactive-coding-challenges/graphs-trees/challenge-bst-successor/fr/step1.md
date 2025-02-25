# Successeur d'un ABR

## Problème

Étant donné un arbre binaire de recherche et un nœud de cet arbre, trouver le successeur dans l'ordre de ce nœud. Le successeur d'un nœud est le nœud qui apparaît immédiatement après le nœud donné lors d'un parcours en ordre de l'arbre. Si aucun successeur n'existe, renvoyer None. Si l'entrée est None, lever une exception. On peut supposer qu'on a déjà une classe Node qui suit les parents, et on peut supposer que cela rentre en mémoire.

## Exigences

- La fonction devrait renvoyer le successeur dans l'ordre d'un nœud donné dans un arbre binaire de recherche.
- Si aucun successeur n'existe, la fonction devrait renvoyer None.
- Si l'entrée est None, la fonction devrait lever une exception.
- On peut supposer qu'on a déjà une classe Node qui suit les parents.
- On peut supposer que cela rentre en mémoire.

## Utilisation de l'exemple

```txt
          _5_
        /     \
       3       8
      / \    /   \
     2   4  6    12
    /        \   / \
   1          7 10  15
               /
              9

Entrée : None  Sortie : Exception
Entrée : 4     Sortie : 5
Entrée : 5     Sortie : 6
Entrée : 8     Sortie : 9
Entrée : 15    Sortie : None
```
