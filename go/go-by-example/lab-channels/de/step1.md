# Kanäle

In diesem Labor müssen Sie einen neuen Kanal erstellen und einen Wert von einer neuen Goroutine in diesen senden. Anschließend empfangen Sie den Wert aus dem Kanal und geben ihn aus.

- Sie müssen die Syntax `make(chan val-type)` verwenden, um einen neuen Kanal zu erstellen.
- Der Kanal muss vom Typ der Werte, die er transportiert, typisiert werden.
- Sie müssen die Syntax `channel <-` verwenden, um einen Wert in den Kanal zu senden.
- Sie müssen die Syntax `<-channel` verwenden, um einen Wert aus dem Kanal zu empfangen.
- Sie müssen eine neue Goroutine verwenden, um den Wert in den Kanal zu senden.

```sh
# Wenn wir das Programm ausführen, wird die Nachricht
# `"ping"` erfolgreich von einer Goroutine über unseren
# Kanal an eine andere weitergeleitet.
$ go run channels.go
ping

# Standardmäßig blockieren Senden und Empfangen, bis sowohl
# der Sender als auch der Empfänger bereit sind. Diese Eigenschaft
# hat es uns ermöglicht, am Ende unseres Programms auf die
# `"ping"`-Nachricht zu warten, ohne weitere Synchronisation
# verwenden zu müssen.
```

Hier ist der vollständige Code:

```go
// _Kanäle_ sind die Rohre, die parallele Goroutinen verbinden.
// Sie können Werte in Kanäle von einer Goroutine senden und
// diese Werte in eine andere Goroutine empfangen.

package main

import "fmt"

func main() {

	// Erstellen Sie einen neuen Kanal mit `make(chan val-type)`.
	// Kanäle sind vom Typ der Werte, die sie transportieren, typisiert.
	messages := make(chan string)

	// _Senden_ Sie einen Wert in einen Kanal, indem Sie die
	// Syntax `channel <-` verwenden. Hier senden wir `"ping"`
	// an den oben erstellten `messages`-Kanal von einer neuen
	// Goroutine aus.
	go func() { messages <- "ping" }()

	// Die Syntax `<-channel` _empfängt_ einen Wert aus dem
	// Kanal. Hier empfangen wir die oben gesendete `"ping"`-Nachricht
	// und geben sie aus.
	msg := <-messages
	fmt.Println(msg)
}

```
