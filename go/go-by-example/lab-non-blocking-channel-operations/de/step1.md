# Nicht blockierende Kanaloperationen

Das Problem, das in diesem Labor gelöst werden soll, ist die Implementierung nicht blockierender Kanaloperationen mit der `select`-Anweisung mit einer `default`-Klausel.

- Implementieren Sie einen nicht blockierenden Empfang über einen Kanal mit der `select`-Anweisung mit einer `default`-Klausel.
- Implementieren Sie einen nicht blockierenden Sendevorgang über einen Kanal mit der `select`-Anweisung mit einer `default`-Klausel.
- Implementieren Sie einen mehrwege nicht blockierenden `select` mit der `select`-Anweisung mit mehreren `case`-Klauseln und einer `default`-Klausel.

```sh
$ go run non-blocking-channel-operations.go
keine Nachricht empfangen
keine Nachricht gesendet
keine Aktivität
```

Hier ist der vollständige Code:

```go
// Grundlegende Sende- und Empfangsoperationen über Kanäle sind blockierend.
// Wir können jedoch `select` mit einer `default`-Klausel verwenden, um
// _nicht blockierende_ Sende-, Empfangs- und sogar
// nicht blockierende mehrwege `select`s zu implementieren.

package main

import "fmt"

func main() {
	messages := make(chan string)
	signals := make(chan bool)

	// Hier ist ein nicht blockierender Empfang. Wenn ein Wert
	// auf `messages` verfügbar ist, wird `select` den `<-messages`-
	// `case` mit diesem Wert auswählen. Wenn nicht, wird es
	// sofort den `default`-Fall auswählen.
	select {
	case msg := <-messages:
		fmt.Println("empfangene Nachricht", msg)
	default:
		fmt.Println("keine Nachricht empfangen")
	}

	// Ein nicht blockierender Sendevorgang funktioniert ähnlich. Hier kann `msg`
	// nicht an den `messages`-Kanal gesendet werden, da der Kanal keinen Puffer hat
	// und es keinen Empfänger gibt. Daher wird der `default`-Fall ausgewählt.
	msg := "hi"
	select {
	case messages <- msg:
		fmt.Println("gesendete Nachricht", msg)
	default:
		fmt.Println("keine Nachricht gesendet")
	}

	// Wir können mehrere `case`s oberhalb der `default`-
	// Klausel verwenden, um einen mehrwege nicht blockierenden
	// `select` zu implementieren. Hier versuchen wir nicht blockierende
	// Empfänge sowohl auf `messages` als auch auf `signals`.
	select {
	case msg := <-messages:
		fmt.Println("empfangene Nachricht", msg)
	case sig := <-signals:
		fmt.Println("empfangenes Signal", sig)
	default:
		fmt.Println("keine Aktivität")
	}
}

```
