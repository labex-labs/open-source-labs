# Stack Min

## Problème

Le problème consiste à implémenter une pile avec les méthodes push, pop et min qui fonctionnent en O(1) temps. La méthode push ajoute un élément à la collection, la méthode pop supprime l'élément le plus récemment ajouté qui n'a pas encore été supprimé, et la méthode min renvoie l'élément minimum de la pile. Les trois méthodes devraient s'exécuter en temps constant, O(1).

## Exigences

Pour résoudre ce problème, nous devons prendre en compte les exigences suivantes :

- La pile ne contient que des entiers.
- Les valeurs d'entrée pour push sont valides.
- Si nous appelons la méthode min sur une pile vide, nous devrions renvoyer sys.maxsize.
- Nous pouvons supposer qu'il existe déjà une classe de pile que nous pouvons utiliser pour ce problème.
- Nous pouvons supposer que la pile tient dans la mémoire.

## Utilisation d'exemple

Nous pouvons tester notre implémentation avec les scénarios suivants :

- Push/pop sur une pile vide.
- Push/pop sur une pile non vide.
- Min sur une pile vide.
- Min sur une pile non vide.
