# waitgroups

Das Problem, das in diesem Labor gelöst werden soll, besteht darin, mehrere Goroutinen zu starten und für jede die Wartegruppen-Zähler zu erhöhen. Anschließend müssen wir auf das Abschluss aller gestarteten Goroutinen warten.

- Grundkenntnisse von Golang.
- Verständnis der Parallelität in Golang.
- Vertrautheit mit dem `sync`-Paket.

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

# Die Reihenfolge, in der die Worker starten und beenden,
# wird bei jeder Ausführung wahrscheinlich unterschiedlich sein.
```

Hier ist der vollständige Code:

```go
// Um auf mehrere Goroutinen zu warten, die abgeschlossen sind, können wir
// eine *Wartegruppe* verwenden.

package main

import (
	"fmt"
	"sync"
	"time"
)

// Dies ist die Funktion, die wir in jeder Goroutine ausführen werden.
func worker(id int) {
	fmt.Printf("Worker %d starting\n", id)

	// Schlafen, um eine aufwendige Aufgabe zu simulieren.
	time.Sleep(time.Second)
	fmt.Printf("Worker %d done\n", id)
}

func main() {

	// Diese Wartegruppe wird verwendet, um auf das Abschluss aller
	// hier gestarteten Goroutinen zu warten. Hinweis: Wenn eine Wartegruppe
	// explizit an Funktionen übergeben wird, sollte dies *per Zeiger* geschehen.
	var wg sync.WaitGroup

	// Starten Sie mehrere Goroutinen und erhöhen Sie die Wartegruppen-Zähler
	// für jede.
	for i := 1; i <= 5; i++ {
		wg.Add(1)
		// Vermeiden Sie die Wiederverwendung des gleichen `i`-Werts in jeder
		// Goroutine-Schließung.
		// Siehe [die FAQ](https://golang.org/doc/faq#closures_and_goroutines)
		// für weitere Details.
		i := i

		// Verpacken Sie den Worker-Aufruf in eine Schließung, die sicherstellt,
		// dass die Wartegruppe benachrichtigt wird, dass dieser Worker abgeschlossen ist.
		// Auf diese Weise muss der Worker selbst nicht über die in seiner Ausführung
		// involvierten Parallelitätsprimitive Bescheid wissen.
		go func() {
			defer wg.Done()
			worker(i)
		}()
	}

	// Blockieren Sie, bis der Wartegruppen-Zähler wieder auf 0 geht;
	// alle Worker haben benachrichtigt, dass sie abgeschlossen sind.
	wg.Wait()

	// Beachten Sie, dass diese Methode keinen einfachen Weg hat,
	// Fehler von den Arbeitern zu propagieren. Für fortgeschrittene
	// Anwendungsfälle sollten Sie die
	// [errgroup-Paket](https://pkg.go.dev/golang.org/x/sync/errgroup)
	// verwenden.
}

```
