# Variables

Se te pide que completes el código para declarar e inicializar variables de diferentes tipos en Golang.

- Conocimientos básicos de la sintaxis de Golang
- Familiaridad con la declaración e inicialización de variables en Golang

```sh
$ go run variables.go
inicial
1 2
true
0
manzana
```

A continuación está el código completo:

```go
// En Go, las _variables_ se declaran explícitamente y se usan por
// el compilador para, por ejemplo, comprobar la corrección de tipos
// de las llamadas a funciones.

package main

import "fmt"

func main() {

	// `var` declara una o más variables.
	var a = "inicial"
	fmt.Println(a)

	// Puedes declarar múltiples variables a la vez.
	var b, c int = 1, 2
	fmt.Println(b, c)

	// Go inferirá el tipo de las variables inicializadas.
	var d = true
	fmt.Println(d)

	// Las variables declaradas sin una inicialización
	// correspondiente tienen un _valor cero_. Por ejemplo, el
	// valor cero para un `int` es `0`.
	var e int
	fmt.Println(e)

	// La sintaxis `:=` es un atajo para declarar e inicializar
	// una variable, por ejemplo, para `var f string = "manzana"`
	// en este caso. Esta sintaxis solo está disponible dentro de
	// funciones.
	f := "manzana"
	fmt.Println(f)
}

```
