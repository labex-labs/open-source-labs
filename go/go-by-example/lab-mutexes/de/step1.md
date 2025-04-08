# Mutexes

Das Problem, das in diesem Labor gelöst werden soll, besteht darin, einen benannten Zähler in einer Schleife mithilfe mehrerer Goroutines zu erhöhen und sicherzustellen, dass der Zugang zum Zähler synchronisiert ist.

- Verwenden Sie eine `Container`-Struktur, um eine Map von Zählern zu speichern.
- Verwenden Sie ein `Mutex`, um den Zugang zur `counters`-Map zu synchronisieren.
- Die `Container`-Struktur sollte eine `inc`-Methode haben, die einen `name`-String annimmt und den entsprechenden Zähler in der `counters`-Map erhöht.
- Die `inc`-Methode sollte den Mutex vor dem Zugang zur `counters`-Map sperren und ihn am Ende der Funktion mit einem `defer`-Statement entsperren.
- Verwenden Sie die `sync.WaitGroup`-Struktur, um auf das Ende der Goroutines zu warten.
- Verwenden Sie die `fmt.Println`-Funktion, um die `counters`-Map auszugeben.

```sh
# Wenn das Programm ausgeführt wird, werden die Zähler
# wie erwartet aktualisiert.

# Als nächstes betrachten wir die Implementierung dieser
# gleichen Zustandsverwaltung mit nur Goroutines und Kanälen.
```

Hier ist der vollständige Code:

```go
// Im vorherigen Beispiel haben wir gesehen, wie einfache
// Zählerzustände mit [atomaren Operationen](atomic-counters) verwaltet werden.
// Für komplexere Zustände können wir ein [_Mutex_](https://en.wikipedia.org/wiki/Mutual_exclusion)
// verwenden, um Daten sicher über mehrere Goroutines hinweg zuzugreifen.

package main

import (
	"fmt"
	"sync"
)

// Container hält eine Map von Zählern; da wir sie
// von mehreren Goroutines gleichzeitig aktualisieren möchten,
// fügen wir ein `Mutex` hinzu, um den Zugang zu synchronisieren.
// Beachten Sie, dass Mutexes nicht kopiert werden dürfen,
// also sollte diese `struct` per Zeiger weitergegeben werden,
// wenn sie umgeleitet wird.
type Container struct {
	mu       sync.Mutex
	counters map[string]int
}

func (c *Container) inc(name string) {
	// Sperren Sie den Mutex, bevor Sie auf `counters` zugreifen; entsperren
	// Sie ihn am Ende der Funktion mit einem [defer](defer)-Statement.
	c.mu.Lock()
	defer c.mu.Unlock()
	c.counters[name]++
}

func main() {
	c := Container{
		// Beachten Sie, dass der Standardwert eines Mutexes direkt verwendbar ist,
		// also ist hier keine Initialisierung erforderlich.
		counters: map[string]int{"a": 0, "b": 0},
	}

	var wg sync.WaitGroup

	// Diese Funktion erhöht einen benannten Zähler
	// in einer Schleife.
	doIncrement := func(name string, n int) {
		for i := 0; i < n; i++ {
			c.inc(name)
		}
		wg.Done()
	}

	// Führen Sie mehrere Goroutines gleichzeitig aus; beachten Sie,
	// dass sie alle auf die gleiche `Container` zugreifen und zwei
	// von ihnen auf den gleichen Zähler zugreifen.
	wg.Add(3)
	go doIncrement("a", 10000)
	go doIncrement("a", 10000)
	go doIncrement("b", 10000)

	// Warten Sie auf das Ende der Goroutines
	wg.Wait()
	fmt.Println(c.counters)
}

```
