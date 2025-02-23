# Zeiger

Das Problem besteht darin, zu verstehen, wie Zeiger im Gegensatz zu Werten mit zwei Funktionen (`zeroval` und `zeroptr`) funktionieren. `zeroval` hat einen `int`-Parameter, sodass Argumente per Wert an sie übergeben werden. `zeroval` erhält eine Kopie von `ival`, die von der im aufrufenden Funktionsunterschiedlich ist. Im Gegensatz dazu hat `zeroptr` einen `*int`-Parameter, was bedeutet, dass es einen `int`-Zeiger annimmt. Der Code `*iptr` im Funktionskörper dereferenziert dann den Zeiger von seiner Speicheradresse auf den aktuellen Wert an dieser Adresse. Das Zuweisen eines Werts an einen dereferenzierten Zeiger ändert den Wert an der referenzierten Adresse.

- Sie sollten ein grundlegendes Verständnis von Golang haben.
- Sie sollten wissen, wie man in Golang Funktionen definiert und verwendet.
- Sie sollten wissen, wie man in Golang Zeiger verwendet.

```sh
# `zeroval` ändert das `i` in `main` nicht, aber
# `zeroptr` tut es, weil es eine Referenz auf die
# Speicheradresse für diese Variable hat.
$ go run pointers.go
initial: 1
zeroval: 1
zeroptr: 0
pointer: 0x42131100
```

Hier ist der vollständige Code:

```go
// Go unterstützt <em><a href="https://en.wikipedia.org/wiki/Pointer_(computer_programming)">Zeiger</a></em>,
// was es Ihnen ermöglicht, Referenzen auf Werte und Datensätze
// in Ihrem Programm zu übergeben.

package main

import "fmt"

// Wir werden zeigen, wie Zeiger im Gegensatz zu Werten mit
// 2 Funktionen funktionieren: `zeroval` und `zeroptr`. `zeroval` hat einen
// `int`-Parameter, sodass Argumente per Wert an sie übergeben werden.
// `zeroval` erhält eine Kopie von `ival`, die von der im aufrufenden
// Funktionsunterschiedlich ist.
func zeroval(ival int) {
	ival = 0
}

// Im Gegensatz dazu hat `zeroptr` einen `*int`-Parameter, was bedeutet,
// dass es einen `int`-Zeiger annimmt. Der Code `*iptr` im
// Funktionskörper dereferenziert dann den Zeiger von seiner
// Speicheradresse auf den aktuellen Wert an dieser Adresse.
// Das Zuweisen eines Werts an einen dereferenzierten Zeiger ändert den
// Wert an der referenzierten Adresse.
func zeroptr(iptr *int) {
	*iptr = 0
}

func main() {
	i := 1
	fmt.Println("initial:", i)

	zeroval(i)
	fmt.Println("zeroval:", i)

	// Die Syntax `&i` liefert die Speicheradresse von `i`,
	// d.h. einen Zeiger auf `i`.
	zeroptr(&i)
	fmt.Println("zeroptr:", i)

	// Zeiger können ebenfalls ausgegeben werden.
	fmt.Println("pointer:", &i)
}

```
