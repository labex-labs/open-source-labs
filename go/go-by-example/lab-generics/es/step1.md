# Genéricos

El problema que se debe resolver en esta práctica es entender cómo definir y usar funciones y tipos genéricos en Golang.

- Comprender el concepto de genéricos en Golang.
- Saber cómo definir funciones genéricas con parámetros y restricciones de tipo.
- Saber cómo definir tipos genéricos con parámetros de tipo.
- Comprender cómo definir métodos en tipos genéricos.
- Saber cómo invocar funciones genéricas con inferencia de tipo.

```sh
$ go run generics.go
keys: [4 1 2]
list: [10 13 23]
```

A continuación se muestra el código completo:

```go
// A partir de la versión 1.18, Go ha agregado soporte para
// _genéricos_, también conocidos como _parámetros de tipo_.

package main

import "fmt"

// Como ejemplo de una función genérica, `MapKeys` toma
// un mapa de cualquier tipo y devuelve una lista de sus claves.
// Esta función tiene dos parámetros de tipo - `K` y `V`;
// `K` tiene la restricción _comparable_, lo que significa que
// podemos comparar valores de este tipo con los operadores `==` y
// `!=`. Esto es necesario para las claves de mapa en Go.
// `V` tiene la restricción `any`, lo que significa que no está
// restringido de ninguna manera (`any` es un alias para `interface{}`).
func MapKeys[K comparable, V any](m map[K]V) []K {
	r := make([]K, 0, len(m))
	for k := range m {
		r = append(r, k)
	}
	return r
}

// Como ejemplo de un tipo genérico, `List` es una
// lista simplemente enlazada con valores de cualquier tipo.
type List[T any] struct {
	head, tail *element[T]
}

type element[T any] struct {
	next *element[T]
	val  T
}

// Podemos definir métodos en tipos genéricos igual que lo hacemos
// en tipos normales, pero tenemos que mantener los parámetros de tipo
// en su lugar. El tipo es `List[T]`, no `List`.
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

	// Cuando invocamos funciones genéricas, a menudo podemos confiar
	// en la _inferencia de tipo_. Tenga en cuenta que no tenemos que
	// especificar los tipos para `K` y `V` cuando
	// llamamos a `MapKeys` - el compilador los infiere
	// automáticamente.
	fmt.Println("keys:", MapKeys(m))

	//... aunque también podríamos especificarlos explícitamente.
	_ = MapKeys[int, string](m)

	lst := List[int]{}
	lst.Push(10)
	lst.Push(13)
	lst.Push(23)
	fmt.Println("list:", lst.GetAll())
}

```
