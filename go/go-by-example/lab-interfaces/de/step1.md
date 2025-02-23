# Schnittstellen

Das Problem besteht darin, eine Schnittstelle in Go zu implementieren. Dazu müssen wir einfach alle Methoden in der Schnittstelle implementieren. Hier implementieren wir `geometry` für `rect`s und `circle`s.

- Implementieren Sie eine Schnittstelle in Go.
- Implementieren Sie alle Methoden in der Schnittstelle.
- Verwenden Sie eine generische `measure`-Funktion, um mit jeder `geometry` zu arbeiten.
- Verwenden Sie Instanzen von `circle`- und `rect`-Strukturen als Argumente für `measure`.

```sh
$ go run interfaces.go
{3 4}
12
14
{5}
78.53981633974483
31.41592653589793

# Um mehr über Go's Schnittstellen zu erfahren, schauen Sie sich diesen
# [tollen Blogbeitrag](https://jordanorelli.tumblr.com/post/32665860244/how-to-use-interfaces-in-go) an.
```

Hier ist der vollständige Code:

```go
// _Schnittstellen_ sind benannte Sammlungen von Methodensignaturen.

package main

import (
	"fmt"
	"math"
)

// Hier ist eine einfache Schnittstelle für geometrische Formen.
type geometry interface {
	area() float64
	perim() float64
}

// Für unser Beispiel implementieren wir diese Schnittstelle für
// `rect`- und `circle`-Typen.
type rect struct {
	width, height float64
}
type circle struct {
	radius float64
}

// Um eine Schnittstelle in Go zu implementieren, müssen wir einfach
// alle Methoden in der Schnittstelle implementieren. Hier implementieren
// wir `geometry` für `rect`s.
func (r rect) area() float64 {
	return r.width * r.height
}
func (r rect) perim() float64 {
	return 2*r.width + 2*r.height
}

// Die Implementierung für `circle`s.
func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}
func (c circle) perim() float64 {
	return 2 * math.Pi * c.radius
}

// Wenn eine Variable einen Schnittstellentyp hat, können wir dann
// Methoden aufrufen, die in der benannten Schnittstelle vorhanden sind.
// Hier ist eine generische `measure`-Funktion, die dies nutzt, um mit
// jeder `geometry` zu arbeiten.
func measure(g geometry) {
	fmt.Println(g)
	fmt.Println(g.area())
	fmt.Println(g.perim())
}

func main() {
	r := rect{width: 3, height: 4}
	c := circle{radius: 5}

	// Die `circle`- und `rect`-Strukturtypen implementieren beide
	// die `geometry`-Schnittstelle, sodass wir Instanzen
	// dieser Strukturen als Argumente für `measure` verwenden können.
	measure(r)
	measure(c)
}

```
