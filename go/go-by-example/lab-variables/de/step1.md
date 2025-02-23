# Variablen

Sie müssen den Code vervollständigen, um Variablen unterschiedlicher Typen in Golang zu deklarieren und zu initialisieren.

- Grundkenntnisse der Golang-Syntax
- Vertrautheit mit der Variablendeklaration und -initialisierung in Golang

```sh
$ go run variables.go
initial
1 2
true
0
apple
```

Hier ist der vollständige Code:

```go
// In Go werden _Variablen_ explizit deklariert und vom
// Compiler verwendet, um z.B. die Typkorrektheit von
// Funktionsaufrufen zu überprüfen.

package main

import "fmt"

func main() {

	// `var` deklariert eine oder mehrere Variablen.
	var a = "initial"
	fmt.Println(a)

	// Sie können mehrere Variablen gleichzeitig deklarieren.
	var b, c int = 1, 2
	fmt.Println(b, c)

	// Go wird den Typ der initialisierten Variablen ableiten.
	var d = true
	fmt.Println(d)

	// Ohne entsprechende Initialisierung deklarierte
	// Variablen werden mit dem _Nullwert_ initialisiert.
	// Beispielsweise ist der Nullwert für einen `int` `0`.
	var e int
	fmt.Println(e)

	// Die `:=`-Syntax ist eine Abkürzung für die Deklaration
	// und Initialisierung einer Variablen, z.B. für
	// `var f string = "apple"` in diesem Fall.
	// Diese Syntax ist nur innerhalb von Funktionen verfügbar.
	f := "apple"
	fmt.Println(f)
}

```
