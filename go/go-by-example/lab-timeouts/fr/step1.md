# Timeouts

Lorsque les programmes se connectent à des ressources externes ou ont besoin de limiter le temps d'exécution, les délais d'attente sont importants. Dans ce laboratoire, nous allons implémenter des délais d'attente en Go à l'aide de canaux et de `select`.

- Implémentez des délais d'attente en Go à l'aide de canaux et de `select`.
- Utilisez un canal tamponné pour éviter les fuites de goroutine au cas où le canal n'est jamais lu.
- Utilisez `time.After` pour attendre qu'une valeur soit envoyée après le délai d'attente.
- Utilisez `select` pour passer à la première réception prête.

```sh
# Exécution de ce programme montre que la première opération
# atteint le délai d'attente et que la seconde réussit.
$ go run timeouts.go
timeout 1
result 2
```

Voici le code complet ci-dessous :

```go
// Les _Timeouts_ sont importants pour les programmes qui se
// connectent à des ressources externes ou qui ont autrement
// besoin de limiter le temps d'exécution. Implémenter des
// délais d'attente en Go est facile et élégant grâce aux
// canaux et à `select`.

package main

import (
	"fmt"
	"time"
)

func main() {

	// Pour notre exemple, supposons que nous exécutons un
	// appel externe qui renvoie son résultat sur un canal
	// `c1` après 2 secondes. Notez que le canal est
	// tamponné, donc l'envoi dans la goroutine est
	// non-bloquant. C'est un motif courant pour éviter les
	// fuites de goroutine au cas où le canal n'est jamais lu.
	c1 := make(chan string, 1)
	go func() {
		time.Sleep(2 * time.Second)
		c1 <- "result 1"
	}()

	// Voici le `select` implémentant un délai d'attente.
	// `res := <-c1` attend le résultat et `<-time.After`
	// attend qu'une valeur soit envoyée après le délai
	// d'attente de 1 seconde. Comme `select` passe à la
	// première réception prête, nous prendrons le cas du
	// délai d'attente si l'opération prend plus de 1 seconde
	// autorisée.
	select {
	case res := <-c1:
		fmt.Println(res)
	case <-time.After(1 * time.Second):
		fmt.Println("timeout 1")
	}

	// Si nous autorisons un délai d'attente plus long de 3
	// secondes, alors la réception de `c2` réussira et nous
	// afficherons le résultat.
	c2 := make(chan string, 1)
	go func() {
		time.Sleep(2 * time.Second)
		c2 <- "result 2"
	}()
	select {
	case res := <-c2:
		fmt.Println(res)
	case <-time.After(3 * time.Second):
		fmt.Println("timeout 2")
	}
}

```
