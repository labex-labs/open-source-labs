# Arrays

Sie müssen ein Array von ganzen Zahlen mit einer Länge von 5 erstellen. Anschließend legen Sie einen Wert an einem bestimmten Index fest und erhalten einen Wert aus einem bestimmten Index. Sie müssen auch die Länge des Arrays ermitteln und ein Array in einer Zeile deklarieren und initialisieren. Schließlich erstellen Sie ein zweidimensionales Array und initialisieren es mit Werten.

- Erstellen Sie ein Array von ganzen Zahlen mit einer Länge von 5
- Legen Sie einen Wert an einem bestimmten Index fest und erhalten Sie einen Wert aus einem bestimmten Index
- Ermitteln Sie die Länge des Arrays
- Deklarieren und initialisieren Sie ein Array in einer Zeile
- Erstellen Sie ein zweidimensionales Array und initialisieren Sie es mit Werten

```sh
# Beachten Sie, dass Arrays im Format `[v1 v2 v3...]`
# erscheinen, wenn sie mit `fmt.Println` ausgegeben werden.
$ go run arrays.go
emp: [0 0 0 0 0]
set: [0 0 0 0 100]
get: 100
len: 5
dcl: [1 2 3 4 5]
2d: [[0 1 2] [1 2 3]]
```

Hier ist der vollständige Code:

```go
// In Go ist ein _Array_ eine nummerierte Folge von Elementen
// einer bestimmten Länge. In typischem Go-Code sind [Slices](slices)
// viel häufiger; Arrays sind in einigen speziellen Szenarien nützlich.

package main

import "fmt"

func main() {

	// Hier erstellen wir ein Array `a`, das genau
	// 5 `int`s aufnehmen wird. Der Typ der Elemente und die Länge
	// gehören beide zum Typ des Arrays. Standardmäßig ist ein Array
	// mit Nullwerten initialisiert, was für `int`s bedeutet, dass es `0`s sind.
	var a [5]int
	fmt.Println("emp:", a)

	// Wir können einen Wert an einem Index setzen, indem wir die
	// Syntax `array[index] = value` verwenden, und einen Wert mit
	// `array[index]` abrufen.
	a[4] = 100
	fmt.Println("set:", a)
	fmt.Println("get:", a[4])

	// Die eingebaut-funktion `len` gibt die Länge eines Arrays zurück.
	fmt.Println("len:", len(a))

	// Verwenden Sie diese Syntax, um ein Array in einer Zeile
	// zu deklarieren und zu initialisieren.
	b := [5]int{1, 2, 3, 4, 5}
	fmt.Println("dcl:", b)

	// Arraytypen sind eindimensional, aber Sie können
	// Typen kombinieren, um mehrdimensionale Datenstrukturen
	// zu erstellen.
	var twoD [2][3]int
	for i := 0; i < 2; i++ {
		for j := 0; j < 3; j++ {
			twoD[i][j] = i + j
		}
	}
	fmt.Println("2d: ", twoD)
}

```
