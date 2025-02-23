# Interfaces

El problema es implementar una interfaz en Go, solo necesitamos implementar todos los métodos de la interfaz. Aquí implementamos `geometry` en `rect`s y `circle`s.

- Implementar una interfaz en Go.
- Implementar todos los métodos de la interfaz.
- Utilizar una función genérica `measure` para trabajar con cualquier `geometry`.
- Utilizar instancias de los structs `circle` y `rect` como argumentos para `measure`.

```sh
$ go run interfaces.go
{3 4}
12
14
{5}
78.53981633974483
31.41592653589793

# Para aprender más sobre las interfaces de Go, consulta este
# [gran artículo del blog](https://jordanorelli.tumblr.com/post/32665860244/how-to-use-interfaces-in-go).
```

A continuación está el código completo:

```go
// Las _Interfaces_ son colecciones nombradas de firmas de métodos.

package main

import (
	"fmt"
	"math"
)

// Aquí está una interfaz básica para formas geométricas.
type geometry interface {
	area() float64
	perim() float64
}

// Para nuestro ejemplo implementaremos esta interfaz en
// los tipos `rect` y `circle`.
type rect struct {
	width, height float64
}
type circle struct {
	radius float64
}

// Para implementar una interfaz en Go, solo necesitamos
// implementar todos los métodos de la interfaz. Aquí
// implementamos `geometry` en `rect`s.
func (r rect) area() float64 {
	return r.width * r.height
}
func (r rect) perim() float64 {
	return 2*r.width + 2*r.height
}

// La implementación para `circle`s.
func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}
func (c circle) perim() float64 {
	return 2 * math.Pi * c.radius
}

// Si una variable tiene un tipo de interfaz, entonces
// podemos llamar a los métodos que están en la interfaz
// nombrada. Aquí está una función genérica `measure`
// que aprovecha esto para trabajar con cualquier
// `geometry`.
func measure(g geometry) {
	fmt.Println(g)
	fmt.Println(g.area())
	fmt.Println(g.perim())
}

func main() {
	r := rect{width: 3, height: 4}
	c := circle{radius: 5}

	// Los tipos de struct `circle` y `rect` ambos
	// implementan la interfaz `geometry` por lo que podemos
	// utilizar instancias de
	// estos structs como argumentos para `measure`.
	measure(r)
	measure(c)
}

```
