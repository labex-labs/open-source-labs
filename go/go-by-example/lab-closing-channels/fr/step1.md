# Fermeture des canaux

Dans ce laboratoire, vous devez modifier le code fourni pour fermer le canal `jobs` lorsqu'il n'y a plus de tâches pour le travailleur. Vous devez également utiliser le canal `done` pour être informé lorsque toutes les tâches ont été terminées.

- Utilisez un canal tamponné `jobs` pour communiquer les travaux à effectuer du goroutine `main()` à une goroutine de travail.
- Utilisez un canal `done` pour être informé lorsque toutes les tâches ont été terminées.
- Utilisez une goroutine de travail pour recevoir répétitivement de `jobs` avec `j, more := <-jobs`.
- Utilisez la forme à 2 valeurs spéciale de la réception pour être informé sur `done` lorsque toutes les tâches ont été terminées.
- Envoyez 3 tâches au travailleur via le canal `jobs`, puis fermez-le.
- Utilisez l'approche de [synchronisation](channel-synchronization) pour attendre le travailleur.

```sh
$ go run closing-channels.go
sent job 1
received job 1
sent job 2
received job 2
sent job 3
received job 3
sent all jobs
received all jobs

# L'idée des canaux fermés conduit naturellement à notre prochain
# exemple : `range` sur des canaux.
```

Voici le code complet ci-dessous :

```go
// _Fermer_ un canal indique qu'aucune valeur supplémentaire
// ne sera envoyée dessus. Cela peut être utile pour communiquer
// la fin aux récepteurs du canal.

package main

import "fmt"

// Dans cet exemple, nous utiliserons un canal `jobs` pour
// communiquer les travaux à effectuer du goroutine `main()`
// à une goroutine de travail. Lorsque nous n'avons plus de tâches
// pour le travailleur, nous allons `fermer` le canal `jobs`.
func main() {
	jobs := make(chan int, 5)
	done := make(chan bool)

	// Voici la goroutine de travail. Elle reçoit répétitivement
	// de `jobs` avec `j, more := <-jobs`. Dans cette
	// forme spéciale à 2 valeurs de la réception, la valeur
	// `more` sera `false` si `jobs` a été `fermé` et toutes
	// les valeurs du canal ont déjà été reçues.
	// Nous utilisons cela pour être informé sur `done` lorsque
	// nous avons terminé toutes nos tâches.
	go func() {
		for {
			j, more := <-jobs
			if more {
				fmt.Println("received job", j)
			} else {
				fmt.Println("received all jobs")
				done <- true
				return
			}
		}
	}()

	// Cela envoie 3 tâches au travailleur via le canal `jobs`,
	// puis le ferme.
	for j := 1; j <= 3; j++ {
		jobs <- j
		fmt.Println("sent job", j)
	}
	close(jobs)
	fmt.Println("sent all jobs")

	// Nous attendons le travailleur en utilisant l'approche
	// de [synchronisation](channel-synchronization) que nous
	// avons vue précédemment.
	<-done
}

```
