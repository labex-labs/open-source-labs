# Context

Die `hello`-Funktion simuliert einige Arbeit, die der Server ausführt, indem er einige Sekunden wartet, bevor er eine Antwort an den Client sendet. Während der Arbeit überwacht man den `Done()`-Kanal des Kontexts auf ein Signal, dass wir die Arbeit abbrechen und so bald wie möglich zurückkehren sollten.

- Golang-Version 1.13 oder höher.

```sh
# Führen Sie den Server im Hintergrund aus.
$ go run context-in-http-servers.go &

# Simulieren Sie einen Clientanfrage an `/hello`, drücken
# Sie kurz nach dem Start `Strg+C`, um eine
# Stornierung zu signalisieren.
$ curl localhost:8090/hello
server: hello handler started
^C
server: context canceled
server: hello handler ended
```

Hier ist der vollständige Code:

```go
// Im vorherigen Beispiel haben wir uns die Einrichtung eines einfachen
// [HTTP-Servers](http-servers) angeschaut. HTTP-Server eignen sich gut,
// um die Verwendung von `context.Context` zur Steuerung der Stornierung
// zu demonstrieren. Ein `Context` trägt Fristen, Stornierungssignale
// und andere anforderungsbezogene Werte über API-Grenzen und Goroutinen
// hinweg.
package main

import (
	"fmt"
	"net/http"
	"time"
)

func hello(w http.ResponseWriter, req *http.Request) {

	// Ein `context.Context` wird für jede Anfrage von der
	// `net/http`-Maschinerie erstellt und ist über die
	// `Context()`-Methode verfügbar.
	ctx := req.Context()
	fmt.Println("server: hello handler started")
	defer fmt.Println("server: hello handler ended")

	// Warten Sie einige Sekunden, bevor Sie eine Antwort an den
	// Client senden. Dies könnte einige Arbeit simulieren, die der
	// Server ausführt. Während der Arbeit überwachen Sie den
	// `Done()`-Kanal des Kontexts auf ein Signal, dass wir die
	// Arbeit abbrechen und so bald wie möglich zurückkehren sollten.
	select {
	case <-time.After(10 * time.Second):
		fmt.Fprintf(w, "hello\n")
	case <-ctx.Done():
		// Die `Err()`-Methode des Kontexts gibt einen Fehler zurück,
		// der erklärt, warum der `Done()`-Kanal geschlossen wurde.
		err := ctx.Err()
		fmt.Println("server:", err)
		internalError := http.StatusInternalServerError
		http.Error(w, err.Error(), internalError)
	}
}

func main() {

	// Wie zuvor registrieren wir unseren Handler für die Route "/hello"
	// und starten den Dienst.
	http.HandleFunc("/hello", hello)
	http.ListenAndServe(":8090", nil)
}

```
