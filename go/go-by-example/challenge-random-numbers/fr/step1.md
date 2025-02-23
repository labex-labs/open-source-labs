# Nombres aléatoires

Vous êtes requis d'écrire un programme qui génère des entiers et des flottants aléatoires dans une plage spécifiée. Le programme devrait également être capable de produire des séquences de nombres variables en changeant la graine.

## Exigences

- Le programme devrait utiliser le package `math/rand` pour générer des nombres aléatoires.
- Le programme devrait générer des entiers aléatoires dans une plage spécifiée.
- Le programme devrait générer des flottants aléatoires dans une plage spécifiée.
- Le programme devrait être capable de produire des séquences de nombres variables en changeant la graine.

## Exemple

```sh
# Selon où vous exécutez cet exemple, certains des
# nombres générés peuvent être différents. Notez que sur
# le terrain de jeu Go, le positionnement avec `time.Now()`
# produit toujours des résultats déterministes en raison
# de la manière dont le terrain de jeu est implémenté.
$ go run random-numbers.go
81,87
0.6645600532184904
7.123187485356329,8.434115364335547
0,28
5,87
5,87

# Consultez la documentation du package [`math/rand`](https://pkg.go.dev/math/rand)
# pour des références sur d'autres quantités aléatoires
# que Go peut fournir.
```
