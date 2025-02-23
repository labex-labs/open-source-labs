# Rekursion

Die `sum`-Funktion nimmt ein Slice von ganzen Zahlen entgegen und gibt die Summe aller ganzen Zahlen im Slice zurück. Die Funktion ist jedoch unvollständig und muss mithilfe von Rekursion implementiert werden.

- Die `sum`-Funktion muss mithilfe von Rekursion implementiert werden.
- Die Funktion muss ein Slice von ganzen Zahlen als Eingabe entgegennehmen.
- Die Funktion muss die Summe aller ganzen Zahlen im Slice zurückgeben.

```sh
$ go run recursion.go
5040
13
```

Hier ist der vollständige Code:

```go
// Go unterstützt
// <a href="https://en.wikipedia.org/wiki/Recursion_(computer_science)"><em>rekursive Funktionen</em></a>.
// Hier ist ein klassisches Beispiel.

package main

import "fmt"

// Diese `fact`-Funktion ruft sich selbst auf, bis sie den
// Basisfall von `fact(0)` erreicht.
func fact(n int) int {
	if n == 0 {
		return 1
	}
	return n * fact(n-1)
}

func main() {
	fmt.Println(fact(7))

	// Schließungen können ebenfalls rekursiv sein, erfordern jedoch,
	// dass die Schließung explizit mit einem typisierten `var`
	// deklariert wird, bevor sie definiert wird.
	var fib func(n int) int

	fib = func(n int) int {
		if n < 2 {
			return n
		}

		// Da `fib` zuvor in `main` deklariert wurde, weiß Go,
		// welche Funktion hier mit `fib` aufgerufen werden soll.
		return fib(n-1) + fib(n-2)
	}

	fmt.Println(fib(7))
}

```
