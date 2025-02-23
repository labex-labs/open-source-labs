# Goroutines avec état

En programmation concurrente, il est essentiel de synchroniser l'accès à un état partagé pour éviter les conditions de course et la corruption des données. Ce défi présente un scénario où une seule goroutine possède l'état, et les autres goroutines envoient des messages pour lire ou écrire l'état.

## Exigences

- Utiliser des canaux pour émettre des requêtes de lecture et d'écriture à la goroutine propriétaire de l'état.
- Utiliser les structs `readOp` et `writeOp` pour encapsuler les requêtes et les réponses.
- Utiliser une carte pour stocker l'état.
- Utiliser des canaux `resp` pour indiquer le succès et renvoyer des valeurs.
- Utiliser le package `atomic` pour compter les opérations de lecture et d'écriture.
- Utiliser le package `time` pour ajouter un délai entre les opérations.

## Exemple

```sh
# En exécutant notre programme, on constate que l'exemple
# de gestion d'état basé sur les goroutines effectue
# environ 80 000 opérations au total.
$ go run stateful-goroutines.go
readOps: 71708
writeOps: 7177

# Dans ce cas particulier, l'approche basée sur les
# goroutines était un peu plus complexe que celle basée
# sur les mutex. Elle peut toutefois s'avérer utile dans
# certains cas, par exemple lorsque vous avez d'autres
# canaux impliqués ou lorsque la gestion de plusieurs
# mutex de cette sorte serait propice à des erreurs. Vous
# devriez utiliser l'approche qui vous semble la plus
# naturelle, en particulier en ce qui concerne la
# compréhension de la correction de votre programme.
```
