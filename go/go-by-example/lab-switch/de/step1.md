# Switch

In diesem Lab müssen Sie die `switch`-Anweisung vervollständigen, um die entsprechende Nachricht basierend auf dem Eingabewert auszugeben.

- Die `switch`-Anweisung muss verwendet werden, um das Problem zu lösen.
- Der `default`-Fall muss verwendet werden, um unerwartete Eingabewerte zu behandeln.

```sh
$ go run switch.go
Schreibe 2 als zwei
Es ist ein Werktag
Es ist nachmittags
Ich bin ein bool
Ich bin ein int
Kenne den Typ string nicht
```

Hier ist der vollständige Code:

```go
// _Switch-Anweisungen_ drücken bedingte Anweisungen über viele
// Zweige aus.

package main

import (
	"fmt"
	"time"
)

func main() {

	// Hier ist eine einfache `switch`.
	i := 2
	fmt.Print("Schreibe ", i, " als ")
	switch i {
	case 1:
		fmt.Println("eins")
	case 2:
		fmt.Println("zwei")
	case 3:
		fmt.Println("drei")
	}

	// Sie können Kommas verwenden, um mehrere Ausdrücke zu trennen
	// in der gleichen `case`-Anweisung. Wir verwenden auch den optionalen
	// `default`-Fall in diesem Beispiel.
	switch time.Now().Weekday() {
	case time.Saturday, time.Sunday:
		fmt.Println("Es ist das Wochenende")
	default:
		fmt.Println("Es ist ein Werktag")
	}

	// `switch` ohne einen Ausdruck ist eine alternative Möglichkeit,
	// um if/else-Logik auszudrücken. Hier zeigen wir auch, wie die
	// `case`-Ausdrücke nicht-konstant sein können.
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("Es ist vor dem Mittag")
	default:
		fmt.Println("Es ist nachmittags")
	}

	// Ein Typ `switch` vergleicht Typen anstelle von Werten.  Sie
	// können dies verwenden, um den Typ eines Schnittstellenwerts
	// zu ermitteln.  In diesem Beispiel wird die Variable `t` den
	// Typ haben, der der zugehörigen Klausel entspricht.
	whatAmI := func(i interface{}) {
		switch t := i.(type) {
		case bool:
			fmt.Println("Ich bin ein bool")
		case int:
			fmt.Println("Ich bin ein int")
		default:
			fmt.Printf("Kenne den Typ %T nicht\n", t)
		}
	}
	whatAmI(true)
	whatAmI(1)
	whatAmI("hey")
}

```
