# Range

Das Problem, das in diesem Lab gelöst werden soll, ist es, zu demonstrieren, wie `range` mit Slices, Arrays, Maps und Strings verwendet wird.

Um dieses Lab abzuschließen, benötigen Sie:

- Grundkenntnisse der Golang-Syntax
- Golang auf Ihrem Computer installiert

```sh
$ go run range.go
sum: 9
index: 1
a - > apple
b - > banana
key: a
key: b
0 103
1 111
```

Hier ist der vollständige Code:

```go
// _range_ iteriert über Elemente in verschiedenen Datenstrukturen.
// Schauen wir uns an, wie `range` mit einigen der Datenstrukturen,
// die wir bereits gelernt haben, verwendet wird.

package main

import "fmt"

func main() {

	// Hier verwenden wir `range`, um die Zahlen in einem Slice zu summieren.
	// Arrays funktionieren genauso.
	nums := []int{2, 3, 4}
	sum := 0
	for _, num := range nums {
		sum += num
	}
	fmt.Println("sum:", sum)

	// `range` auf Arrays und Slices liefert sowohl den Index als auch den Wert für jedes Element.
	// Oben haben wir den Index nicht benötigt, daher haben wir ihn mit dem Platzhalter `_` ignoriert.
	// Manchmal möchten wir aber tatsächlich die Indizes.
	for i, num := range nums {
		if num == 3 {
			fmt.Println("index:", i)
		}
	}

	// `range` auf einer Map iteriert über Schlüssel/Wert-Paare.
	kvs := map[string]string{"a": "apple", "b": "banana"}
	for k, v := range kvs {
		fmt.Printf("%s -> %s\n", k, v)
	}

	// `range` kann auch nur über die Schlüssel einer Map iterieren.
	for k := range kvs {
		fmt.Println("key:", k)
	}

	// `range` auf Strings iteriert über Unicode-Codepunkte.
	// Der erste Wert ist der Startbyte-Index des `rune`, der zweite der `rune` selbst.
	// Siehe [Strings and Runes](strings-and-runes) für weitere Details.
	for i, c := range "go" {
		fmt.Println(i, c)
	}
}

```
