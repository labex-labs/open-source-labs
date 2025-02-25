# Recherche dans un tableau roté

## Problème

Étant donné un tableau trié qui a été roté un certain nombre de fois, nous devons trouver un élément spécifique dans le tableau. Par exemple, si le tableau trié original était [1, 2, 3, 4, 5] et qu'il a été roté deux fois pour devenir [3, 4, 5, 1, 2], nous devons trouver l'index d'un élément spécifique, tel que 4.

## Exigences

Pour résoudre ce problème, nous devons prendre en compte les exigences suivantes :

- L'entrée est un tableau d'entiers.
- Nous ne savons pas combien de fois le tableau a été roté.
- Le tableau était originalement trié par ordre croissant.
- Pour la sortie, nous devons retourner l'index de l'élément que nous cherchons.
- Nous ne pouvons pas supposer que les entrées sont valides.
- Nous pouvons supposer que la solution s'adapte à la mémoire.

## Utilisation de l'exemple

Voici quelques exemples de manière dont cette fonction peut être utilisée :

- Si aucune entrée n'est fournie, une exception devrait être levée.
- Si un tableau vide est fourni, None devrait être retourné.
- Si l'élément que nous cherchons n'est pas trouvé dans le tableau, None devrait être retourné.
- Si le tableau contient des doublons, la fonction devrait toujours être capable de trouver l'index correct.
- Si le tableau ne contient pas de doublons, la fonction devrait toujours être capable de trouver l'index correct.
