# Soustraire deux

## Problème

Écrivez une fonction Python qui prend deux entiers en entrée et renvoie leur différence sans utiliser le signe '+' ou '-'. La fonction doit gérer les cas suivants :

- Si l'une des entrées est None, la fonction doit lever une `TypeError`.
- La fonction doit fonctionner pour les entiers positifs et négatifs.

## Exigences

Pour résoudre ce problème, nous devons suivre les exigences suivantes :

- Vérifiez l'entrée None et levez une `TypeError` si nécessaire.
- Nous pouvons supposer que les entrées entreront en mémoire.

## Utilisation exemple

Voici quelques exemples de comportement attendu de la fonction :

```
sub_two(None, 5) -> TypeError
sub_two(7, 5) -> 2
sub_two(-5, -7) -> 2
sub_two(-5, 7) -> -12
sub_two(5, -7) -> 12
```
