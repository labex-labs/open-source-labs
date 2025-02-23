# Select

Dans ce laboratoire, vous recevez deux canaux, `c1` et `c2`, qui recevront une valeur après un certain laps de temps. Votre tâche consiste à utiliser `select` pour attendre simultanément les deux valeurs, en affichant chacune lorsqu'elle arrive.

- Vous devriez utiliser l'instruction `select` pour attendre sur les deux canaux.
- Vous devriez afficher la valeur reçue de chaque canal lorsqu'elle arrive.

```sh
# Nous recevons les valeurs `"one"` puis `"two"` comme
# prévu.
$ time go run select.go
received one
received two

# Notez que le temps d'exécution total est d'environ 2 secondes
# car les `Sleeps` de 1 et 2 secondes s'exécutent
# concurremment.
real 0m2.245s
```

Voici le code complet ci-dessous :

```go
// Le _select_ de Go vous permet d'attendre plusieurs opérations sur des canaux.
// Combiner des goroutines et des canaux avec
// select est une fonctionnalité puissante de Go.

package main

import (
	"fmt"
	"time"
)

func main() {

	// Pour notre exemple, nous allons sélectionner sur deux canaux.
	c1 := make(chan string)
	c2 := make(chan string)

	// Chaque canal recevra une valeur après un certain laps de temps,
	// pour simuler par exemple des opérations RPC bloquantes
	// s'exécutant dans des goroutines concourantes.
	go func() {
		time.Sleep(1 * time.Second)
		c1 <- "one"
	}()
	go func() {
		time.Sleep(2 * time.Second)
		c2 <- "two"
	}()

	// Nous utiliserons `select` pour attendre simultanément les deux valeurs
	// et afficher chacune lorsqu'elle arrive.
	for i := 0; i < 2; i++ {
		select {
		case msg1 := <-c1:
			fmt.Println("received", msg1)
		case msg2 := <-c2:
			fmt.Println("received", msg2)
		}
	}
}

```
