# Atomare Zähler

Das Problem besteht darin, einen Zähler genau 1000 Mal zu erhöhen, indem 50 Goroutinen und das Paket `sync/atomic` verwendet werden.

- Verwenden Sie das Paket `sync/atomic`, um den Zähler zu erhöhen.
- Verwenden Sie eine WaitGroup, um auf alle Goroutinen zu warten, bis sie ihre Arbeit beendet haben.

```sh
# Wir erwarten genau 50.000 Operationen. Hätten wir
# den nicht-atomaren `ops++` verwendet, um den Zähler
# zu erhöhen, würden wir wahrscheinlich eine andere
# Zahl erhalten, die zwischen den Ausführungen
# variiert, da die Goroutinen sich gegenseitig
# stören würden. Darüber hinaus würden wir bei der
# Ausführung mit der `-race`-Flagge Datenkonfliktfehler
# erhalten.
$ go run atomic-counters.go
ops: 50000

# Als nächstes werden wir uns Mutexs ansehen, ein anderes
# Werkzeug zum Verwalten des Zustands.
```

Hier ist der vollständige Code:

```go
// Der primäre Mechanismus zum Verwalten des Zustands in Go ist
// die Kommunikation über Kanäle. Wir haben das beispielsweise
// bei [Arbeitskräftepools](worker-pools) gesehen. Es gibt jedoch
// einige andere Optionen zum Verwalten des Zustands. Hier
// werden wir das Paket `sync/atomic` für _atomare Zähler_
// verwenden, die von mehreren Goroutinen zugegriffen werden.

package main

import (
	"fmt"
	"sync"
	"sync/atomic"
)

func main() {

	// Wir verwenden eine unsigned Integer, um unseren
	// (immer positiven) Zähler darzustellen.
	var ops uint64

	// Eine WaitGroup wird uns helfen, auf alle Goroutinen
	// zu warten, bis sie ihre Arbeit beendet haben.
	var wg sync.WaitGroup

	// Wir starten 50 Goroutinen, die jeweils den Zähler
	// genau 1000 Mal erhöhen.
	for i := 0; i < 50; i++ {
		wg.Add(1)

		go func() {
			for c := 0; c < 1000; c++ {
				// Um den Zähler atomar zu erhöhen, verwenden
				// wir `AddUint64` und geben ihm die Speicheradresse
				// unseres `ops`-Zählers mit der `&`-Syntax.
				atomic.AddUint64(&ops, 1)
			}
			wg.Done()
		}()
	}

	// Warten Sie, bis alle Goroutinen fertig sind.
	wg.Wait()

	// Es ist jetzt sicher, auf `ops` zuzugreifen, da wir wissen,
	// dass keine andere Goroutine darauf schreibt. Es ist auch
	// möglich, atomare Werte sicher zu lesen, während sie
	// aktualisiert werden, indem Funktionen wie
	// `atomic.LoadUint64` verwendet werden.
	fmt.Println("ops:", ops)
}

```
