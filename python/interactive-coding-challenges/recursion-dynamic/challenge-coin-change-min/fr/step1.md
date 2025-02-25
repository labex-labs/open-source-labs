# Coin Change Min

## Problème

Étant donné un ensemble de pièces de valeurs inférieures à n cents, nous devons déterminer le nombre minimum de façons de composer n cents à l'aide de ces pièces. Les pièces peuvent être utilisées en toute combinaison et nous avons un nombre infini de pièces de chaque dénomination. Nous n'avons pas besoin de rapporter la ou les combinaisons de pièces qui représentent le minimum.

## Exigences

Pour résoudre ce problème, nous devons prendre en compte les exigences suivantes :

- Les pièces doivent composer exactement n cents.
- Nous pouvons supposer que nous avons un nombre infini de pièces pour composer n cents.
- Nous n'avons pas besoin de rapporter la ou les combinaisons de pièces qui représentent le minimum.
- Nous ne pouvons pas supposer que les dénominations des pièces sont données dans l'ordre trié.
- Nous pouvons supposer que cela tient dans la mémoire.

## Utilisation de l'exemple

Voici quelques exemples de manière dont cette fonction peut être utilisée :

- pièces : None ou n : None -> Exception
- pièces : [] ou n : 0 -> 0
- pièces : [1, 2, 3] ou [3, 2, 1] -> 2
