# Partition

## Problème

Étant donné une liste chaînée simple, la partitionner autour d'une valeur x, de sorte que tous les nœuds inférieurs à x viennent avant tous les nœuds supérieurs ou égaux à x. La fonction devrait retourner une nouvelle liste chaînée.

## Exigences

Pour résoudre ce problème, nous devons prendre en compte les exigences suivantes :

- La liste chaînée n'est pas circulaire et est simple.
- La fonction devrait retourner une nouvelle liste chaînée.
- La valeur d'entrée x est valide.
- Nous avons déjà une classe de liste chaînée qui peut être utilisée pour ce problème.
- Nous pouvons créer des structures de données supplémentaires.
- Le problème tient en mémoire.

## Utilisation de l'exemple

Voici quelques exemples de fonctionnement de la fonction :

- Liste vide -> []
- Liste à un élément -> [élément]
- Liste gauche vide -> [10, 11, 12]
- Liste droite vide -> [1, 2, 3]
- Cas général
  - Partition = 10
  - Entrée : 4, 3, 7, 8, 10, 1, 10, 12
  - Sortie : 4, 3, 7, 8, 1, 10, 10, 12
