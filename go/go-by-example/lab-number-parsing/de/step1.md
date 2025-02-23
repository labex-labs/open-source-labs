# Zahlensyntaxanalyse

Das Extrahieren von Zahlen aus Zeichenketten ist eine häufige Aufgabe in vielen Programmen. In diesem Lab müssen Sie das integrierte Paket `strconv` verwenden, um verschiedene Arten von Zahlen aus Zeichenketten zu analysieren.

- Verwenden Sie das Paket `strconv`, um Zahlen aus Zeichenketten zu analysieren.
- Analysieren Sie eine Gleitkommazahl mit `ParseFloat`.
- Analysieren Sie eine Ganzzahl mit `ParseInt`.
- Analysieren Sie eine hexadezimal formatierte Zahl mit `ParseInt`.
- Analysieren Sie eine vorzeichenlose Ganzzahl mit `ParseUint`.
- Analysieren Sie eine Dezimalzahl mit `Atoi`.
- Behandeln Sie die von den Analysefunktionen zurückgegebenen Fehler.

```sh
$ go run number-parsing.go
1,234
123
456
789
135
strconv.ParseInt: Parsen von "wat": ungültige Syntax

# Als nächstes betrachten wir eine weitere häufige Analysetask: URLs.
```

Hier ist der vollständige Code:

```go
// Das Extrahieren von Zahlen aus Zeichenketten ist eine einfache, aber häufige Aufgabe
// in vielen Programmen; hier ist, wie man es in Go macht.

package main

// Das integrierte Paket `strconv` bietet die Zahlensyntaxanalyse.
import (
	"fmt"
	"strconv"
)

func main() {

	// Mit `ParseFloat` gibt diese `64` an, wie viele Bits der
	// Genauigkeit analysiert werden sollen.
	f, _ := strconv.ParseFloat("1,234", 64)
	fmt.Println(f)

	// Für `ParseInt` bedeutet die `0`, dass die Basis aus der
	// Zeichenkette abgeleitet werden soll. `64` erfordert, dass das Ergebnis in 64
	// Bits passt.
	i, _ := strconv.ParseInt("123", 0, 64)
	fmt.Println(i)

	// `ParseInt` erkennt hexadezimal formatierte Zahlen.
	d, _ := strconv.ParseInt("0x1c8", 0, 64)
	fmt.Println(d)

	// Ein `ParseUint` ist ebenfalls verfügbar.
	u, _ := strconv.ParseUint("789", 0, 64)
	fmt.Println(u)

	// `Atoi` ist eine Hilfsfunktion für die einfache Dezimalzahl (`int`)-Syntaxanalyse.
	k, _ := strconv.Atoi("135")
	fmt.Println(k)

	// Analysefunktionen geben einen Fehler bei ungültiger Eingabe zurück.
	_, e := strconv.Atoi("wat")
	fmt.Println(e)
}

```
