# `for`

Der folgende Code enthält verschiedene Arten von `for`-Schleifen. Einige Teile des Codes sind jedoch unvollständig, und Sie müssen die Lücken ausfüllen, um den Code richtig zu machen.

- Grundkenntnisse der Golang-Syntax
- Vertrautheit mit `for`-Schleifen in Golang

```sh
$ go run for.go
1
2
3
7
8
9
loop
1
3
5

# Wir werden später einige andere `for`-Formen sehen, wenn wir uns
# `range`-Anweisungen, Kanäle und andere Daten
# Strukturen ansehen.
```

Hier ist der vollständige Code:

```go
// `for` ist die einzige Schleifenkonstruktion in Go. Hier sind
// einige grundlegende Arten von `for`-Schleifen.

package main

import "fmt"

func main() {

	// Die einfachste Art, mit einer einzigen Bedingung.
	i := 1
	for i <= 3 {
		fmt.Println(i)
		i = i + 1
	}

	// Eine klassische Initialisierungs-/Bedingungs-/Nach-Schleife.
	for j := 7; j <= 9; j++ {
		fmt.Println(j)
	}

	// `for` ohne Bedingung wird wiederholt schleifen,
	// bis Sie aus der Schleife `brechen` oder aus der
	// umschließenden Funktion `zurückkehren`.
	for {
		fmt.Println("loop")
		break
	}

	// Sie können auch `continue` zu der nächsten Iteration der
	// Schleife springen.
	for n := 0; n <= 5; n++ {
		if n%2 == 0 {
			continue
		}
		fmt.Println(n)
	}
}

```
