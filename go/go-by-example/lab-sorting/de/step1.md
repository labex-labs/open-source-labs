# Sortieren

Das Problem, das in diesem Lab gelöst werden soll, ist es, Slices von Strings und ganzen Zahlen mit dem Paket `sort` zu sortieren.

- Das Paket `sort` muss importiert werden.
- Die Funktion `sort.Strings()` muss verwendet werden, um einen String-Slice zu sortieren.
- Die Funktion `sort.Ints()` muss verwendet werden, um einen Integer-Slice zu sortieren.
- Die Funktion `sort.IntsAreSorted()` muss verwendet werden, um zu überprüfen, ob ein Integer-Slice bereits sortiert ist.

```sh
# Wenn wir unser Programm ausführen, werden der sortierte String- und Int-Slice
# sowie `true` als Ergebnis unserer `AreSorted`-Prüfung ausgegeben.
$ go run sorting.go
Strings: [a b c]
Ints: [2 4 7]
Sorted: true
```

Hier ist der vollständige Code:

```go
// Go's `sort`-Paket implementiert die Sortierung für eingebautes
// und benutzerdefinierte Typen. Wir werden uns zuerst um die Sortierung
// von eingebauten kümmern.

package main

import (
	"fmt"
	"sort"
)

func main() {

	// Sortier-Methoden sind spezifisch für den eingebauten Typ;
	// hier ist ein Beispiel für Strings. Beachten Sie, dass die Sortierung
	// in-place erfolgt, sodass sie den gegebenen Slice ändert und keinen neuen zurückgibt.
	strs := []string{"c", "a", "b"}
	sort.Strings(strs)
	fmt.Println("Strings:", strs)

	// Ein Beispiel für die Sortierung von `int`s.
	ints := []int{7, 2, 4}
	sort.Ints(ints)
	fmt.Println("Ints:   ", ints)

	// Wir können auch `sort` verwenden, um zu überprüfen, ob ein Slice
	// bereits in sortierter Reihenfolge vorliegt.
	s := sort.IntsAreSorted(ints)
	fmt.Println("Sorted: ", s)
}

```
