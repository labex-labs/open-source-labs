# Mehrere Rückgabewerte

Vervollständigen Sie die `swap`-Funktion, um zwei Eingabeparameter in umgekehrter Reihenfolge zurückzugeben.

- Die `swap`-Funktion sollte zwei ganze Zahlen als Eingabeparameter akzeptieren.
- Die `swap`-Funktion sollte zwei ganze Zahlen in umgekehrter Reihenfolge zurückgeben.

```sh
$ go run multiple-return-values.go
3
7
7

# Die Akzeptanz einer variablen Anzahl von Argumenten ist eine weitere schöne
# Eigenschaft von Go-Funktionen; wir werden uns das nächste ansehen.
```

Hier ist der vollständige Code:

```go
// Go hat eine integrierte Unterstützung für _mehrere Rückgabewerte_.
// Diese Funktion wird häufig in idiomatischem Go verwendet, beispielsweise
// um sowohl das Ergebnis als auch die Fehlerwerte aus einer Funktion zurückzugeben.

package main

import "fmt"

// Die `(int, int)` in dieser Funktionssignatur zeigt an, dass
// die Funktion 2 `int`s zurückgibt.
func vals() (int, int) {
	return 3, 7
}

func main() {

	// Hier verwenden wir die 2 verschiedenen Rückgabewerte aus dem
	// Aufruf mit _mehrfacher Zuweisung_.
	a, b := vals()
	fmt.Println(a)
	fmt.Println(b)

	// Wenn Sie nur einen Teil der zurückgegebenen Werte möchten,
	// verwenden Sie den Platzhalter `_`.
	_, c := vals()
	fmt.Println(c)
}

```
