# Bst

## Problème

Un arbre binaire de recherche est une structure de données qui permet des opérations de recherche, d'insertion et de suppression rapides. C'est un arbre dans lequel chaque nœud a au plus deux enfants, et le fils gauche est inférieur au parent, tandis que le fils droit est supérieur au parent. La méthode d'insertion ajoute un nouveau nœud à l'arbre à la position appropriée en fonction de sa valeur.

Votre tâche est d'implémenter un arbre binaire de recherche avec une méthode d'insertion en Python. La méthode d'insertion devrait prendre une valeur et ajouter un nouveau nœud à l'arbre à la position appropriée en fonction de sa valeur. Si l'entrée de la racine est None, retournez un arbre dont le seul élément est le nouveau nœud racine.

## Exigences

Pour terminer ce défi, vous devez répondre aux exigences suivantes :

- Vous ne pouvez pas insérer de valeurs None.
- Vous pouvez supposer que vous travaillez avec des entiers valides.
- Vous pouvez supposer que tous les descendants gauche sont inférieurs ou égaux au nœud, et que tous les descendants droits sont supérieurs au nœud.
- Vous n'avez pas à suivre les nœuds parents, mais c'est facultatif.
- Vous pouvez supposer que cela tient en mémoire.

## Utilisation de l'exemple

### Insertion

L'insertion sera testée par la traversée suivante :

### Traversée in-order

- 5, 2, 8, 1, 3 -> 1, 2, 3, 5, 8
- 1, 2, 3, 4, 5 -> 1, 2, 3, 4, 5

Vous n'avez pas à coder la traversée in-order, elle fait partie des tests unitaires.
