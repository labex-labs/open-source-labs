# Generics

Das Problem, das in diesem Lab gelöst werden soll, ist es, zu verstehen, wie man generische Funktionen und Typen in Golang definiert und verwendet.

- Verstehen Sie das Konzept der Generics in Golang.
- Wissen Sie, wie man generische Funktionen mit Typ-Parametern und -Beschränkungen definiert.
- Wissen Sie, wie man generische Typen mit Typ-Parametern definiert.
- Verstehen Sie, wie man Methoden auf generischen Typen definiert.
- Wissen Sie, wie man generische Funktionen mit Typ-Schlussfolgerung aufruft.

```sh
$ go run generics.go
keys: [4 1 2]
list: [10 13 23]
```

Hier ist der vollständige Code:

```go
// Ab Version 1.18 hat Go die Unterstützung für
// _Generics_, auch bekannt als _Typ-Parameter_, hinzugefügt.

package main

import "fmt"

// Als Beispiel für eine generische Funktion nimmt `MapKeys`
// eine Map beliebigen Typs und gibt eine Liste ihrer Schlüssel zurück.
// Diese Funktion hat zwei Typ-Parameter - `K` und `V`;
// `K` hat die _Beschränkung_ `comparable`, was bedeutet, dass
// wir Werte dieses Typs mit den Operatoren `==` und
// `!=` vergleichen können. Dies ist für Map-Schlüssel in Go erforderlich.
// `V` hat die `any`-Beschränkung, was bedeutet, dass es
// auf keiner Weise eingeschränkt ist (`any` ist ein Alias für `interface{}`).
func MapKeys[K comparable, V any](m map[K]V) []K {
	r := make([]K, 0, len(m))
	for k := range m {
		r = append(r, k)
	}
	return r
}

// Als Beispiel für einen generischen Typ ist `List` eine
// einfach verkettete Liste mit Werten beliebigen Typs.
type List[T any] struct {
	head, tail *element[T]
}

type element[T any] struct {
	next *element[T]
	val  T
}

// Wir können Methoden auf generischen Typen genauso definieren wie
// auf regulären Typen, müssen aber die Typ-Parameter beibehalten.
// Der Typ ist `List[T]`, nicht `List`.
func (lst *List[T]) Push(v T) {
	if lst.tail == nil {
		lst.head = &element[T]{val: v}
		lst.tail = lst.head
	} else {
		lst.tail.next = &element[T]{val: v}
		lst.tail = lst.tail.next
	}
}

func (lst *List[T]) GetAll() []T {
	var elems []T
	for e := lst.head; e!= nil; e = e.next {
		elems = append(elems, e.val)
	}
	return elems
}

func main() {
	var m = map[int]string{1: "2", 2: "4", 4: "8"}

	// Wenn wir generische Funktionen aufrufen, können wir uns oft auf
	// _Typ-Schlussfolgerung_ verlassen. Beachten Sie, dass wir die Typen
	// für `K` und `V` nicht angeben müssen, wenn wir
	// `MapKeys` aufrufen - der Compiler schließt sie automatisch.
	fmt.Println("keys:", MapKeys(m))

	//... obwohl wir sie auch explizit angeben könnten.
	_ = MapKeys[int, string](m)

	lst := List[int]{}
	lst.Push(10)
	lst.Push(13)
	lst.Push(23)
	fmt.Println("list:", lst.GetAll())
}

```
