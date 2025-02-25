# Coin Change Ways

## Problème

Étant donné un entier `n` et un tableau de pièces distinctes, écrire une fonction pour compter le nombre de façons de rendre la monnaie pour `n` en utilisant les pièces du tableau. Une pièce peut être utilisée un nombre quelconque de fois, et on compte les combinaisons uniques.

Par exemple, si `n = 4` et `coins = [1, 2]`, il y a 3 façons de rendre la monnaie : 1+1+1+1, 1+2+1 et 2+2.

## Exigences

Pour résoudre ce problème, vous devrez :

- Écrire une fonction qui prend deux arguments : un entier `n` et un tableau de pièces distinctes.
- Utiliser la programmation dynamique pour compter le nombre de façons de rendre la monnaie pour `n` en utilisant les pièces du tableau.
- Retourner le nombre de combinaisons uniques.

## Exemple

Entrée : `n = 4`, `coins = [1, 2]`

Sortie : 3. 1+1+1+1, 1+2+1, 2+2, seraient les façons de rendre la monnaie.
