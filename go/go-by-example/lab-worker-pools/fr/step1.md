# Worker Pools

Implémentez un pool de travailleurs qui reçoit des travaux sur le canal `jobs` et envoie les résultats correspondants sur le canal `results`. Le pool de travailleurs devrait avoir plusieurs instances concurrentes, et chaque travailleur devrait dormir une seconde par travail pour simuler une tâche coûteuse.

- Utilisez des goroutines et des canaux pour implémenter le pool de travailleurs.
- Le pool de travailleurs devrait avoir plusieurs instances concurrentes.
- Chaque travailleur devrait dormir une seconde par travail pour simuler une tâche coûteuse.
- Le pool de travailleurs devrait recevoir des travaux sur le canal `jobs` et envoyer les résultats correspondants sur le canal `results`.

```sh
# Notre programme en cours d'exécution montre les 5 travaux exécutés par
# divers travailleurs. Le programme ne prend que environ 2 secondes
# malgré un travail total d'environ 5 secondes car
# il y a 3 travailleurs qui opèrent en parallèle.
$ time go run worker-pools.go
worker 1 started job 1
worker 2 started job 2
worker 3 started job 3
worker 1 finished job 1
worker 1 started job 4
worker 2 finished job 2
worker 2 started job 5
worker 3 finished job 3
worker 1 finished job 4
worker 2 finished job 5

real 0m2.358s
```

Voici le code complet ci-dessous :

```go
// Dans cet exemple, nous allons voir comment implémenter
// un _pool de travailleurs_ à l'aide de goroutines et de canaux.

package main

import (
	"fmt"
	"time"
)

// Voici le travailleur, dont nous allons exécuter plusieurs
// instances concurrentes. Ces travailleurs recevront
// des travaux sur le canal `jobs` et enverront les résultats
// correspondants sur `results`. Nous dormirons une seconde par travail pour
// simuler une tâche coûteuse.
func worker(id int, jobs <-chan int, results chan<- int) {
	for j := range jobs {
		fmt.Println("worker", id, "started  job", j)
		time.Sleep(time.Second)
		fmt.Println("worker", id, "finished job", j)
		results <- j * 2
	}
}

func main() {

	// Pour utiliser notre pool de travailleurs, nous devons envoyer
	// des travaux et collecter leurs résultats. Nous créons 2
	// canaux pour cela.
	const numJobs = 5
	jobs := make(chan int, numJobs)
	results := make(chan int, numJobs)

	// Cela lance 3 travailleurs, initialement bloqués
	// car il n'y a pas encore de travaux.
	for w := 1; w <= 3; w++ {
		go worker(w, jobs, results)
	}

	// Ici, nous envoyons 5 `jobs` puis `fermons` ce
	// canal pour indiquer que c'est tout le travail que nous avons.
	for j := 1; j <= numJobs; j++ {
		jobs <- j
	}
	close(jobs)

	// Enfin, nous collectons tous les résultats du travail.
	// Cela garantit également que les goroutines de travail ont
	// fini. Une autre manière d'attendre plusieurs
	// goroutines est d'utiliser un [WaitGroup](waitgroups).
	for a := 1; a <= numJobs; a++ {
		<-results
	}
}

```
