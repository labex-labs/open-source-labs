# Interfaces

O problema é implementar uma interface em Go, basta implementar todos os métodos na interface. Aqui implementamos `geometry` em `rect`s e `circle`s.

- Implementar uma interface em Go.
- Implementar todos os métodos na interface.
- Usar uma função genérica `measure` para trabalhar em qualquer `geometry`.
- Usar instâncias das structs `circle` e `rect` como argumentos para `measure`.

```sh
$ go run interfaces.go
{3 4}
12
14
{5}
78.53981633974483
31.41592653589793

# Para saber mais sobre interfaces em Go, confira este
# [ótimo post de blog](https://jordanorelli.tumblr.com/post/32665860244/how-to-use-interfaces-in-go).
```

Aqui está o código completo:

```go
// _Interfaces_ são coleções nomeadas de assinaturas de métodos.

package main

import (
	"fmt"
	"math"
)

// Aqui está uma interface básica para formas geométricas.
type geometry interface {
	area() float64
	perim() float64
}

// Para nosso exemplo, implementaremos esta interface nos tipos
// `rect` e `circle`.
type rect struct {
	width, height float64
}
type circle struct {
	radius float64
}

// Para implementar uma interface em Go, basta
// implementar todos os métodos na interface. Aqui nós
// implementamos `geometry` em `rect`s.
func (r rect) area() float64 {
	return r.width * r.height
}
func (r rect) perim() float64 {
	return 2*r.width + 2*r.height
}

// A implementação para `circle`s.
func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}
func (c circle) perim() float64 {
	return 2 * math.Pi * c.radius
}

// Se uma variável tem um tipo de interface, então podemos chamar
// métodos que estão na interface nomeada. Aqui está uma
// função genérica `measure` aproveitando isso
// para trabalhar em qualquer `geometry`.
func measure(g geometry) {
	fmt.Println(g)
	fmt.Println(g.area())
	fmt.Println(g.perim())
}

func main() {
	r := rect{width: 3, height: 4}
	c := circle{radius: 5}

	// Os tipos de struct `circle` e `rect` ambos
	// implementam a interface `geometry`, então podemos usar
	// instâncias destas
	// structs como argumentos para `measure`.
	measure(r)
	measure(c)
}
```
