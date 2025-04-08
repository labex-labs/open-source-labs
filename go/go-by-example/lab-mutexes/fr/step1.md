# Mutexes

Le problème à résoudre dans ce laboratoire est d'incrémenter un compteur nommé dans une boucle en utilisant plusieurs goroutines, et de s'assurer que l'accès au compteur est synchronisé.

- Utiliser une structure `Container` pour stocker une carte de compteurs.
- Utiliser un `Mutex` pour synchroniser l'accès à la carte `counters`.
- La structure `Container` devrait avoir une méthode `inc` qui prend une chaîne de caractères `name` et incrémente le compteur correspondant dans la carte `counters`.
- La méthode `inc` devrait verrouiller le mutex avant d'accéder à la carte `counters`, et le déverrouiller à la fin de la fonction en utilisant une instruction `defer`.
- Utiliser la structure `sync.WaitGroup` pour attendre que les goroutines se terminent.
- Utiliser la fonction `fmt.Println` pour imprimer la carte `counters`.

```sh
# Exécution du programme montre que les compteurs
# sont mis à jour comme prévu.

# Ensuite, nous allons voir comment implémenter cette même tâche
# de gestion d'état en utilisant seulement des goroutines et des canaux.
```

Voici le code complet ci-dessous :

```go
// Dans l'exemple précédent, nous avons vu comment gérer un état
// de compteur simple en utilisant [opérations atomiques](atomic-counters).
// Pour un état plus complexe, nous pouvons utiliser un [_mutex_](https://en.wikipedia.org/wiki/Mutual_exclusion)
// pour accéder en toute sécurité à des données à travers plusieurs goroutines.

package main

import (
	"fmt"
	"sync"
)

// Container stocke une carte de compteurs ; comme nous voulons
// la mettre à jour de manière concurrente à partir de plusieurs goroutines,
// nous ajoutons un `Mutex` pour synchroniser l'accès.
// Notez que les mutexes ne doivent pas être copiés, donc si cette
// `struct` est passée en boucle, cela devrait être fait par
// pointeur.
type Container struct {
	mu       sync.Mutex
	counters map[string]int
}

func (c *Container) inc(name string) {
	// Verrouillez le mutex avant d'accéder à `counters` ; déverrouillez
	// le à la fin de la fonction en utilisant une instruction [defer](defer).
	c.mu.Lock()
	defer c.mu.Unlock()
	c.counters[name]++
}

func main() {
	c := Container{
		// Notez que la valeur zéro d'un mutex est utilisable telle quelle, donc
		// aucune initialisation n'est requise ici.
		counters: map[string]int{"a": 0, "b": 0},
	}

	var wg sync.WaitGroup

	// Cette fonction incrémente un compteur nommé
	// dans une boucle.
	doIncrement := func(name string, n int) {
		for i := 0; i < n; i++ {
			c.inc(name)
		}
		wg.Done()
	}

	// Exécutez plusieurs goroutines en parallèle ; notez
	// qu'elles accèdent toutes au même `Container`,
	// et deux d'entre elles accèdent au même compteur.
	wg.Add(3)
	go doIncrement("a", 10000)
	go doIncrement("a", 10000)
	go doIncrement("b", 10000)

	// Attendez que les goroutines se terminent
	wg.Wait()
	fmt.Println(c.counters)
}

```
