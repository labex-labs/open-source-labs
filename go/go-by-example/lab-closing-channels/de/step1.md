# Kanäle schließen

In diesem Lab müssen Sie den gegebenen Code ändern, um den `jobs`-Kanal zu schließen, wenn es keine weiteren Aufgaben für die Arbeiter gibt. Sie müssen auch den `done`-Kanal verwenden, um zu signalisieren, wenn alle Aufgaben abgeschlossen sind.

- Verwenden Sie einen gepufferten Kanal `jobs`, um Arbeit von der `main()`-Goroutine an eine Arbeits-Goroutine zu kommunizieren.
- Verwenden Sie einen Kanal `done`, um zu signalisieren, wenn alle Aufgaben abgeschlossen sind.
- Verwenden Sie eine Arbeits-Goroutine, um wiederholt von `jobs` zu empfangen mit `j, more := <-jobs`.
- Verwenden Sie die spezielle 2-Wert-Form des Empfangs, um auf `done` zu signalisieren, wenn alle Aufgaben abgeschlossen sind.
- Senden Sie 3 Aufgaben an die Arbeiter über den `jobs`-Kanal, und schließen Sie ihn anschließend.
- Verwenden Sie die [Synchronisation](channel-synchronization)-Methode, um auf die Arbeiter zu warten.

```sh
$ go run closing-channels.go
sent job 1
received job 1
sent job 2
received job 2
sent job 3
received job 3
sent all jobs
received all jobs

# Die Idee geschlossener Kanäle führt natürlich zu unserem nächsten
# Beispiel: `range` über Kanäle.
```

Hier ist der vollständige Code:

```go
// Ein _geschlossener_ Kanal signalisiert, dass keine weiteren Werte
// darauf gesendet werden werden. Dies kann nützlich sein, um die
// Fertigstellung an die Empfänger des Kanals zu kommunizieren.

package main

import "fmt"

// In diesem Beispiel verwenden wir einen `jobs`-Kanal, um
// Arbeit von der `main()`-Goroutine an eine Arbeits-Goroutine
// zu kommunizieren. Wenn wir keine weiteren Aufgaben für die
// Arbeiter haben, schließen wir den `jobs`-Kanal.
func main() {
	jobs := make(chan int, 5)
	done := make(chan bool)

	// Hier ist die Arbeits-Goroutine. Sie empfängt wiederholt
	// von `jobs` mit `j, more := <-jobs`. In dieser
	// speziellen 2-Wert-Form des Empfangs wird der `more`-Wert
	// `false` sein, wenn `jobs` geschlossen wurde und alle
	// Werte im Kanal bereits empfangen wurden. Wir verwenden
	// dies, um auf `done` zu signalisieren, wenn wir alle
	// unsere Aufgaben erledigt haben.
	go func() {
		for {
			j, more := <-jobs
			if more {
				fmt.Println("received job", j)
			} else {
				fmt.Println("received all jobs")
				done <- true
				return
			}
		}
	}()

	// Dies sendet 3 Aufgaben an die Arbeiter über den `jobs`-
	// Kanal und schließt ihn anschließend.
	for j := 1; j <= 3; j++ {
		jobs <- j
		fmt.Println("sent job", j)
	}
	close(jobs)
	fmt.Println("sent all jobs")

	// Wir warten auf die Arbeiter, indem wir die
	// [Synchronisation](channel-synchronization)-Methode
	// verwenden, die wir zuvor gesehen haben.
	<-done
}

```
