# Werttypen

Ihre Aufgabe ist es, die `calculate`-Funktion abzuschließen, die zwei Ganzzahlen entgegennimmt und deren Summe und Produkt zurückgibt.

- Die `calculate`-Funktion sollte zwei Ganzzahlen als Parameter entgegennehmen.
- Die `calculate`-Funktion sollte zwei Ganzzahlen zurückgeben, die Summe und das Produkt der Eingabeparameter.

```sh
$ go run values.go
golang
1+1 = 2
7.0/3.0 = 2.3333333333333335
false
true
false
```

Hier ist der vollständige Code:

```go
// Go hat verschiedene Werttypen, darunter Zeichenketten,
// Ganzzahlen, Gleitkommazahlen, Boolesche Werte usw. Hier sind ein paar
// grundlegende Beispiele.

package main

import "fmt"

func main() {

	// Zeichenketten, die mit `+` zusammengefügt werden können.
	fmt.Println("go" + "lang")

	// Ganzzahlen und Gleitkommazahlen.
	fmt.Println("1+1 =", 1+1)
	fmt.Println("7.0/3.0 =", 7.0/3.0)

	// Boolesche Werte mit den erwarteten booleschen Operatoren.
	fmt.Println(true && false)
	fmt.Println(true || false)
	fmt.Println(!true)
}

```
