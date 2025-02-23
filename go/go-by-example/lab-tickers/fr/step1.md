# Horloges et chronomètres

Dans ce laboratoire, vous devez créer un chronomètre qui sonne toutes les 500 ms jusqu'à ce que nous l'arrêtions. Vous utiliserez un canal pour attendre les valeurs à mesure qu'elles arrivent.

- Utilisez le package `time` pour créer un chronomètre.
- Utilisez un canal pour attendre les valeurs à mesure qu'elles arrivent.
- Utilisez l'instruction `select` pour recevoir les valeurs du canal.
- Arrêtez le chronomètre après 1600 ms.

```sh
# Lorsque nous exécutons ce programme, le chronomètre devrait sonner 3 fois
# avant que nous ne l'arrêtions.
$ go run tickers.go
Tick at 2012-09-23 11:29:56.487625 -0700 PDT
Tick at 2012-09-23 11:29:56.988063 -0700 PDT
Tick at 2012-09-23 11:29:57.488076 -0700 PDT
Ticker arrêté
```

Voici le code complet ci-dessous :

```go
// [Les horloges](timers) sont utilisées lorsque vous voulez faire
// quelque chose une fois dans le futur - les _chronomètres_ sont utilisés lorsque
// vous voulez faire quelque chose de manière répétée à intervalles réguliers. Voici un exemple d'un chronomètre qui sonne
// périodiquement jusqu'à ce que nous l'arrêtions.

package main

import (
	"fmt"
	"time"
)

func main() {

	// Les chronomètres utilisent un mécanisme similaire aux horloges : un
	// canal sur lequel des valeurs sont envoyées. Ici, nous utiliserons l'instruction
	// `select` sur le canal pour attendre les valeurs à mesure qu'elles arrivent toutes les 500 ms.
	ticker := time.NewTicker(500 * time.Millisecond)
	done := make(chan bool)

	go func() {
		for {
			select {
			case <-done:
				return
			case t := <-ticker.C:
				fmt.Println("Tick at", t)
			}
		}
	}()

	// Les chronomètres peuvent être arrêtés comme les horloges. Une fois qu'un chronomètre
	// est arrêté, il ne recevra plus de valeurs sur son canal. Nous l'arrêterons après 1600 ms.
	time.Sleep(1600 * time.Millisecond)
	ticker.Stop()
	done <- true
	fmt.Println("Ticker arrêté")
}

```
