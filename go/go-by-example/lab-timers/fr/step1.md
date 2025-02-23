# Timers

Le laboratoire nécessite la mise en œuvre d'un timer qui attend une durée spécifiée puis déclenche une action. De plus, le timer devrait être annulable avant son déclenchement.

- Le package `time` devrait être importé.
- Deux timers devraient être créés, l'un qui attend 2 secondes et l'autre qui attend 1 seconde.
- Le premier timer devrait afficher "Timer 1 fired" lorsqu'il déclenche.
- Le second timer devrait afficher "Timer 2 fired" lorsqu'il déclenche.
- Le second timer devrait être annulé avant son déclenchement.
- Le programme devrait attendre 2 secondes pour montrer que le second timer n'a pas déclenché.

```sh
// Le premier timer déclenchera environ 2 secondes après que
// nous ayons démarré le programme, mais le second devrait être
// arrêté avant qu'il ait eu le temps de déclencher.
$ go run timers.go
Timer 1 fired
Timer 2 stopped
```

Voici le code complet ci-dessous :

```go
// Nous souhaitons souvent exécuter du code Go à un moment donné
// dans le futur, ou de manière répétée à intervalles réguliers.
// Les fonctionnalités intégrées de _timer_ et _ticker_ de Go
// facilitent ces deux tâches. Nous examinerons tout d'abord les
// timers puis les [tickers](tickers).

package main

import (
	"fmt"
	"time"
)

func main() {

	// Les timers représentent un seul événement dans le futur. Vous
	// indiquez au timer combien de temps vous voulez attendre, et il
	// fournit un canal qui sera signalé à ce moment-là. Ce timer
	// attendra 2 secondes.
	timer1 := time.NewTimer(2 * time.Second)

	// Le `<-timer1.C` bloque sur le canal `C` du timer jusqu'à ce
	// qu'il envoie une valeur indiquant que le timer a déclenché.
	<-timer1.C
	fmt.Println("Timer 1 fired")

	// Si vous vouliez simplement attendre, vous auriez pu utiliser
	// `time.Sleep`. Une raison pour laquelle un timer peut être
	// utile est que vous pouvez annuler le timer avant qu'il ne
	// déclenche. Voici un exemple de cela.
	timer2 := time.NewTimer(time.Second)
	go func() {
		<-timer2.C
		fmt.Println("Timer 2 fired")
	}()
	stop2 := timer2.Stop()
	if stop2 {
		fmt.Println("Timer 2 stopped")
	}

	// Donnez au `timer2` suffisamment de temps pour déclencher, s'il
	// devait jamais le faire, pour montrer qu'il est effectivement
	// arrêté.
	time.Sleep(2 * time.Second)
}

```
