# Closures

Du musst eine Funktion erstellen, die eine andere Funktion zurückgibt. Die zurückgegebene Funktion sollte jede Mal, wenn sie aufgerufen wird, eine Variable um eins erhöhen. Die Variable sollte für jede zurückgegebene Funktion einzigartig sein.

- Die Funktion `intSeq` sollte eine andere Funktion zurückgeben.
- Die zurückgegebene Funktion sollte jede Mal, wenn sie aufgerufen wird, eine Variable um eins erhöhen.
- Die Variable sollte für jede zurückgegebene Funktion einzigartig sein.

```sh
$ go run closures.go
1
2
3
1

# Das letzte Feature von Funktionen, das wir uns momentan ansehen, ist
# Rekursion.
```

Hier ist der vollständige Code:

```go
// Go unterstützt [_anonyme Funktionen_](https://en.wikipedia.org/wiki/Anonymous_function),
// die <a href="https://en.wikipedia.org/wiki/Closure_(computer_science)"><em>Closures</em></a> bilden können.
// Anonyme Funktionen sind nützlich, wenn du eine Funktion inline definieren möchtest, ohne sie benennen zu müssen.

package main

import "fmt"

// Diese Funktion `intSeq` gibt eine andere Funktion zurück, die
// wir anonym im Körper von `intSeq` definieren. Die
// zurückgegebene Funktion _schließt sich um_ die Variable `i`, um
// einen Closure zu bilden.
func intSeq() func() int {
	i := 0
	return func() int {
		i++
		return i
	}
}

func main() {

	// Wir rufen `intSeq` auf und weisen das Ergebnis (eine Funktion)
	// der Variable `nextInt` zu. Dieser Funktionswert fängt seinen
	// eigenen `i`-Wert ein, der jedes Mal aktualisiert wird, wenn
	// wir `nextInt` aufrufen.
	nextInt := intSeq()

	// Betrachte die Wirkung des Closures, indem du `nextInt`
	// ein paar Mal aufrufst.
	fmt.Println(nextInt())
	fmt.Println(nextInt())
	fmt.Println(nextInt())

	// Um zu bestätigen, dass der Zustand für diese
	// bestimmte Funktion einzigartig ist, erstelle und teste eine neue.
	newInts := intSeq()
	fmt.Println(newInts())
}

```
