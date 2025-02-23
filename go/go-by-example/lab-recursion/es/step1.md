# Recursividad

La función `sum` toma una slice de enteros y devuelve la suma de todos los enteros de la slice. Sin embargo, la función está incompleta y necesita ser implementada utilizando recursividad.

- La función `sum` debe ser implementada utilizando recursividad.
- La función debe tomar una slice de enteros como entrada.
- La función debe devolver la suma de todos los enteros de la slice.

```sh
$ go run recursion.go
5040
13
```

A continuación está el código completo:

```go
// Go soporta
// <a href="https://en.wikipedia.org/wiki/Recursion_(computer_science)"><em>funciones recursivas</em></a>.
// Aquí hay un ejemplo clásico.

package main

import "fmt"

// Esta función `fact` se llama a sí misma hasta que alcanza
// el caso base de `fact(0)`.
func fact(n int) int {
	if n == 0 {
		return 1
	}
	return n * fact(n-1)
}

func main() {
	fmt.Println(fact(7))

	// Las closures también pueden ser recursivas, pero esto requiere
	// que la closure sea declarada con una `var` tipada explícitamente
	// antes de ser definida.
	var fib func(n int) int

	fib = func(n int) int {
		if n < 2 {
			return n
		}

		// Dado que `fib` fue previamente declarada en `main`, Go
		// sabe qué función llamar con `fib` aquí.
		return fib(n-1) + fib(n-2)
	}

	fmt.Println(fib(7))
}

```
