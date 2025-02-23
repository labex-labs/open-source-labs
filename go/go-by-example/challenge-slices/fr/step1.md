# Slices

Le problème à résoudre dans ce défi est de créer et de manipuler des slices en Go. Vous devrez créer un slice vide avec une longueur non nulle, définir et obtenir des valeurs dans le slice, utiliser la fonction `len` pour obtenir la longueur du slice, utiliser la fonction `append` pour ajouter de nouvelles valeurs au slice, utiliser la fonction `copy` pour copier un slice et utiliser l'opérateur de slice pour obtenir un sous-ensemble d'éléments à partir d'un slice existant.

## Exigences

Pour terminer ce défi, vous devrez avoir une compréhension de base de la syntaxe Go et du type de données slice. Vous devrez également être familier avec les fonctions `make`, `append` et `copy`, ainsi que l'opérateur de slice.

## Exemple

```sh
# Notez que bien que les slices soient de différents types que les tableaux,
# ils sont affichés de manière similaire par `fmt.Println`.
$ go run slices.go
emp: [ ]
set: [a b c]
get: c
len: 3
apd: [a b c d e f]
cpy: [a b c d e f]
sl1: [c d e]
sl2: [a b c d e]
sl3: [c d e f]
dcl: [g h i]
2d: [[0] [1 2] [2 3 4]]

# Consultez ce [super article de blog](https://go.dev/blog/slices-intro)
# de l'équipe Go pour plus de détails sur la conception et
# l'implémentation des slices en Go.

# Maintenant que nous avons vu les tableaux et les slices, nous allons examiner
# la principale structure de données intégrée d'autres Go : les cartes.
```
