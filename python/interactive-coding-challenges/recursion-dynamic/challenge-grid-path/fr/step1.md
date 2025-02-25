# Itinéraire dans une grille

## Problème

Étant donné une grille rectangulaire avec des cellules valides et invalides, implémentez une fonction pour trouver un itinéraire valide pour le robot pour se déplacer du coin supérieur gauche au coin inférieur droit. Si aucun itinéraire valide n'existe, renvoyez None. Si l'entrée est invalide ou la matrice est vide, renvoyez None.

## Exigences

Les exigences de cet algorithme sont les suivantes :

- Le robot ne peut se déplacer que vers la droite et vers le bas.
- Certaines cellules peuvent être interdites.
- La grille est rectangulaire et n'est pas irrégulière.
- Il n'y a pas toujours un itinéraire valide pour que le robot atteigne le coin inférieur droit.
- L'entrée n'est pas toujours valide.
- L'algorithme doit tenir compte des contraintes de mémoire.

## Utilisation de l'exemple

Considérez la grille suivante :

```txt
o = cellule valide
x = cellule invalide

   0  1  2  3
0  o  o  o  o
1  o  x  o  o
2  o  o  x  o
3  x  o  o  o
4  o  o  x  o
5  o  o  o  x
6  o  x  o  x
7  o  x  o  o
```

- Cas général :

```txt
attendu = [(0, 0), (1, 0), (2, 0),
            (2, 1), (3, 1), (4, 1),
            (5, 1), (5, 2), (6, 2),
            (7, 2), (7, 3)]
```

- Aucun itinéraire valide : Dans l'exemple ci-dessus, la cellule de la ligne 7 colonne 2 est également invalide -> None
- Entrée None -> None
- Matrice vide -> None
