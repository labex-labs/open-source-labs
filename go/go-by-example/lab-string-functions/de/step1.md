# String-Funktionen

Vervollständigen Sie den folgenden Code, um die Ausgabe verschiedener String-Funktionen des `strings`-Pakets auszugeben.

- Verwenden Sie das `strings`-Paket, um den Laborkurs abzuschließen.
- Verwenden Sie die `fmt.Println`-Funktion, um die Ausgabe auszugeben.
- Ändern Sie den Funktionsnamen oder die Parameter nicht.

```sh
$ go run string-functions.go
Enthält: true
Anzahl: 2
Hat Präfix: true
Hat Suffix: true
Index: 1
Verknüpfen: a-b
Wiederholen: aaaaa
Ersetzen: f00
Ersetzen: f0o
Teilen: [a b c d e]
In Kleinbuchstaben: test
In Großbuchstaben: TEST
```

Hier ist der vollständige Code:

```go
// Das Standardbibliothekspaket `strings` bietet viele
// nützliche string-bezogene Funktionen. Hier sind einige Beispiele,
// um Ihnen einen Eindruck vom Paket zu geben.

package main

import (
	"fmt"
	s "strings"
)

// Wir verweisen `fmt.Println` auf einen kürzeren Namen, da wir ihn
// häufig unten verwenden werden.
var p = fmt.Println

func main() {

	// Hier ist ein Beispiel für die verfügbaren Funktionen in
	// `strings`. Da dies Funktionen aus dem Paket sind, nicht Methoden
	// auf dem String-Objekt selbst, müssen wir den betrachteten String
	// als erstes Argument an die Funktion übergeben. Sie können weitere
	// Funktionen in der Dokumentation des [`strings`](https://pkg.go.dev/strings)
	// Pakets finden.
	p("Enthält:  ", s.Contains("test", "es"))
	p("Anzahl:     ", s.Count("test", "t"))
	p("Hat Präfix: ", s.HasPrefix("test", "te"))
	p("Hat Suffix: ", s.HasSuffix("test", "st"))
	p("Index:     ", s.Index("test", "e"))
	p("Verknüpfen: ", s.Join([]string{"a", "b"}, "-"))
	p("Wiederholen: ", s.Repeat("a", 5))
	p("Ersetzen:   ", s.Replace("foo", "o", "0", -1))
	p("Ersetzen:   ", s.Replace("foo", "o", "0", 1))
	p("Teilen:     ", s.Split("a-b-c-d-e", "-"))
	p("In Kleinbuchstaben: ", s.ToLower("TEST"))
	p("In Großbuchstaben: ", s.ToUpper("test"))
}

```
