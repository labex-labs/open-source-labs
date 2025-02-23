# Kanalsynchronisierung

Das Problem, das in diesem Labor gelöst werden soll, besteht darin, eine Goroutine zu erstellen, die eine bestimmte Aufgabe ausführt und eine andere Goroutine über einen Kanal benachrichtigt, wenn die Aufgabe abgeschlossen ist.

Um dieses Labor abzuschließen, müssen Sie Folgendes tun:

- Erstellen Sie eine Funktion namens `worker`, die einen Kanal vom Typ `bool` als Parameter akzeptiert.
- Innerhalb der `worker`-Funktion führen Sie einige Arbeit durch und senden dann einen Wert an den Kanal, um zu signalisieren, dass die Arbeit abgeschlossen ist.
- In der `main`-Funktion erstellen Sie einen Kanal vom Typ `bool` mit einer Puffergröße von 1.
- Starten Sie eine Goroutine, die die `worker`-Funktion aufruft und den Kanal als Parameter übergibt.
- Blockieren Sie die `main`-Funktion, bis ein Wert vom Kanal empfangen wird.

```sh
$ go run channel-synchronization.go
working...done

# Wenn Sie die Zeile `<- done` aus diesem Programm entfernt hätten,
# würde das Programm bereits vor dem Start der `worker`-Goroutine beenden.
```

Hier ist der vollständige Code:

```go
// Wir können Kanäle verwenden, um die Ausführung zwischen Goroutines zu synchronisieren.
// Hier ist ein Beispiel für die Verwendung eines blockierenden Empfangs, um auf das
// Ende einer Goroutine zu warten. Wenn Sie auf das Ende mehrerer Goroutines warten,
// können Sie stattdessen eine [WaitGroup](waitgroups) verwenden.

package main

import (
	"fmt"
	"time"
)

// Dies ist die Funktion, die wir in einer Goroutine ausführen werden. Der
// `done`-Kanal wird verwendet, um eine andere Goroutine zu benachrichtigen,
// dass die Arbeit dieser Funktion abgeschlossen ist.
func worker(done chan bool) {
	fmt.Print("working...")
	time.Sleep(time.Second)
	fmt.Println("done")

	// Senden Sie einen Wert, um zu signalisieren, dass wir fertig sind.
	done <- true
}

func main() {

	// Starten Sie eine worker-Goroutine und übergeben Sie ihr den Kanal,
	// über den benachrichtigt werden soll.
	done := make(chan bool, 1)
	go worker(done)

	// Blockieren Sie, bis wir eine Benachrichtigung von der worker-Goroutine
	// über den Kanal erhalten.
	<-done
}

```
