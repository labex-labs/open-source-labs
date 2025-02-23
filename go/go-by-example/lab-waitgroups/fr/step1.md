# waitgroups

Le problème à résoudre dans ce laboratoire est de lancer plusieurs goroutines et d'incrémenter le compteur du WaitGroup pour chacune d'entre elles. Ensuite, nous devons attendre que toutes les goroutines lancées se terminent.

- Connaissance de base de Golang.
- Compréhension de la concurrence en Golang.
- Familiarité avec le package `sync`.

```sh
$ go run waitgroups.go
Worker 5 starting
Worker 3 starting
Worker 4 starting
Worker 1 starting
Worker 2 starting
Worker 4 done
Worker 1 done
Worker 2 done
Worker 5 done
Worker 3 done

# L'ordre dans lequel les workers démarrent et se terminent
# est probablement différent pour chaque invocation.
```

Voici le code complet ci-dessous :

```go
// Pour attendre que plusieurs goroutines se terminent, on peut
// utiliser un *groupe d'attente*.

package main

import (
	"fmt"
	"sync"
	"time"
)

// Cette fonction sera exécutée dans chaque goroutine.
func worker(id int) {
	fmt.Printf("Worker %d starting\n", id)

	// Dormir pour simuler une tâche coûteuse.
	time.Sleep(time.Second)
	fmt.Printf("Worker %d done\n", id)
}

func main() {

	// Ce WaitGroup est utilisé pour attendre que toutes les
	// goroutines lancées ici se terminent. Note : si un WaitGroup est
	// explicitement passé en paramètre de fonctions, il doit être fait
	// *par pointeur*.
	var wg sync.WaitGroup

	// Lancer plusieurs goroutines et incrémenter le compteur du
	// WaitGroup pour chacune d'entre elles.
	for i := 1; i <= 5; i++ {
		wg.Add(1)
		// Éviter d'utiliser la même valeur de `i` dans chaque fermeture de goroutine.
		// Voir [la FAQ](https://golang.org/doc/faq#closures_and_goroutines)
		// pour plus de détails.
		i := i

		// Envelopper l'appel à worker dans une fermeture qui s'assure de dire
		// au WaitGroup que ce worker est terminé. De cette manière, le worker
		// lui-même n'a pas besoin d'être au courant des primitives de concurrence
		// impliquées dans son exécution.
		go func() {
			defer wg.Done()
			worker(i)
		}()
	}

	// Bloquer jusqu'à ce que le compteur du WaitGroup revienne à 0 ;
	// tous les workers ont été notifiés qu'ils étaient terminés.
	wg.Wait()

	// Notez que cette approche n'a pas de manière directe
	// de propager les erreurs provenant des workers. Pour des cas
	// d'utilisation plus avancés, considérez utiliser le
	// [package errgroup](https://pkg.go.dev/golang.org/x/sync/errgroup).
}

```
