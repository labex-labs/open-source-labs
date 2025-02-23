# Tri

Le problème à résoudre dans ce défi est de trier des slices de chaînes de caractères et d'entiers à l'aide du package `sort`.

## Exigences

- Le package `sort` doit être importé.
- La fonction `sort.Strings()` doit être utilisée pour trier un slice de chaînes de caractères.
- La fonction `sort.Ints()` doit être utilisée pour trier un slice d'entiers.
- La fonction `sort.IntsAreSorted()` doit être utilisée pour vérifier si un slice d'entiers est déjà trié.

## Exemple

```sh
# Exécuter notre programme affiche les slices de chaînes de caractères et d'entiers triés
# et `true` comme résultat de notre test `AreSorted`.
$ go run sorting.go
Chaînes de caractères : [a b c]
Entiers : [2 4 7]
Trié : true
```
