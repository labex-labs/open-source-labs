# Variables de entorno

En esta práctica, deberás establecer, obtener y listar variables de entorno.

- Utiliza `os.Setenv` para establecer un par clave/valor.
- Utiliza `os.Getenv` para obtener un valor para una clave.
- Utiliza `os.Environ` para listar todos los pares clave/valor del entorno.
- Utiliza `strings.SplitN` para dividir la clave y el valor.

```sh
# Al ejecutar el programa se muestra que recogemos el valor
# de `FOO` que establecemos en el programa, pero que
# `BAR` está vacío.
$ go run environment-variables.go
FOO: 1
BAR:

# La lista de claves del entorno dependerá de tu
# máquina en particular.
TERM_PROGRAM
PATH
SHELL
...
FOO

# Si establecemos `BAR` en el entorno primero, el programa
# en ejecución recoge ese valor.
$ BAR=2 go run environment-variables.go
FOO: 1
BAR: 2
...
```

A continuación está el código completo:

```go
// [Variables de entorno](https://en.wikipedia.org/wiki/Environment_variable)
// son un mecanismo universal para [transmitir información
// de configuración a los programas Unix](https://www.12factor.net/config).
// Echemos un vistazo a cómo establecer, obtener y listar variables de entorno.

package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {

	// Para establecer un par clave/valor, utiliza `os.Setenv`. Para obtener
	// un valor para una clave, utiliza `os.Getenv`. Esto devolverá
	// una cadena vacía si la clave no está presente en el entorno.
	os.Setenv("FOO", "1")
	fmt.Println("FOO:", os.Getenv("FOO"))
	fmt.Println("BAR:", os.Getenv("BAR"))

	// Utiliza `os.Environ` para listar todos los pares clave/valor del
	// entorno. Esto devuelve una slice de strings en la forma `KEY=value`.
	// Puedes `strings.SplitN` para obtener la clave y el valor. Aquí
	// imprimimos todas las claves.
	fmt.Println()
	for _, e := range os.Environ() {
		pair := strings.SplitN(e, "=", 2)
		fmt.Println(pair[0])
	}
}

```
