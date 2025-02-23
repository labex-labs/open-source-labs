# Tipos de Valor

Tu tarea es completar la función `calculate` que recibe dos enteros y devuelve su suma y producto.

- La función `calculate` debe recibir dos enteros como parámetros.
- La función `calculate` debe devolver dos enteros, la suma y el producto de los parámetros de entrada.

```sh
$ go run values.go
golang
1+1 = 2
7.0/3.0 = 2.3333333333333335
false
true
false
```

A continuación está el código completo:

```go
// Go tiene varios tipos de valor, incluyendo cadenas,
// enteros, flotantes, booleanos, etc. Aquí hay algunos
// ejemplos básicos.

package main

import "fmt"

func main() {

	// Cadenas, que se pueden sumar con `+`.
	fmt.Println("go" + "lang")

	// Enteros y flotantes.
	fmt.Println("1+1 =", 1+1)
	fmt.Println("7.0/3.0 =", 7.0/3.0)

	// Booleanos, con operadores booleanos como se esperaría.
	fmt.Println(true && false)
	fmt.Println(true || false)
	fmt.Println(!true)
}

```
