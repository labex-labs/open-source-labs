# Inverser une chaîne de caractères

## Problème

Implémentez une fonction pour inverser une chaîne de caractères (une liste de caractères), en place. Cela signifie que la fonction doit modifier la chaîne d'origine plutôt que de créer une nouvelle. La fonction doit prendre une liste de caractères en entrée et renvoyer la même liste avec les caractères inversés.

Pour résoudre ce problème, nous devons prendre en compte quelques exigences :

## Exigences

- On peut supposer que la chaîne est en ASCII.
- Puisque nous devons le faire en place, nous ne pouvons pas utiliser l'opérateur de tranche ou la fonction `reversed`.
- Puisque les chaînes de caractères Python sont immuables, nous pouvons utiliser une liste de caractères à la place.

## Utilisation de l'exemple

Voici quelques exemples de comment doit se comporter la fonction :

- `None` -> `None`
- `['']` -> `['']`
- `['f', 'o', 'o','', 'b', 'a', 'r']` -> `['r', 'a', 'b','', 'o', 'o', 'f']`
