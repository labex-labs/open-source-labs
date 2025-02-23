# Goroutines avec état

En programmation concurrente, il est essentiel de synchroniser l'accès à un état partagé pour éviter les conditions de course et la corruption des données. Ce laboratoire présente un scénario où une seule goroutine possède l'état, et les autres goroutines envoient des messages pour lire ou écrire l'état.

- Utiliser des canaux pour émettre des requêtes de lecture et d'écriture à la goroutine propriétaire de l'état.
- Utiliser les structs `readOp` et `writeOp` pour encapsuler les requêtes et les réponses.
- Utiliser une carte pour stocker l'état.
- Utiliser des canaux `resp` pour indiquer le succès et renvoyer des valeurs.
- Utiliser le package `atomic` pour compter les opérations de lecture et d'écriture.
- Utiliser le package `time` pour ajouter un délai entre les opérations.

```sh
# En exécutant notre programme, on constate que l'exemple
# de gestion d'état basé sur les goroutines effectue
# environ 80 000 opérations au total.
$ go run stateful-goroutines.go
readOps: 71708
writeOps: 7177

# Dans ce cas particulier, l'approche basée sur les
# goroutines était un peu plus complexe que celle
# basée sur les mutex. Elle peut toutefois s'avérer
# utile dans certains cas, par exemple lorsque vous
# avez d'autres canaux impliqués ou lorsque la gestion
# de plusieurs mutex serait propice à des erreurs. Vous
# devriez utiliser l'approche qui vous semble la plus
# naturelle, en particulier en ce qui concerne la
# compréhension de la correction de votre programme.
```

Voici le code complet ci-dessous :

```go
// Dans l'exemple précédent, nous avons utilisé un verrouillage
// explicite avec des [mutex](mutexes) pour synchroniser
// l'accès à un état partagé entre plusieurs goroutines.
// Une autre option est d'utiliser les fonctionnalités
// de synchronisation intégrées des goroutines et des
// canaux pour obtenir le même résultat. Cette approche
// basée sur les canaux est conforme aux idées de Go
// sur le partage de mémoire en communiquant et en
// donnant à chaque morceau de données un propriétaire
// unique, une goroutine.

package main

import (
	"fmt"
	"math/rand"
	"sync/atomic"
	"time"
)

// Dans cet exemple, notre état sera détenu par une seule
// goroutine. Cela garantira que les données ne seront
// jamais corrompues par un accès concurrent. Pour lire
// ou écrire cet état, les autres goroutines enverront
// des messages à la goroutine propriétaire et recevront
// des réponses correspondantes. Ces structs `readOp`
// et `writeOp` encapsulent ces requêtes et un moyen
// pour la goroutine propriétaire de répondre.
type readOp struct {
	key  int
	resp chan int
}
type writeOp struct {
	key  int
	val  int
	resp chan bool
}

func main() {

	// Comme avant, nous allons compter le nombre
	// d'opérations que nous effectuons.
	var readOps uint64
	var writeOps uint64

	// Les canaux `reads` et `writes` seront utilisés
	// par les autres goroutines pour émettre respectivement
	// des requêtes de lecture et d'écriture.
	reads := make(chan readOp)
	writes := make(chan writeOp)

	// Voici la goroutine qui possède l'`état`, qui est
	// une carte comme dans l'exemple précédent, mais
	// maintenant privée à la goroutine avec état. Cette
	// goroutine sélectionne répétitivement sur les canaux
	// `reads` et `writes`, répondant aux requêtes à
	// mesure qu'elles arrivent. Une réponse est exécutée
	// en premier en effectuant l'opération demandée, puis
	// en envoyant une valeur sur le canal de réponse
	// `resp` pour indiquer le succès (et la valeur
	// souhaitée dans le cas de `reads`).
	go func() {
		var state = make(map[int]int)
		for {
			select {
			case read := <-reads:
				read.resp <- state[read.key]
			case write := <-writes:
				state[write.key] = write.val
				write.resp <- true
			}
		}
	}()

	// Cela lance 100 goroutines pour émettre des lectures
	// à la goroutine propriétaire de l'état via le canal
	// `reads`. Chaque lecture nécessite de construire un
	// `readOp`, de l'envoyer sur le canal `reads`, puis
	// de recevoir le résultat sur le canal `resp` fourni.
	for r := 0; r < 100; r++ {
		go func() {
			for {
				read := readOp{
					key:  rand.Intn(5),
					resp: make(chan int)}
				reads <- read
				<-read.resp
				atomic.AddUint64(&readOps, 1)
				time.Sleep(time.Millisecond)
			}
		}()
	}

	// Nous lançons également 10 écritures, en utilisant
	// une approche similaire.
	for w := 0; w < 10; w++ {
		go func() {
			for {
				write := writeOp{
					key:  rand.Intn(5),
					val:  rand.Intn(100),
					resp: make(chan bool)}
				writes <- write
				<-write.resp
				atomic.AddUint64(&writeOps, 1)
				time.Sleep(time.Millisecond)
			}
		}()
	}

	// Laissez les goroutines travailler pendant une seconde.
	time.Sleep(time.Second)

	// Enfin, capturez et rapportez les comptes d'opérations.
	readOpsFinal := atomic.LoadUint64(&readOps)
	fmt.Println("readOps:", readOpsFinal)
	writeOpsFinal := atomic.LoadUint64(&writeOps)
	fmt.Println("writeOps:", writeOpsFinal)
}

```
