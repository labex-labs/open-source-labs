# if-else

Sie müssen die Funktion `checkNumber` vervollständigen, die eine Ganzzahl als Eingabe nimmt und einen String zurückgibt. Wenn die Zahl gerade ist, soll "even" zurückgegeben werden, andernfalls "odd".

- Die Funktion sollte `checkNumber` heißen.
- Die Funktion sollte eine Ganzzahl als Eingabe nehmen.
- Die Funktion sollte einen String zurückgeben.
- Wenn die Zahl gerade ist, soll "even" zurückgegeben werden.
- Wenn die Zahl ungerade ist, soll "odd" zurückgegeben werden.

```sh
$ go run if-else.go
7 ist ungerade
8 ist durch 4 teilbar
9 hat 1 Ziffer

# Es gibt kein [ternäres if](https://en.wikipedia.org/wiki/%3F:)
# in Go, daher müssen Sie auch für einfache Bedingungen eine vollständige `if`-Anweisung verwenden.
```

Hier ist der vollständige Code:

```go
// Die Verzweigung mit `if` und `else` in Go ist
// einfach.

package main

import "fmt"

func main() {

	// Hier ist ein einfaches Beispiel.
	if 7%2 == 0 {
		fmt.Println("7 ist gerade")
	} else {
		fmt.Println("7 ist ungerade")
	}

	// Es kann eine `if`-Anweisung ohne `else` geben.
	if 8%4 == 0 {
		fmt.Println("8 ist durch 4 teilbar")
	}

	// Ein Statement kann den bedingten Anweisungen vorangehen; alle Variablen,
	// die in diesem Statement deklariert werden, sind in der aktuellen
	// und allen nachfolgenden Zweigen verfügbar.
	if num := 9; num < 0 {
		fmt.Println(num, "ist negativ")
	} else if num < 10 {
		fmt.Println(num, "hat 1 Ziffer")
	} else {
		fmt.Println(num, "hat mehrere Ziffern")
	}
}

// Beachten Sie, dass Sie in Go keine Klammern um die Bedingungen brauchen,
// dass jedoch die geschweiften Klammern erforderlich sind.

```
