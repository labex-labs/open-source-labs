# Hauteur de l'arbre

## Problème

Étant donné un arbre binaire, écrire une fonction Python pour déterminer la hauteur de l'arbre. La hauteur d'un arbre binaire est la longueur du plus long chemin du nœud racine à n'importe quel nœud feuille de l'arbre.

## Exigences

Pour résoudre ce problème, nous devons répondre aux exigences suivantes :

- L'arbre donné est un arbre binaire.
- Nous disposons déjà d'une classe Node avec une méthode insert.
- La solution s'adapte à la mémoire.

## Utilisation de l'exemple

Voici quelques exemples de comportement attendu de la fonction :

- Si l'arbre ne contient qu'un seul nœud, la hauteur est 1. Par exemple, si l'entrée est 5 -> 1, la sortie devrait être 1.
- Si l'arbre contient plusieurs nœuds, la hauteur est la longueur du plus long chemin du nœud racine à n'importe quel nœud feuille. Par exemple, si l'entrée est 5, 2, 8, 1, 3 -> 3, la sortie devrait être 3.
