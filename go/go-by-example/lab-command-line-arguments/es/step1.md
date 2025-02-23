# Argumentos de línea de comandos

El programa actualmente imprime los argumentos de línea de comandos brutos que se le pasan. Sin embargo, se debe modificar para imprimir argumentos específicos según su índice.

- Conocimientos básicos de Golang
- Familiaridad con los argumentos de línea de comandos

```sh
# Para experimentar con los argumentos de línea de comandos es mejor
# compilar un binario con `go build` primero.
$ go build command-line-arguments.go
$./command-line-arguments a b c d
[./command-line-arguments a b c d]
[a b c d]
c

# A continuación, veremos un procesamiento de línea de comandos más avanzado
# con flags.
```

A continuación está el código completo:

```go
// [_Argumentos de línea de comandos_](https://en.wikipedia.org/wiki/Command-line_interface#Arguments)
// son una forma común de parametrizar la ejecución de programas.
// Por ejemplo, `go run hello.go` utiliza los argumentos `run` y
// `hello.go` para el programa `go`.

package main

import (
	"fmt"
	"os"
)

func main() {

	// `os.Args` proporciona acceso a los argumentos de línea de comandos brutos.
	// Tenga en cuenta que el primer valor en este slice
	// es la ruta al programa, y `os.Args[1:]`
	// contiene los argumentos del programa.
	argsWithProg := os.Args
	argsWithoutProg := os.Args[1:]

	// Puede obtener argumentos individuales con la indexación normal.
	arg := os.Args[3]

	fmt.Println(argsWithProg)
	fmt.Println(argsWithoutProg)
	fmt.Println(arg)
}

```
