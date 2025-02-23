# Compteurs atomiques

Le problème consiste à incrémenter un compteur exactement 1000 fois en utilisant 50 goroutines et le package `sync/atomic`.

- Utilisez le package `sync/atomic` pour incrémenter le compteur.
- Utilisez un WaitGroup pour attendre que toutes les goroutines aient terminé leur travail.

```sh
# Nous nous attendons à obtenir exactement 50 000 opérations. Si nous
# avions utilisé l'incrémentation non atomique `ops++` pour incrémenter le compteur,
# nous obtiendrions probablement un nombre différent, variant d'une exécution
# à l'autre, car les goroutines se interféreraient mutuellement. De plus,
# nous obtiendrions des erreurs de course de données lorsque nous exécutons
# avec le drapeau `-race`.
$ go run atomic-counters.go
ops: 50000

# Ensuite, nous examinerons les mutexes, un autre outil pour gérer
# l'état.
```

Voici le code complet ci-dessous :

```go
// Le principal mécanisme pour gérer l'état en Go est
// la communication via des canaux. Nous l'avons vu par exemple
// avec [les pools de travailleurs](worker-pools). Il existe cependant
// quelques autres options pour gérer l'état. Ici, nous allons
// examiner l'utilisation du package `sync/atomic` pour les _compteurs
// atomiques_ accessibles par plusieurs goroutines.

package main

import (
	"fmt"
	"sync"
	"sync/atomic"
)

func main() {

	// Nous utiliserons un entier non signé pour représenter notre
	// compteur (toujours positif).
	var ops uint64

	// Un WaitGroup nous aidera à attendre que toutes les goroutines
	// aient terminé leur travail.
	var wg sync.WaitGroup

	// Nous démarrerons 50 goroutines qui chacune incrémenteront le
	// compteur exactement 1000 fois.
	for i := 0; i < 50; i++ {
		wg.Add(1)

		go func() {
			for c := 0; c < 1000; c++ {
				// Pour incrémenter le compteur de manière atomique, nous
				// utilisons `AddUint64`, en lui donnant l'adresse mémoire
				// de notre compteur `ops` avec la syntaxe `&`.
				atomic.AddUint64(&ops, 1)
			}
			wg.Done()
		}()
	}

	// Attendez jusqu'à ce que toutes les goroutines soient terminées.
	wg.Wait()

	// Il est sûr d'accéder à `ops` maintenant car nous savons
	// qu'aucune autre goroutine n'écrit dessus. Il est également
	// possible de lire les atomiques de manière sûre pendant qu'elles
	// sont mises à jour, en utilisant des fonctions telles que
	// `atomic.LoadUint64`.
	fmt.Println("ops:", ops)
}

```
