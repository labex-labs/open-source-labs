# Rechercher dans une matrice triée

## Problème

Étant donné une matrice triée, nous devons rechercher un élément spécifique dans celle-ci. La matrice est triée de manière à ce que les éléments de chaque ligne et de chaque colonne soient triés par ordre croissant. La matrice n'est pas nécessairement une matrice carrée. Nous devons retourner la position de l'élément dans la matrice sous forme d'un tuple (ligne, colonne) s'il est trouvé, sinon, nous devons retourner None.

## Exigences

Pour résoudre ce problème, nous devons faire les hypothèses suivantes :

- Les éléments de chaque ligne de la matrice sont triés par ordre croissant.
- Les éléments de chaque colonne de la matrice sont triés par ordre croissant.
- La matrice n'est pas irrégulière, c'est-à-dire qu'elle est un rectangle.
- L'ordre de tri est croissant.
- La matrice n'est pas nécessairement une matrice carrée.
- La sortie est un tuple (ligne, colonne).
- L'élément que nous recherchons peut ou non être dans la matrice.
- Les entrées peuvent ou non être valides.
- La solution doit tenir en mémoire.

## Utilisation de l'exemple

Nous pouvons utiliser les cas de test suivants pour vérifier notre solution :

- Si l'entrée est None, la fonction doit lever une exception.
- Si l'élément est trouvé dans la matrice, la fonction doit retourner sa position sous forme d'un tuple (ligne, colonne).
- Si l'élément n'est pas trouvé dans la matrice, la fonction doit retourner None.
