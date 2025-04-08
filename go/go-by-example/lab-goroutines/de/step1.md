# Goroutinen

Das Problem, das in diesem Labor gelöst werden soll, ist es, Goroutinen zu erstellen und auszuführen, um Funktionen gleichzeitig auszuführen.

- Die `f`-Funktion sollte ihre Eingabezeichenfolge und eine Zählervariable dreimal ausgeben.
- Die `main`-Funktion sollte die `f`-Funktion synchron aufrufen und "direct" und eine Zählervariable dreimal ausgeben.
- Die `main`-Funktion sollte die `f`-Funktion asynchron mithilfe einer Goroutine aufrufen und "goroutine" und eine Zählervariable dreimal ausgeben.
- Die `main`-Funktion sollte eine Goroutine starten, um eine anonyme Funktion auszuführen, die eine Nachricht ausgibt.
- Die `main`-Funktion sollte auf die Fertigstellung der Goroutinen warten, bevor sie "done" ausgibt.

```sh
# Wenn wir dieses Programm ausführen, sehen wir zuerst die Ausgabe des
# blockierenden Aufrufs, dann die Ausgabe der beiden
# Goroutinen. Die Ausgabe der Goroutinen kann verzahnt sein,
# da die Goroutinen von der Go Laufzeit gleichzeitig ausgeführt werden.

# Als Nächstes betrachten wir einen Ergänzungsteil zu Goroutinen in
# parallelen Go-Programmen: Kanäle.
```

Hier ist der vollständige Code:

```go
// Eine _Goroutine_ ist ein leichter Ausführungsthread.

package main

import (
	"fmt"
	"time"
)

func f(from string) {
	for i := 0; i < 3; i++ {
		fmt.Println(from, ":", i)
	}
}

func main() {

	// Nehmen wir an, wir hätten einen Funktionsaufruf `f(s)`. Hier ist, wie
	// wir ihn auf die übliche Weise aufrufen würden, indem wir ihn
	// synchron ausführen.
	f("direct")

	// Um diese Funktion in einer Goroutine aufzurufen, verwenden wir
	// `go f(s)`. Diese neue Goroutine wird gleichzeitig mit der aufrufenden
	// ausgeführt.
	go f("goroutine")

	// Sie können auch eine Goroutine für einen anonymen
	// Funktionsaufruf starten.
	go func(msg string) {
		fmt.Println(msg)
	}("going")

	// Unsere beiden Funktionsaufrufe laufen jetzt asynchron in
	// separaten Goroutinen. Warten Sie, bis sie fertig sind
	// (für einen robusteren Ansatz verwenden Sie eine [WaitGroup](waitgroups)).
	time.Sleep(time.Second)
	fmt.Println("done")
}

```
