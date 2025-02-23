# `for`

El código siguiente contiene diferentes tipos de bucles `for`. Sin embargo, algunas partes del código están incompletas y debes completar los espacios en blanco para que el código funcione correctamente.

- Conocimientos básicos de la sintaxis de Golang
- Familiaridad con los bucles `for` en Golang

```sh
$ go run for.go
1
2
3
7
8
9
loop
1
3
5

# Veremos otras formas de `for` más adelante cuando veamos
# las declaraciones `range`, los canales y otras estructuras
# de datos.
```

A continuación está el código completo:

```go
// `for` es la única estructura de bucle en Go. Aquí están
// algunos de los tipos básicos de bucles `for`.

package main

import "fmt"

func main() {

	// El tipo más básico, con una sola condición.
	i := 1
	for i <= 3 {
		fmt.Println(i)
		i = i + 1
	}

	// Un bucle `for` clásico con inicialización/condición/post-incremento.
	for j := 7; j <= 9; j++ {
		fmt.Println(j)
	}

	// `for` sin una condición se ejecutará repetidamente
	// hasta que salgas del bucle con `break` o `return` de
	// la función envolvente.
	for {
		fmt.Println("loop")
		break
	}

	// También puedes usar `continue` para pasar a la siguiente
	// iteración del bucle.
	for n := 0; n <= 5; n++ {
		if n%2 == 0 {
			continue
		}
		fmt.Println(n)
	}
}

```
