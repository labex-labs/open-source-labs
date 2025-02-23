# Variadische Funktionen

In diesem Lab müssen Sie eine Funktion namens `max` implementieren, die beliebig viele ganze Zahlen als Argumente annimmt und den maximalen Wert zurückgibt.

- Die Funktion `max` sollte beliebig viele ganze Zahlen als Argumente akzeptieren.
- Die Funktion `max` sollte den maximalen Wert der als Argumente übergebenen ganzen Zahlen zurückgeben.

```sh
$ go run variadic-functions.go
[1 2] 3
[1 2 3] 6
[1 2 3 4] 10

# Ein weiterer wichtiger Aspekt von Funktionen in Go ist ihre Fähigkeit,
# Closures zu bilden, auf die wir im nächsten Schritt eingehen werden.
```

Hier ist der vollständige Code:

```go
// [_Variadische Funktionen_](https://en.wikipedia.org/wiki/Variadic_function)
// können mit beliebig vielen Nachfolgeargumenten aufgerufen werden.
// Beispielsweise ist `fmt.Println` eine häufige variadische
// Funktion.

package main

import "fmt"

// Hier ist eine Funktion, die beliebig viele `int`s als Argumente annimmt.
func sum(nums...int) {
	fmt.Print(nums, " ")
	total := 0
	// Innerhalb der Funktion ist der Typ von `nums`
	// gleichwertig mit `[]int`. Wir können `len(nums)` aufrufen,
	// mit `range` darüber iterieren usw.
	for _, num := range nums {
		total += num
	}
	fmt.Println(total)
}

func main() {

	// Variadische Funktionen können auf die übliche Weise
	// mit einzelnen Argumenten aufgerufen werden.
	sum(1, 2)
	sum(1, 2, 3)

	// Wenn Sie bereits mehrere Argumente in einem Slice haben,
	// wenden Sie sie auf eine variadische Funktion an, indem Sie
	// `func(slice...)` wie folgt verwenden.
	nums := []int{1, 2, 3, 4}
	sum(nums...)
}

```
