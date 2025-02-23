# Channel Puffering

Standardmäßig sind Kanäle in Golang unpuffernd, was bedeutet, dass sie nur Sendevorgänge (`chan <-`) akzeptieren, wenn es einen entsprechenden Empfang (`<- chan`) gibt, der bereit ist, den gesendeten Wert zu empfangen. Puffernde Kanäle akzeptieren jedoch eine begrenzte Anzahl von Werten ohne einen entsprechenden Empfänger für diese Werte. In diesem Labor müssen Sie einen puffernden Kanal erstellen und Werte in den Kanal senden, ohne dass ein entsprechender paralleler Empfang erfolgt.

- Grundkenntnisse von Golang-Kanälen
- Verständnis von puffernden Kanälen

```sh
$ go run channel-buffering.go
puffernd
Kanal
```

Hier ist der vollständige Code:

```go
// Standardmäßig sind Kanäle _unpuffernd_, was bedeutet, dass sie
// nur Sendevorgänge (`chan <-`) akzeptieren, wenn es einen
// entsprechenden Empfang (`<- chan`) gibt, der bereit ist, den
// gesendeten Wert zu empfangen. _Puffernde Kanäle_ akzeptieren
// eine begrenzte Anzahl von Werten ohne einen entsprechenden
// Empfänger für diese Werte.

package main

import "fmt"

func main() {

	// Hier `make` wir einen Kanal vom Typ string, der bis zu
	// 2 Werte puffernd speichert.
	messages := make(chan string, 2)

	// Da dieser Kanal puffernd ist, können wir diese
	// Werte in den Kanal senden, ohne dass ein entsprechender
	// paralleler Empfang erfolgt.
	messages <- "puffernd"
	messages <- "Kanal"

	// Später können wir diese beiden Werte wie üblich empfangen.
	fmt.Println(<-messages)
	fmt.Println(<-messages)
}

```
