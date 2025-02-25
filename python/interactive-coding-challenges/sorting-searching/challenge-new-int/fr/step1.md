# Trouver l'entier manquant

## Problème

Étant donné un tableau de 32 entiers non négatifs, trouver un entier qui n'est pas présent dans le tableau d'entrée. La solution devrait utiliser la mémoire minimale.

## Exigences

Pour résoudre ce problème, nous devons prendre en compte les exigences suivantes :

- Le tableau d'entrée contient des entiers non négatifs.
- La plage des entiers n'est pas spécifiée, mais nous devons discuter de l'approche pour 4 milliards d'entiers.
- Nous devons implémenter la solution pour un tableau de 32 entiers.
- Nous ne pouvons pas supposer que le tableau d'entrée est valide.

## Utilisation de l'exemple

Voici quelques exemples de la manière dont la fonction devrait se comporter :

- Si l'entrée est None ou un tableau vide, la fonction devrait lever une exception.
- S'il y a un entier exclu du tableau d'entrée, la fonction devrait renvoyer cet entier.
- S'il n'y a pas d'entier exclu du tableau d'entrée, la fonction devrait renvoyer None.
