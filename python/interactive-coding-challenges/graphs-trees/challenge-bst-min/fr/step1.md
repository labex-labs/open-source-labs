# Bst Min

## Problème

Étant donné un tableau trié, nous devons créer un arbre de recherche binaire de hauteur minimale. La hauteur d'un arbre de recherche binaire est le nombre d'arêtes entre la racine de l'arbre et sa feuille la plus éloignée. L'objectif est de créer un arbre de recherche binaire avec la hauteur la plus faible possible.

## Exigences

Pour résoudre ce problème, nous devons répondre aux exigences suivantes :

- Le tableau doit être trié par ordre croissant.
- Les éléments du tableau doivent être uniques.
- Nous devons supposer qu'il existe déjà une classe `Node` avec une méthode `insert`.
- Nous devons supposer que cela rentre en mémoire.

## Utilisation de l'exemple

Voici quelques exemples d'utilisation de la fonction :

- Entrée : [0, 1, 2, 3, 4, 5, 6]
  Sortie : Un arbre de recherche binaire de hauteur 3

- Entrée : [0, 1, 2, 3, 4, 5, 6, 7]
  Sortie : Un arbre de recherche binaire de hauteur 4
