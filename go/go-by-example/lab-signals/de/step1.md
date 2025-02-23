# Signale

In einigen Fällen möchten wir, dass unsere Go-Programme Unix-Signale intelligent behandeln. Beispielsweise möchten wir, dass ein Server sich bei Empfang eines `SIGTERM` gnädig beendet, oder dass ein Befehlszeilentool die Eingabeverarbeitung stoppt, wenn es ein `SIGINT` erhält.

- Erstellen Sie einen gepufferten Kanal, um `os.Signal`-Benachrichtigungen zu empfangen.
- Registrieren Sie den Kanal, um Benachrichtigungen über bestimmte Signale mithilfe von `signal.Notify` zu erhalten.
- Erstellen Sie eine Goroutine, um einen blockierenden Empfang von Signalen auszuführen.
- Geben Sie das empfangene Signal aus und benachrichtigen Sie das Programm, dass es beendet werden kann.
- Warten Sie auf das erwartete Signal und beenden Sie dann das Programm.

```sh
# Wenn wir dieses Programm ausführen, wird es blockieren und auf ein
# Signal warten. Indem wir `ctrl-C` eingeben (was der
# Terminal als `^C` anzeigt), können wir ein `SIGINT`-Signal senden,
# was das Programm veranlasst, `interrupt` auszugeben und dann zu beenden.
$ go run signals.go
awaiting signal
^C
interrupt
exiting
```

Hier ist der vollständige Code:

```go
// Manchmal möchten wir, dass unsere Go-Programme intelligent
// [Unix-Signale](https://en.wikipedia.org/wiki/Unix_signal) behandeln.
// Beispielsweise möchten wir, dass ein Server sich bei Empfang eines `SIGTERM` gnädig beendet,
// oder dass ein Befehlszeilentool die Eingabeverarbeitung stoppt, wenn es ein `SIGINT` erhält.
// Hier ist, wie man Signale in Go mit Kanälen behandelt.

package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
)

func main() {

	// Die Go-Signalbenachrichtigung funktioniert, indem `os.Signal`-
	// Werte über einen Kanal gesendet werden. Wir werden einen Kanal
	// erstellen, um diese Benachrichtigungen zu empfangen. Beachten Sie,
	// dass dieser Kanal gepuffert sein sollte.
	sigs := make(chan os.Signal, 1)

	// `signal.Notify` registriert den angegebenen Kanal, um
	// Benachrichtigungen über die angegebenen Signale zu erhalten.
	signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM)

	// Wir könnten hier im Hauptprogramm von `sigs` empfangen,
	// aber sehen wir uns an, wie dies auch in einer separaten Goroutine
	// geschehen könnte, um ein realistischeres Szenario der gnädigen Beendigung zu demonstrieren.
	done := make(chan bool, 1)

	go func() {
		// Diese Goroutine führt einen blockierenden Empfang von
		// Signalen aus. Wenn sie eines erhält, wird es ausgegeben
		// und dann das Programm benachrichtigt, dass es beendet werden kann.
		sig := <-sigs
		fmt.Println()
		fmt.Println(sig)
		done <- true
	}()

	// Das Programm wird hier warten, bis es das erwartete Signal erhält
	// (wie durch die obige Goroutine angedeutet, indem ein Wert auf `done` gesendet wird)
	// und wird dann beendet.
	fmt.Println("awaiting signal")
	<-done
	fmt.Println("exiting")
}

```
