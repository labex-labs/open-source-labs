# Mutexes

Le problème à résoudre dans ce défi est d'incrémenter un compteur nommé dans une boucle en utilisant plusieurs goroutines, et de s'assurer que l'accès au compteur est synchronisé.

## Exigences

- Utiliser une structure `Container` pour stocker une carte de compteurs.
- Utiliser un `Mutex` pour synchroniser l'accès à la carte `counters`.
- La structure `Container` devrait avoir une méthode `inc` qui prend une chaîne `name` et incrémente le compteur correspondant dans la carte `counters`.
- La méthode `inc` devrait verrouiller le mutex avant d'accéder à la carte `counters`, et le déverrouiller à la fin de la fonction en utilisant une instruction `defer`.
- Utiliser la structure `sync.WaitGroup` pour attendre que les goroutines se terminent.
- Utiliser la fonction `fmt.Println` pour afficher la carte `counters`.

## Exemple

```sh
# Exécution du programme montre que les compteurs
# sont mis à jour comme prévu.
$ go run mutexes.go
map[a:20000 b:10000]

# Ensuite, nous allons voir comment implémenter cette même tâche
# de gestion d'état en utilisant seulement des goroutines et des canaux.

```
