# Parcours DFS d'un arbre

## Problème

Implémenter des parcours en profondeur (en ordre, pré-ordre, post-ordre) sur un arbre binaire. Pour le parcours en ordre, on visite le sous-arbre gauche, puis le nœud courant, puis le sous-arbre droit. Pour le parcours pré-ordre, on visite le nœud courant, puis le sous-arbre gauche, puis le sous-arbre droit. Pour le parcours post-ordre, on visite le sous-arbre gauche, puis le sous-arbre droit, puis le nœud courant.

## Exigences

Pour résoudre ce défi, nous devons répondre aux exigences suivantes :

- Nous pouvons supposer que nous disposons déjà d'une classe `Node` avec une méthode `insert`.
- Lorsque nous traitons chaque nœud, nous devons appeler une méthode d'entrée `visit_func` sur le nœud.
- Nous pouvons supposer que cela tient en mémoire.

## Utilisation exemple

Voici quelques exemples d'utilisation de l'algorithme DFS :

### Parcours en ordre

Pour un arbre binaire avec les valeurs 5, 2, 8, 1 et 3, le parcours en ordre serait 1, 2, 3, 5 et 8. Pour un arbre binaire avec les valeurs 1, 2, 3, 4 et 5, le parcours en ordre serait 1, 2, 3, 4 et 5.

### Parcours pré-ordre

Pour un arbre binaire avec les valeurs 5, 2, 8, 1 et 3, le parcours pré-ordre serait 5, 2, 1, 3 et 8. Pour un arbre binaire avec les valeurs 1, 2, 3, 4 et 5, le parcours pré-ordre serait 1, 2, 3, 4 et 5.

### Parcours post-ordre

Pour un arbre binaire avec les valeurs 5, 2, 8, 1 et 3, le parcours post-ordre serait 1, 3, 2, 8 et 5. Pour un arbre binaire avec les valeurs 1, 2, 3, 4 et 5, le parcours post-ordre serait 5, 4, 3, 2 et 1.
