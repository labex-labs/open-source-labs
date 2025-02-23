# Recover

Die `mayPanic`-Funktion im bereitgestellten Code wird aufgerufen, wenn sie aufgerufen wird. Ihre Aufgabe besteht darin, die `main`-Funktion zu ändern, um von der Panik zurückzukehren und die Fehlermeldung auszugeben.

- Verwenden Sie die `recover`-Funktion, um die Panik in der `mayPanic`-Funktion zu behandeln.
- Geben Sie die Fehlermeldung aus, wenn eine Panik auftritt.

```sh
$ go run recover.go
Recovered. Error:
a problem
```

Hier ist der vollständige Code:

```go
// Go ermöglicht es, von einer Panik zurückzukehren, indem
// die integrierte Funktion `recover` verwendet wird. Ein `recover` kann
// verhindern, dass eine Panik das Programm abbricht und lässt es
// stattdessen fortfahren.

// Ein Beispiel, wo dies nützlich sein kann: Ein Server
// möchte nicht abstürzen, wenn eine der Clientverbindungen
// einen kritischen Fehler aufweist. Stattdessen möchte der Server
// die Verbindung schließen und weiterhin andere Clients bedienen.
// Tatsächlich macht dies Go's `net/http` standardmäßig für HTTP-Server.

package main

import "fmt"

// Diese Funktion stößt eine Panik aus.
func mayPanic() {
	panic("a problem")
}

func main() {
	// `recover` muss innerhalb einer deferenzierten Funktion aufgerufen werden.
	// Wenn die umschließende Funktion in Panik gerät, wird die defer
	// aktiviert und ein `recover`-Aufruf darin wird die Panik fangen.
	defer func() {
		if r := recover(); r!= nil {
			// Der Rückgabewert von `recover` ist der Fehler, der in
			// dem Aufruf von `panic` ausgelöst wurde.
			fmt.Println("Recovered. Error:\n", r)
		}
	}()

	mayPanic()

	// Dieser Code wird nicht ausgeführt, da `mayPanic` in Panik gerät.
	// Die Ausführung von `main` stoppt am Punkt der Panik und setzt sich
	// in der deferenzierten Schließung fort.
	fmt.Println("After mayPanic()")
}

```
