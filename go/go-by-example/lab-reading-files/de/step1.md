# Dateien lesen

In Ihrem Go-Programm müssen Sie Dateien lesen und verschiedene Operationen auf den Daten in der Datei ausführen.

- Sie sollten mit den grundlegenden Go-Programmierkonzepten vertraut sein.
- Sie sollten Go auf Ihrem Computer installiert haben.

```sh
$ echo "hello" > /tmp/dat
$ echo "go" >> /tmp/dat
$ go run reading-files.go
hello
go
5 bytes: hello
2 bytes @ 6: go
2 bytes @ 6: go
5 bytes: hello

# Als nächstes werden wir uns ansehen, wie man Dateien schreibt.
```

Hier ist der vollständige Code:

```go
// Dateien lesen und schreiben sind grundlegende Aufgaben, die für
// viele Go-Programme erforderlich sind. Zunächst werden wir uns einige
// Beispiele für das Lesen von Dateien ansehen.

package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

// Beim Lesen von Dateien muss bei den meisten Aufrufen auf Fehler geprüft werden.
// Diese Hilfsmethode vereinfacht unsere Fehlerprüfungen unten.
func check(e error) {
	if e!= nil {
		panic(e)
	}
}

func main() {

	// Vielleicht ist die einfachste Dateilesetask das
	// Einlesen des gesamten Inhalts einer Datei in den Arbeitsspeicher.
	dat, err := os.ReadFile("/tmp/dat")
	check(err)
	fmt.Print(string(dat))

	// Sie möchten oft mehr Kontrolle darüber haben, wie und welche
	// Teile einer Datei gelesen werden. Für diese Aufgaben starten Sie
	// mit dem Öffnen einer Datei, um einen `os.File`-Wert zu erhalten.
	f, err := os.Open("/tmp/dat")
	check(err)

	// Lesen Sie einige Bytes am Anfang der Datei.
	// Erlauben Sie es, bis zu 5 zu lesen, aber beachten Sie auch, wie viele
	// tatsächlich gelesen wurden.
	b1 := make([]byte, 5)
	n1, err := f.Read(b1)
	check(err)
	fmt.Printf("%d bytes: %s\n", n1, string(b1[:n1]))

	// Sie können auch an einen bekannten Ort in der Datei springen
	// und von dort lesen.
	o2, err := f.Seek(6, 0)
	check(err)
	b2 := make([]byte, 2)
	n2, err := f.Read(b2)
	check(err)
	fmt.Printf("%d bytes @ %d: ", n2, o2)
	fmt.Printf("%v\n", string(b2[:n2]))

	// Das `io`-Paket bietet einige Funktionen, die möglicherweise
	// hilfreich für das Lesen von Dateien sind. Beispielsweise können
	// Lesevorgänge wie die obigen robuster mit `ReadAtLeast` implementiert werden.
	o3, err := f.Seek(6, 0)
	check(err)
	b3 := make([]byte, 2)
	n3, err := io.ReadAtLeast(f, b3, 2)
	check(err)
	fmt.Printf("%d bytes @ %d: %s\n", n3, o3, string(b3))

	// Es gibt keine integrierte Rückspulenfunktion, aber `Seek(0, 0)`
	// erreicht dies.
	_, err = f.Seek(0, 0)
	check(err)

	// Das `bufio`-Paket implementiert einen Pufferreader, der möglicherweise
	// sowohl aufgrund seiner Effizienz bei vielen kleinen Lesevorgängen als auch
	// aufgrund der zusätzlichen Lesemethoden, die es bietet, nützlich ist.
	r4 := bufio.NewReader(f)
	b4, err := r4.Peek(5)
	check(err)
	fmt.Printf("5 bytes: %s\n", string(b4))

	// Schließen Sie die Datei, wenn Sie fertig sind (normalerweise würde
	// dies unmittelbar nach dem Öffnen mit `defer` geplant werden).
	f.Close()
}

```
