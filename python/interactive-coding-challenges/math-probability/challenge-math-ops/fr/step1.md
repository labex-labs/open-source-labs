# Math Ops

## Problème

Créez une classe Python avec une méthode d'insertion qui peut insérer un entier dans une liste. La classe devrait également prendre en charge le calcul du maximum, du minimum, de la moyenne et du mode de la liste avec une complexité temporelle de O(1). La classe devrait gérer les scénarios suivants :

- Si l'entrée n'est pas valide, elle devrait lever une `TypeError`.
- Si la liste est vide, elle devrait lever une `ValueError`.
- Si plusieurs modes existent, elle peut renvoyer l'un quelconque des modes.

## Exigences

Pour résoudre le problème ci-dessus, nous devons suivre les exigences suivantes :

- Les entrées peuvent ne pas être valides, donc nous ne pouvons pas supposer que les entrées sont valides.
- La plage des entrées est comprise entre 0 et 100 inclus.
- La moyenne devrait renvoyer un `float`.
- Les autres résultats devraient renvoyer un entier.
- Si plusieurs modes existent, la classe peut renvoyer l'un quelconque des modes.
- Nous pouvons supposer que la liste tient en mémoire.

## Utilisation de l'exemple

Voici quelques exemples d'utilisation de la classe :

- `None` -> `TypeError`
- `[]` -> `ValueError`
- `[5, 2, 7, 9, 9, 2, 9, 4, 3, 3, 2]`
  - max : 9
  - min : 2
  - mean : 4.909090909090909
  - mode : 9 ou 2
