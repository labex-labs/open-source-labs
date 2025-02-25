# Puissance de deux

## Problème

Écrivez une fonction Python appelée `is_power_of_two` qui prend un entier en tant que paramètre et renvoie `True` si l'entrée est une puissance de deux, et `False` sinon. Une puissance de deux est tout nombre qui peut s'écrire sous la forme 2^n, où n est un entier. Par exemple, 2, 4, 8 et 16 sont toutes des puissances de deux.

## Exigences

La fonction `is_power_of_two` doit répondre aux exigences suivantes :

- Le nombre d'entrée doit être un entier.
- La fonction doit gérer les entrées invalides de manière appropriée.
- La sortie doit être un booléen.
- La fonction doit être conforme aux contraintes de mémoire.

## Utilisation exemple

Voici quelques exemples de comportement attendu de la fonction `is_power_of_two` :

- `is_power_of_two(None)` doit lever une `TypeError`.
- `is_power_of_two(0)` doit renvoyer `False`.
- `is_power_of_two(1)` doit renvoyer `True`.
- `is_power_of_two(2)` doit renvoyer `True`.
- `is_power_of_two(15)` doit renvoyer `False`.
- `is_power_of_two(16)` doit renvoyer `True`.
