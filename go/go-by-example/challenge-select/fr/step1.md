# Select

Dans ce défi, vous recevez deux canaux, `c1` et `c2`, qui recevront une valeur après un certain laps de temps. Votre tâche consiste à utiliser `select` pour attendre simultanément les deux valeurs, en affichant chacune lorsqu'elle arrive.

## Exigences

- Vous devriez utiliser l'instruction `select` pour attendre sur les deux canaux.
- Vous devriez afficher la valeur reçue de chaque canal lorsqu'elle arrive.

## Exemple

```sh
# Nous recevons les valeurs `"one"` puis `"two"` comme
# prévu.
$ time go run select.go
received one
received two

# Notez que le temps d'exécution total est seulement d'environ 2 secondes
# car les deux `Sleeps` de 1 et 2 secondes s'exécutent
# simultanément.
real 0m2.245s
```
