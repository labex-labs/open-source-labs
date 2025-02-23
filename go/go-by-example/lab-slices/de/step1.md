# Slices

Das Problem, das in diesem Labor gelöst werden soll, ist es, Slice in Go zu erstellen und zu manipulieren. Sie müssen einen leeren Slice mit nicht null Länge erstellen, Werte im Slice setzen und abrufen, die `len`-Funktion verwenden, um die Länge des Slices zu erhalten, die `append`-Funktion verwenden, um neue Werte zum Slice hinzuzufügen, die `copy`-Funktion verwenden, um einen Slice zu kopieren, und den Slice-Operator verwenden, um einen Schnitt der Elemente aus einem bestehenden Slice zu erhalten.

Um dieses Labor abzuschließen, müssen Sie eine grundlegende Kenntnis der Go-Syntax und des Slice-Datentyps haben. Sie müssen auch vertraut sein mit den Funktionen `make`, `append` und `copy` sowie dem Slice-Operator.

```sh
# Beachten Sie, dass Slice zwar von Arrays unterschiedlicher Typ sind,
# aber von `fmt.Println` ähnlich gerendert werden.
$ go run slices.go
emp: [ ]
set: [a b c]
get: c
len: 3
apd: [a b c d e f]
cpy: [a b c d e f]
sl1: [c d e]
sl2: [a b c d e]
sl3: [c d e f]
dcl: [g h i]
2d: [[0] [1 2] [2 3 4]]

# Lesen Sie diesen [tollen Blogbeitrag](https://go.dev/blog/slices-intro)
# vom Go-Team, um mehr Details über das Design und
# die Implementierung von Slice in Go zu erhalten.

# Nachdem wir uns nun Arrays und Slice angeschaut haben, werden wir uns
# nun Go's anderen wichtigen eingebauten Datenstruktur: Maps, ansehen.
```

Hier ist der vollständige Code:

```go
// _Slice_ sind ein wichtiger Datentyp in Go und bieten
// eine leistungsfähigere Schnittstelle zu Sequenzen als Arrays.

package main

import "fmt"

func main() {

	// Im Gegensatz zu Arrays werden Slice nur durch die
	// Elemente typisiert, die sie enthalten (nicht die Anzahl der Elemente).
	// Um einen leeren Slice mit nicht null Länge zu erstellen, verwenden
	// Sie die eingebaut Funktion `make`. Hier erstellen wir einen Slice
	// von `string`s mit der Länge `3` (initially mit Nullen initialisiert).
	s := make([]string, 3)
	fmt.Println("emp:", s)

	// Wir können setzen und abrufen wie bei Arrays.
	s[0] = "a"
	s[1] = "b"
	s[2] = "c"
	fmt.Println("set:", s)
	fmt.Println("get:", s[2])

	// `len` gibt die Länge des Slices wie erwartet zurück.
	fmt.Println("len:", len(s))

	// Zusätzlich zu diesen grundlegenden Operationen unterstützen Slice
	// mehrere weitere, die sie leistungsfähiger machen als Arrays. Eine davon
	// ist die eingebaut Funktion `append`, die ein Slice zurückgibt, das
	// ein oder mehrere neue Werte enthält. Beachten Sie, dass wir einen
	// Rückgabewert von `append` akzeptieren müssen, da wir möglicherweise
	// einen neuen Slice-Wert erhalten.
	s = append(s, "d")
	s = append(s, "e", "f")
	fmt.Println("apd:", s)

	// Slice können auch kopiert werden. Hier erstellen wir einen
	// leeren Slice `c` der gleichen Länge wie `s` und kopieren
	// von `s` in `c`.
	c := make([]string, len(s))
	copy(c, s)
	fmt.Println("cpy:", c)

	// Slice unterstützen einen "Slice"-Operator mit der Syntax
	// `slice[low:high]`. Beispielsweise erhält man so einen Schnitt
	// der Elemente `s[2]`, `s[3]` und `s[4]`.
	l := s[2:5]
	fmt.Println("sl1:", l)

	// Dies schneidet bis (aber nicht einschließlich) `s[5]`.
	l = s[:5]
	fmt.Println("sl2:", l)

	// Und dies schneidet ab (und einschließlich) `s[2]`.
	l = s[2:]
	fmt.Println("sl3:", l)

	// Wir können auch eine Variable für einen Slice in einer
	// einzigen Zeile deklarieren und initialisieren.
	t := []string{"g", "h", "i"}
	fmt.Println("dcl:", t)

	// Slice können zu mehrdimensionalen Datenstrukturen zusammengesetzt
	// werden. Die Länge der inneren Slice kann variieren, im Gegensatz
	// zu mehrdimensionalen Arrays.
	twoD := make([][]int, 3)
	for i := 0; i < 3; i++ {
		innerLen := i + 1
		twoD[i] = make([]int, innerLen)
		for j := 0; j < innerLen; j++ {
			twoD[i][j] = i + j
		}
	}
	fmt.Println("2d: ", twoD)
}

```
