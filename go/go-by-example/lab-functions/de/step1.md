# Funktionen

Im gegebenen Code haben wir zwei Funktionen `plus` und `plusPlus`. Die `plus`-Funktion nimmt zwei ganze Zahlen als Argumente entgegen und gibt ihre Summe zurück. Die `plusPlus`-Funktion nimmt drei ganze Zahlen als Argumente entgegen und gibt ihre Summe zurück. Ihre Aufgabe ist es, die `plusPlus`-Funktion zu vervollständigen, indem Sie die dritte ganze Zahl zur Summe der ersten beiden ganzen Zahlen hinzufügen.

- Die `plus`-Funktion sollte zwei ganze Zahlen als Argumente entgegennehmen und ihre Summe als ganze Zahl zurückgeben.
- Die `plusPlus`-Funktion sollte drei ganze Zahlen als Argumente entgegennehmen und ihre Summe als ganze Zahl zurückgeben.
- Die `plusPlus`-Funktion sollte die `plus`-Funktion verwenden, um die Summe der ersten beiden ganzen Zahlen zu berechnen.

```sh
$ go run functions.go
1+2 = 3
1+2+3 = 6

# Es gibt mehrere weitere Eigenschaften von Go-Funktionen. Eine davon ist
# die Möglichkeit von mehreren Rückgabewerten, über die wir uns im nächsten
# Abschnitt beschäftigen werden.
```

Hier ist der vollständige Code:

```go
// _Funktionen_ sind zentral in Go. Wir werden uns mit
// Funktionen anhand einiger unterschiedlicher Beispiele
// beschäftigen.

package main

import "fmt"

// Hier ist eine Funktion, die zwei `int`s entgegennimmt und
// ihre Summe als `int` zurückgibt.
func plus(a int, b int) int {

	// Go erfordert explizite Rückgaben, d.h. es gibt
	// nicht automatisch den Wert des letzten Ausdrucks
	// zurück.
	return a + b
}

// Wenn Sie mehrere aufeinanderfolgende Parameter vom
// gleichen Typ haben, können Sie den Typnamen für die
// gleichtypierten Parameter bis zum letzten Parameter, der
// den Typ deklariert, weglassen.
func plusPlus(a, b, c int) int {
	return a + b + c
}

func main() {

	// Rufen Sie eine Funktion wie gewohnt mit `name(args)` auf.
	res := plus(1, 2)
	fmt.Println("1+2 =", res)

	res = plusPlus(1, 2, 3)
	fmt.Println("1+2+3 =", res)
}

```
