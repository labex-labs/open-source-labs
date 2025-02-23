# Timeouts

Wenn Programme sich an externe Ressourcen anschließen oder die Ausführungszeit begrenzen müssen, sind Timeouts wichtig. In diesem Lab wird die Implementierung von Timeouts in Go mit Hilfe von Kanälen und `select` behandelt.

- Implementieren Sie Timeouts in Go mit Hilfe von Kanälen und `select`.
- Verwenden Sie einen gepufferten Kanal, um Goroutine-Lecks zu vermeiden, falls der Kanal nie gelesen wird.
- Verwenden Sie `time.After`, um auf einen Wert zu warten, der nach Ablauf der Zeitüberschreitung gesendet wird.
- Verwenden Sie `select`, um mit der ersten empfangenen Nachricht fortzufahren, die bereit ist.

```sh
# Wenn Sie dieses Programm ausführen, wird die erste Operation
# aufgrund der Zeitüberschreitung fehlschlagen und die zweite
# erfolgreich abgeschlossen werden.
$ go run timeouts.go
timeout 1
result 2
```

Hier ist der vollständige Code:

```go
// _Timeouts_ sind wichtig für Programme, die sich an externe
// Ressourcen anschließen oder die anderweitig die Ausführungszeit
// begrenzen müssen. Die Implementierung von Timeouts in Go ist dank
// Kanälen und `select` einfach und elegant.

package main

import (
	"fmt"
	"time"
)

func main() {

	// Für unser Beispiel nehmen wir an, dass wir einen externen
	// Aufruf ausführen, der sein Ergebnis nach 2 Sekunden auf einem
	// Kanal `c1` zurückgibt. Beachten Sie, dass der Kanal gepuffert
	// ist, sodass das Senden in der Goroutine nicht blockiert. Dies
	// ist ein häufiges Muster, um Goroutine-Lecks zu vermeiden, falls
	// der Kanal nie gelesen wird.
	c1 := make(chan string, 1)
	go func() {
		time.Sleep(2 * time.Second)
		c1 <- "result 1"
	}()

	// Hier implementiert `select` einen Timeout.
	// `res := <-c1` wartet auf das Ergebnis und `<-time.After`
	// wartet auf einen Wert, der nach Ablauf der Zeitüberschreitung
	// von 1 Sekunde gesendet wird. Da `select` mit der ersten
	// empfangenen Nachricht fortfährt, die bereit ist, wird der
	// Timeout-Fall eintreten, wenn die Operation länger als die
	// zugelassene 1 Sekunde dauert.
	select {
	case res := <-c1:
		fmt.Println(res)
	case <-time.After(1 * time.Second):
		fmt.Println("timeout 1")
	}

	// Wenn wir einen längeren Timeout von 3 Sekunden zulassen,
	// wird die Nachricht von `c2` empfangen und das Ergebnis
	// ausgegeben.
	c2 := make(chan string, 1)
	go func() {
		time.Sleep(2 * time.Second)
		c2 <- "result 2"
	}()
	select {
	case res := <-c2:
		fmt.Println(res)
	case <-time.After(3 * time.Second):
		fmt.Println("timeout 2")
	}
}

```
