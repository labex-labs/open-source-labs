# Défi Python : Les marches

## Problème

Imaginez que vous vous trouviez au pied d'un escalier avec n marches. Vous pouvez prendre une, deux ou trois marches d'un coup. Le problème consiste à déterminer combien de façons possibles il y a de monter jusqu'à la nème marche.

Par exemple, s'il y a 3 marches, vous pouvez monter l'escalier de la manière suivante :

- 1-1-1
- 1-2
- 2-1
- 3

Donc, il y a 4 façons possibles de monter jusqu'à la 3ème marche.

## Exigences

Pour résoudre ce problème, nous devons garder à l'esprit les exigences suivantes :

- Si n == 0, le résultat devrait être 1. Cependant, il existe différentes approches pour ce problème, qui peuvent être discutées.
- Nous ne pouvons pas supposer que les entrées sont valides.
- Nous pouvons supposer que le problème s'adapte à la mémoire.

## Utilisation exemple

Voici quelques exemples de résolution de ce problème en utilisant Python :

- Aucune entrée ou entrée négative -> Exception
- n == 0 -> 1
- n == 1 -> 1
- n == 2 -> 2
- n == 3 -> 4
- n == 4 -> 7
- n == 10 -> 274
