# Salida

El problema que se debe resolver en este laboratorio es salir de un programa de Go con un código de estado específico utilizando la función `os.Exit`.

Para completar este laboratorio, necesitarás tener un conocimiento básico de la programación en Go y del paquete `os`.

```sh
# Si ejecutas `exit.go` usando `go run`, la salida
# será capturada por `go` y mostrada.
$ go run exit.go
estado de salida 3

# Al compilar y ejecutar un binario, puedes ver
# el estado en la terminal.
$ go build exit.go
$./exit
$ echo $?
3

# Observa que el `!` de nuestro programa nunca se imprimió.
```

A continuación está el código completo:

```go
// Usa `os.Exit` para salir inmediatamente con un
// estado dado.

package main

import (
	"fmt"
	"os"
)

func main() {

	// Los `defer` no se ejecutarán cuando se use `os.Exit`, por lo que
	// esta llamada a `fmt.Println` nunca se hará.
	defer fmt.Println("!")

	// Sale con estado 3.
	os.Exit(3)
}

// Observa que a diferencia de, por ejemplo, C, Go no utiliza un valor
// de retorno entero de `main` para indicar el estado de salida. Si
// quieres salir con un estado no nulo, debes usar `os.Exit`.

```
