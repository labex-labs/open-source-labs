# Worker-Pools

Implementieren Sie einen Worker-Pool, der Arbeit über den `jobs`-Kanal empfängt und die entsprechenden Ergebnisse über den `results`-Kanal sendet. Der Worker-Pool sollte mehrere parallele Instanzen haben, und jeder Worker sollte pro Aufgabe eine Sekunde schlafen, um eine aufwendige Aufgabe zu simulieren.

- Verwenden Sie Goroutines und Kanäle, um den Worker-Pool zu implementieren.
- Der Worker-Pool sollte mehrere parallele Instanzen haben.
- Jeder Worker sollte pro Aufgabe eine Sekunde schlafen, um eine aufwendige Aufgabe zu simulieren.
- Der Worker-Pool sollte Arbeit über den `jobs`-Kanal empfangen und die entsprechenden Ergebnisse über den `results`-Kanal senden.

```sh
# Unser laufendes Programm zeigt die 5 Aufgaben, die von
# verschiedenen Arbeitern ausgeführt werden. Das Programm
# benötigt nur etwa 2 Sekunden, obwohl insgesamt etwa
# 5 Sekunden Arbeit zu erledigen sind, weil
# 3 Arbeiter gleichzeitig arbeiten.
$ time go run worker-pools.go
worker 1 started job 1
worker 2 started job 2
worker 3 started job 3
worker 1 finished job 1
worker 1 started job 4
worker 2 finished job 2
worker 2 started job 5
worker 3 finished job 3
worker 1 finished job 4
worker 2 finished job 5

real 0m2.358s
```

Hier ist der vollständige Code:

```go
// In diesem Beispiel werden wir uns ansehen, wie man
// einen _Worker-Pool_ mit Goroutines und Kanälen implementiert.

package main

import (
	"fmt"
	"time"
)

// Hier ist der Worker, von dem wir mehrere
// parallele Instanzen ausführen werden. Diese Worker
// werden Arbeit über den `jobs`-Kanal empfangen und
// die entsprechenden Ergebnisse über `results` senden.
// Wir werden pro Aufgabe eine Sekunde schlafen, um
// eine aufwendige Aufgabe zu simulieren.
func worker(id int, jobs <-chan int, results chan<- int) {
	for j := range jobs {
		fmt.Println("worker", id, "started  job", j)
		time.Sleep(time.Second)
		fmt.Println("worker", id, "finished job", j)
		results <- j * 2
	}
}

func main() {

	// Um unseren Worker-Pool zu verwenden, müssen wir
	// ihnen Arbeit senden und ihre Ergebnisse sammeln.
	// Wir erstellen dazu 2 Kanäle.
	const numJobs = 5
	jobs := make(chan int, numJobs)
	results := make(chan int, numJobs)

	// Dies startet 3 Arbeiter, die zunächst blockiert
	// sind, da noch keine Aufgaben vorliegen.
	for w := 1; w <= 3; w++ {
		go worker(w, jobs, results)
	}

	// Hier senden wir 5 `jobs` und schließen dann
	// diesen Kanal, um anzuzeigen, dass das alles ist,
	// was wir zu tun haben.
	for j := 1; j <= numJobs; j++ {
		jobs <- j
	}
	close(jobs)

	// Schließlich sammeln wir alle Ergebnisse der Arbeit.
	// Dies stellt auch sicher, dass die Worker-Goroutines
	// beendet sind. Ein alternativer Weg, um auf mehrere
	// Goroutines zu warten, ist es, eine [WaitGroup](waitgroups) zu verwenden.
	for a := 1; a <= numJobs; a++ {
		<-results
	}
}

```
