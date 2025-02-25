# Pile

## Problème

Implémentez une pile en utilisant une liste chaînée en Python, avec les méthodes suivantes :

- push : ajoute un élément au sommet de la pile
- pop : supprime et renvoie l'élément au sommet de la pile. Si la pile est vide, renvoie None.
- peek : renvoie l'élément au sommet de la pile sans le supprimer. Si la pile est vide, renvoie None.
- is_empty : renvoie True si la pile est vide, False sinon.

## Exigences

Les exigences suivantes doivent être satisfaites :

- Lorsque l'on dépile une pile vide, renvoyer None.
- L'implémentation doit utiliser une liste chaînée.
- L'implémentation doit être en Python.
- L'implémentation doit inclure les quatre méthodes : push, pop, peek et is_empty.

## Utilisation Exemple

### Push

- Empiler sur une pile vide : stack.push(1)
- Empiler sur une pile non vide : stack.push(2)

### Pop

- Dépiler sur une pile vide : stack.pop() -> None
- Dépiler sur une pile avec un seul élément : stack.pop() -> 1
- Dépiler sur une pile avec plusieurs éléments : stack.pop() -> 2

### Peek

- Consulter le sommet d'une pile vide : stack.peek() -> None
- Consulter le sommet d'une pile avec un ou plusieurs éléments : stack.peek() -> 2

### Est Vide

- Est vide sur une pile vide : stack.is_empty() -> True
- Est vide sur une pile avec un ou plusieurs éléments : stack.is_empty() -> False
