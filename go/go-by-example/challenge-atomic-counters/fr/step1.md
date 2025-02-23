# Compteurs atomiques

Le problème consiste à incrémenter un compteur exactement 1000 fois en utilisant 50 goroutines et le package `sync/atomic`.

## Exigences

- Utiliser le package `sync/atomic` pour incrémenter le compteur.
- Utiliser un WaitGroup pour attendre que toutes les goroutines aient terminé leur travail.

## Exemple

```sh
# Nous nous attendons à obtenir exactement 50 000 opérations. Si nous
# avions utilisé l'incrémentation non atomique `ops++` pour incrémenter le compteur,
# nous obtiendrions probablement un nombre différent, variant d'une exécution
# à l'autre, car les goroutines interféreraient les unes avec les autres. De plus,
# nous aurions des échecs de course de données lorsque nous exécutons avec le drapeau `-race`.
$ go run atomic-counters.go
ops: 50000

# Ensuite, nous examinerons les mutex, un autre outil pour gérer
# l'état.
```
