# Rendement de monnaie

## Problème

Étant donné un ensemble de pièces de différentes valeurs et un montant total d'argent n, déterminer le nombre total de façons uniques de rendre la monnaie pour n cents. Les pièces fournies ont des valeurs inférieures à n cents.

## Exigences

Pour résoudre ce problème, les exigences suivantes doivent être satisfaites :

- Les pièces doivent atteindre exactement n cents.
- On peut supposer qu'un nombre infini de pièces est disponible pour former n cents.
- Il n'est pas nécessaire de rapporter la ou les combinaisons de pièces qui représentent le minimum.
- Les valeurs des pièces ne sont pas données dans l'ordre trié.
- La solution doit tenir en mémoire.

## Utilisation de l'exemple

Les exemples suivants démontrent l'utilisation du problème du rendu de monnaie :

- pièces : None ou n : None -> Exception
- pièces : [] ou n : 0 -> 0
- pièces : [1, 2, 3], n : 5 -> 5
