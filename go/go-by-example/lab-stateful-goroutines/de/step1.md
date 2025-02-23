# Zustandsbehaftete Goroutinen

Beim parallelen Programmieren ist es unerlässlich, den Zugang zu einem gemeinsamen Zustand zu synchronisieren, um Wettlaufbedingungen und Datenschädigungen zu vermeiden. In diesem Labor wird ein Szenario vorgestellt, in dem eine einzelne Goroutine den Zustand besitzt und andere Goroutinen Nachrichten senden, um den Zustand zu lesen oder zu schreiben.

- Verwenden Sie Kanäle, um Lesen- und Schreibanforderungen an die den Zustand besitzende Goroutine zu senden.
- Verwenden Sie die `readOp`- und `writeOp`-Strukturen, um Anforderungen und Antworten zu kapseln.
- Verwenden Sie eine Map, um den Zustand zu speichern.
- Verwenden Sie `resp`-Kanäle, um Erfolg und Rückgabewerte anzuzeigen.
- Verwenden Sie das `atomic`-Paket, um die Anzahl der Lesen- und Schreiboperationen zu zählen.
- Verwenden Sie das `time`-Paket, um eine Verzögerung zwischen den Operationen hinzuzufügen.

```sh
# Wenn wir unser Programm ausführen, zeigt sich, dass das
# Beispiel zur Zustandsverwaltung auf der Grundlage von
# Goroutinen insgesamt etwa 80.000 Operationen
# durchführt.
$ go run stateful-goroutines.go
readOps: 71708
writeOps: 7177

# Für diesen speziellen Fall war der auf Goroutinen
# basierende Ansatz etwas aufwendiger als der auf
# Mutex basierende. Er kann in bestimmten Fällen jedoch
# nützlich sein, beispielsweise wenn Sie andere Kanäle
# verwenden oder wenn das Verwalten mehrerer solcher
# Mutexe fehleranfällig wäre. Sie sollten den Ansatz
# verwenden, der Ihnen am natürlichsten erscheint,
# insbesondere was die Korrektheit Ihres Programms
# betrifft.
```

Hier ist der vollständige Code:

```go
// Im vorherigen Beispiel haben wir explizites Sperren mit
// [Mutexen](mutexes) verwendet, um den Zugang zu einem
// gemeinsamen Zustand über mehrere Goroutinen zu
// synchronisieren. Eine andere Option ist es, die
// eingebauten Synchronisationsfunktionen von Goroutinen
// und Kanälen zu verwenden, um das gleiche Ergebnis zu
// erzielen. Dieser auf Kanälen basierende Ansatz stimmt
// mit den Ideen von Go überein, den gemeinsamen Zustand
// über die Kommunikation zu teilen und jede Datenstelle
// genau von einer Goroutine zu besitzen.

package main

import (
	"fmt"
	"math/rand"
	"sync/atomic"
	"time"
)

// In diesem Beispiel wird unser Zustand von einer einzelnen
// Goroutine besessen. Dies gewährleistet, dass die Daten
// bei gleichzeitigem Zugang niemals beschädigt werden. Um
// diesen Zustand zu lesen oder zu schreiben, senden
// andere Goroutinen Nachrichten an die besitzende
// Goroutine und erhalten entsprechende Antworten. Diese
// `readOp`- und `writeOp`-`struct`s kapseln diese
// Anforderungen und eine Möglichkeit für die besitzende
// Goroutine, zu antworten.
type readOp struct {
	key  int
	resp chan int
}
type writeOp struct {
	key  int
	val  int
	resp chan bool
}

func main() {

	// Wie zuvor zählen wir, wie viele Operationen wir
	// ausführen.
	var readOps uint64
	var writeOps uint64

	// Die `reads`- und `writes`-Kanäle werden von anderen
	// Goroutinen verwendet, um jeweils Lesen- und
	// Schreibanforderungen zu senden.
	reads := make(chan readOp)
	writes := make(chan writeOp)

	// Hier ist die Goroutine, die den `state` besitzt,
	// der wie im vorherigen Beispiel eine Map ist, aber
	// jetzt privat für die zustandsbehaftete Goroutine.
	// Diese Goroutine wählt wiederholt auf den `reads`-
	// und `writes`-Kanälen und antwortet auf Anforderungen,
	// sobald sie eintreffen. Eine Antwort wird ausgeführt,
	// indem zunächst die angeforderte Operation durchgeführt
	// wird und dann ein Wert über den Antwortkanal `resp`
	// gesendet wird, um Erfolg anzuzeigen (und den gewünschten
	// Wert im Falle von `reads`).
	go func() {
		var state = make(map[int]int)
		for {
			select {
			case read := <-reads:
				read.resp <- state[read.key]
			case write := <-writes:
				state[write.key] = write.val
				write.resp <- true
			}
		}
	}()

	// Hier werden 100 Goroutinen gestartet, um über den
	// `reads`-Kanal Lesen an die den Zustand besitzende
	// Goroutine zu senden. Jede Leseoperation erfordert die
	// Konstruktion eines `readOp`, das über den `reads`-
	// Kanal gesendet und das Ergebnis über den bereitgestellten
	// `resp`-Kanal empfangen zu werden.
	for r := 0; r < 100; r++ {
		go func() {
			for {
				read := readOp{
					key:  rand.Intn(5),
					resp: make(chan int)}
				reads <- read
				<-read.resp
				atomic.AddUint64(&readOps, 1)
				time.Sleep(time.Millisecond)
			}
		}()
	}

	// Wir starten ebenfalls 10 Schreiboperationen, indem wir
	// einen ähnlichen Ansatz verwenden.
	for w := 0; w < 10; w++ {
		go func() {
			for {
				write := writeOp{
					key:  rand.Intn(5),
					val:  rand.Intn(100),
					resp: make(chan bool)}
				writes <- write
				<-write.resp
				atomic.AddUint64(&writeOps, 1)
				time.Sleep(time.Millisecond)
			}
		}()
	}

	// Lassen Sie die Goroutinen für eine Sekunde arbeiten.
	time.Sleep(time.Second)

	// Schließlich erfassen und melden Sie die Op-Zählungen.
	readOpsFinal := atomic.LoadUint64(&readOps)
	fmt.Println("readOps:", readOpsFinal)
	writeOpsFinal := atomic.LoadUint64(&writeOps)
	fmt.Println("writeOps:", writeOpsFinal)
}

```
