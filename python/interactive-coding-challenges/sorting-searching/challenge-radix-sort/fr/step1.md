# Tri par radix

## Problème

Implémentez l'algorithme de tri par radix pour trier une liste d'entiers. L'algorithme trie les entiers en comparant leurs chiffres, en commençant par le chiffre de poids faible jusqu'au chiffre de poids fort. L'algorithme trie d'abord les entiers sur la base du chiffre de poids faible, puis du second chiffre de poids faible, et ainsi de suite jusqu'à ce que le chiffre de poids fort soit trié.

## Exigences

Pour implémenter le tri par radix, les exigences suivantes doivent être satisfaites :

- L'entrée doit être une liste d'entiers.
- Vérifiez s'il y a None au lieu d'un tableau.
- Supposons que les éléments du tableau sont des entiers.
- Les chiffres doivent être en base 10.
- L'algorithme doit être capable de gérer n'importe quel nombre de chiffres.
- L'algorithme doit tenir en mémoire.

## Utilisation exemple

Voici des exemples d'utilisation de l'algorithme de tri par radix :

- None -> Exception
- [] -> []
- [128, 256, 164, 8, 2, 148, 212, 242, 244] -> [2, 8, 128, 148, 164, 212, 242, 244, 256]
