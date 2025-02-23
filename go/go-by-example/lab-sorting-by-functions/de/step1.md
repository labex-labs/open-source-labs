# Sortieren mit Funktionen

Das Problem, das in diesem Labor gelöst werden soll, besteht darin, eine benutzerdefinierte Sortierfunktion in Go zu implementieren, die eine Zeichenfolgen-Slice nach ihrer Länge sortiert.

- Der `byLength`-Typ sollte als Alias für den `[]string`-Typ erstellt werden.
- Die `sort.Interface`-Schnittstelle sollte auf dem `byLength`-Typ implementiert werden.
- Die `Len`- und `Swap`-Funktionen sollten auf dem `byLength`-Typ implementiert werden.
- Die `Less`-Funktion sollte auf dem `byLength`-Typ implementiert werden, um die tatsächliche benutzerdefinierte Sortierlogik zu enthalten.
- Die `main`-Funktion sollte das ursprüngliche `fruits`-Slice in `byLength` umwandeln und dann `sort.Sort` auf diesem typisierten Slice verwenden.

```sh
# Wenn wir unser Programm ausführen, wird eine Liste
# nach der Zeichenfolgenlänge sortiert, wie gewünscht.
$ go run sorting-by-functions.go
[kiwi peach banana]

# Indem wir dieses Muster von der Erstellung eines
# benutzerdefinierten Typs befolgen, die drei
# `Interface`-Methoden auf diesem Typ implementieren
# und dann `sort.Sort` auf einer Sammlung dieses
# benutzerdefinierten Typs aufrufen, können wir Go-Slices
# nach beliebigen Funktionen sortieren.
```

Hier ist der vollständige Code:

```go
// Manchmal möchten wir eine Sammlung nach einem anderen
// Kriterium als ihrer natürlichen Reihenfolge sortieren.
// Beispielsweise möchten wir Strings nach ihrer Länge
// statt alphabetisch sortieren. Hier ist ein Beispiel für
// benutzerdefinierte Sortierungen in Go.

package main

import (
	"fmt"
	"sort"
)

// Um in Go nach einer benutzerdefinierten Funktion zu
// sortieren, benötigen wir einen entsprechenden Typ.
// Hier haben wir einen `byLength`-Typ erstellt, der
// einfach ein Alias für den eingebauten `[]string`-Typ
// ist.
type byLength []string

// Wir implementieren die `sort.Interface`-Schnittstelle -
// `Len`, `Less` und `Swap` - auf unserem Typ, damit wir
// die generische `Sort`-Funktion des `sort`-Pakets
// verwenden können. `Len` und `Swap` werden normalerweise
// für verschiedene Typen ähnlich sein, und `Less` wird
// die tatsächliche benutzerdefinierte Sortierlogik
// enthalten. Im unserem Fall möchten wir in aufsteigender
// Zeichenfolgenlänge sortieren, daher verwenden wir hier
// `len(s[i])` und `len(s[j])`.
func (s byLength) Len() int {
	return len(s)
}
func (s byLength) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}
func (s byLength) Less(i, j int) bool {
	return len(s[i]) < len(s[j])
}

// Mit all dem in place können wir jetzt unsere
// benutzerdefinierte Sortierung implementieren, indem wir
// das ursprüngliche `fruits`-Slice in `byLength`
// umwandeln und dann `sort.Sort` auf diesem typisierten
// Slice verwenden.
func main() {
	fruits := []string{"peach", "banana", "kiwi"}
	sort.Sort(byLength(fruits))
	fmt.Println(fruits)
}

```
