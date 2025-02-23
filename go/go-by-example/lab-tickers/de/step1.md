# Timer und Taster

In diesem Labor müssen Sie einen Taster erstellen, der alle 500 Millisekunden tickt, bis wir ihn stoppen. Sie werden einen Kanal verwenden, um auf die Werte zu warten, sobald sie eintreffen.

- Verwenden Sie das `time`-Paket, um einen Taster zu erstellen.
- Verwenden Sie einen Kanal, um auf die Werte zu warten, sobald sie eintreffen.
- Verwenden Sie die `select`-Anweisung, um Werte aus dem Kanal zu empfangen.
- Stoppen Sie den Taster nach 1600 Millisekunden.

```sh
# Wenn wir dieses Programm ausführen, sollte der Taster 3 mal ticken,
# bevor wir ihn stoppen.
$ go run tickers.go
Tick at 2012-09-23 11:29:56.487625 -0700 PDT
Tick at 2012-09-23 11:29:56.988063 -0700 PDT
Tick at 2012-09-23 11:29:57.488076 -0700 PDT
Ticker stopped
```

Hier ist der vollständige Code:

```go
// [Timer](timers) sind für den Fall, dass Sie etwas einmal in der Zukunft tun möchten - _Taster_ sind für den Fall, dass Sie etwas wiederholt in regelmäßigen Abständen tun möchten. Hier ist ein Beispiel für einen Taster, der periodisch tickt, bis wir ihn stoppen.

package main

import (
	"fmt"
	"time"
)

func main() {

	// Taster verwenden einen ähnlichen Mechanismus wie Timer: einen Kanal, an den Werte gesendet werden. Hier werden wir die eingebautte `select`-Anweisung auf dem Kanal verwenden, um auf die Werte zu warten, sobald sie alle 500 Millisekunden eintreffen.
	ticker := time.NewTicker(500 * time.Millisecond)
	done := make(chan bool)

	go func() {
		for {
			select {
			case <-done:
				return
			case t := <-ticker.C:
				fmt.Println("Tick at", t)
			}
		}
	}()

	// Taster können wie Timer gestoppt werden. Sobald ein Taster gestoppt ist, wird er keine weiteren Werte auf seinem Kanal empfangen. Wir werden unseren nach 1600 Millisekunden stoppen.
	time.Sleep(1600 * time.Millisecond)
	ticker.Stop()
	done <- true
	fmt.Println("Ticker stopped")
}

```
