# Filtros de línea

El problema que se debe resolver en este laboratorio es escribir un programa en Go que lea el texto de entrada desde stdin, ponga en mayúsculas todas las letras del texto y luego imprima el texto modificado en stdout.

- El programa debe leer el texto de entrada desde stdin.
- El programa debe poner en mayúsculas todas las letras del texto de entrada.
- El programa debe imprimir el texto modificado en stdout.

```sh
# Para probar nuestro filtro de línea, primero crea un archivo
# con algunas líneas en minúsculas.
$ echo 'hello' > /tmp/lines
$ echo 'filter' >> /tmp/lines

# Luego utiliza el filtro de línea para obtener líneas en mayúsculas.
$ cat /tmp/lines | go run line-filters.go
HELLO
FILTER
```

A continuación está el código completo:

```go
// Un _filtro de línea_ es un tipo común de programa que lee
// la entrada en stdin, la procesa y luego imprime algún
// resultado derivado en stdout. `grep` y `sed` son filtros
// de línea comunes.

// Aquí hay un ejemplo de filtro de línea en Go que escribe una
// versión en mayúsculas de todo el texto de entrada. Puedes utilizar
// este patrón para escribir tus propios filtros de línea en Go.
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {

	// Envolver `os.Stdin` no bufferizado con un
	// escáner bufferizado nos da un método `Scan` conveniente
	// que avanza el escáner al siguiente token; que es la
	// siguiente línea en el escáner predeterminado.
	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		// `Text` devuelve el token actual, aquí la siguiente línea,
		// de la entrada.
		ucl := strings.ToUpper(scanner.Text())

		// Escribe la línea en mayúsculas.
		fmt.Println(ucl)
	}

	// Comprueba si hay errores durante `Scan`. El final de archivo
	// es esperado y no se informa como un error por `Scan`.
	if err := scanner.Err(); err!= nil {
		fmt.Fprintln(os.Stderr, "error:", err)
		os.Exit(1)
	}
}

```
