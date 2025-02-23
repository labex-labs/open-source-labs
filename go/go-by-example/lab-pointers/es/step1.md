# Punteros

El problema consiste en comprender cómo funcionan los punteros en contraste con los valores mediante dos funciones: `zeroval` y `zeroptr`. `zeroval` tiene un parámetro de tipo `int`, por lo que los argumentos se pasarán a ella por valor. `zeroval` obtendrá una copia de `ival` distinta de la que existe en la función llamante. En contraste, `zeroptr` tiene un parámetro de tipo `*int`, lo que significa que acepta un puntero a `int`. El código `*iptr` en el cuerpo de la función luego _desreferencia_ el puntero desde su dirección de memoria hasta el valor actual en esa dirección. Asignar un valor a un puntero desreferenciado cambia el valor en la dirección de memoria referenciada.

- Deberías tener un conocimiento básico de Golang.
- Deberías saber cómo definir y usar funciones en Golang.
- Deberías saber cómo usar punteros en Golang.

```sh
# `zeroval` no cambia la variable `i` en `main`, pero
# `zeroptr` sí lo hace porque tiene una referencia a
# la dirección de memoria de esa variable.
$ go run pointers.go
inicial: 1
zeroval: 1
zeroptr: 0
puntero: 0x42131100
```

A continuación se muestra el código completo:

```go
// Go admite <em><a href="https://en.wikipedia.org/wiki/Pointer_(computer_programming)">punteros</a></em>,
// lo que te permite pasar referencias a valores y registros
// dentro de tu programa.

package main

import "fmt"

// Mostraremos cómo funcionan los punteros en contraste con los valores con
// 2 funciones: `zeroval` y `zeroptr`. `zeroval` tiene un
// parámetro de tipo `int`, por lo que los argumentos se pasarán a ella por
// valor. `zeroval` obtendrá una copia de `ival` distinta
// de la que existe en la función llamante.
func zeroval(ival int) {
	ival = 0
}

// En contraste, `zeroptr` tiene un parámetro de tipo `*int`, lo que significa
// que acepta un puntero a `int`. El código `*iptr` en el
// cuerpo de la función luego _desreferencia_ el puntero desde su
// dirección de memoria hasta el valor actual en esa dirección.
// Asignar un valor a un puntero desreferenciado cambia el
// valor en la dirección de memoria referenciada.
func zeroptr(iptr *int) {
	*iptr = 0
}

func main() {
	i := 1
	fmt.Println("inicial:", i)

	zeroval(i)
	fmt.Println("zeroval:", i)

	// La sintaxis `&i` devuelve la dirección de memoria de `i`,
	// es decir, un puntero a `i`.
	zeroptr(&i)
	fmt.Println("zeroptr:", i)

	// Los punteros también se pueden imprimir.
	fmt.Println("puntero:", &i)
}

```
