# Iteration über Kanäle

Sie müssen eine Funktion schreiben, die einen Kanal von ganzen Zahlen entgegennimmt und die Summe aller empfangenen ganzen Zahlen zurückgibt.

- Die Funktion sollte `sumInts` heißen.
- Die Funktion sollte einen einzelnen Parameter vom Typ `chan int` entgegennehmen.
- Die Funktion sollte einen einzelnen ganzzahligen Wert zurückgeben.
- Innerhalb des Funktionskörpers sind Sie nicht gestattet, Schleifen oder Rekursionen zu verwenden.
- Sie sind nicht gestattet, externe Pakete zu verwenden.

```sh
$ go run range-over-channels.go
one
two

# Dieses Beispiel zeigte auch, dass es möglich ist,
# einen nicht leeren Kanal zu schließen, aber die
# verbleibenden Werte weiterhin zu empfangen.
```

Hier ist der vollständige Code:

```go
// In einem [vorherigen](range) Beispiel haben wir gesehen, wie `for` und
// `range` die Iteration über grundlegende Datenstrukturen ermöglichen.
// Wir können auch diese Syntax verwenden, um über
// von einem Kanal empfangene Werte zu iterieren.

package main

import "fmt"

func main() {

	// Wir werden über 2 Werte im `queue`-Kanal iterieren.
	queue := make(chan string, 2)
	queue <- "one"
	queue <- "two"
	close(queue)

	// Diese `range`-Iteration geht über jedes Element, das
	// aus `queue` empfangen wird. Da wir oben den
	// Kanal geschlossen haben, endet die Iteration nach
	// dem Empfang der 2 Elemente.
	for elem := range queue {
		fmt.Println(elem)
	}
}

```
