# Select

In diesem Labor erhältst du zwei Kanäle, `c1` und `c2`, die nach einer gewissen Zeit einen Wert empfangen werden. Deine Aufgabe besteht darin, `select` zu verwenden, um beide Werte gleichzeitig abzuwarten und jeden Wert, sobald er eintrifft, auszugeben.

- Du sollst die `select`-Anweisung verwenden, um auf beiden Kanälen zu warten.
- Du sollst den empfangenen Wert von jedem Kanal ausgeben, sobald er eintrifft.

```sh
# Wir empfangen die Werte `"one"` und dann `"two"` wie
# erwartet.
$ time go run select.go
empfangen one
empfangen two

# Beachte, dass die gesamte Ausführungszeit nur etwa 2 Sekunden beträgt,
# da sowohl die 1- als auch die 2-Sekunden-`Sleeps` gleichzeitig ausgeführt werden.
real 0m2.245s
```

Hier ist der vollständige Code:

```go
// Go's _select_ ermöglicht es dir, auf mehrere Kanaloperationen zu warten.
// Die Kombination von Goroutinen und Kanälen mit select ist eine leistungsstarke Eigenschaft von Go.

package main

import (
	"fmt"
	"time"
)

func main() {

	// Für unser Beispiel werden wir über zwei Kanäle selektieren.
	c1 := make(chan string)
	c2 := make(chan string)

	// Jeder Kanal wird nach einer gewissen Zeit einen Wert empfangen, um z.B. blockierende RPC-Operationen zu simulieren,
	// die in parallelen Goroutinen ausgeführt werden.
	go func() {
		time.Sleep(1 * time.Second)
		c1 <- "one"
	}()
	go func() {
		time.Sleep(2 * time.Second)
		c2 <- "two"
	}()

	// Wir werden `select` verwenden, um beide Werte gleichzeitig abzuwarten und jeden Wert, sobald er eintrifft, auszugeben.
	for i := 0; i < 2; i++ {
		select {
		case msg1 := <-c1:
			fmt.Println("empfangen", msg1)
		case msg2 := <-c2:
			fmt.Println("empfangen", msg2)
		}
	}
}

```
