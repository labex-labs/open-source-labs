# Funciones de cadenas

Completa el código siguiente para imprimir la salida de varias funciones de cadenas proporcionadas por el paquete `strings`.

- Utiliza el paquete `strings` para completar la práctica.
- Utiliza la función `fmt.Println` para imprimir la salida.
- No modifiques el nombre de la función o los parámetros.

```sh
$ go run string-functions.go
Contains: true
Count: 2
HasPrefix: true
HasSuffix: true
Index: 1
Join: a-b
Repeat: aaaaa
Replace: f00
Replace: f0o
Split: [a b c d e]
ToLower: test
ToUpper: TEST
```

A continuación está el código completo:

```go
// El paquete `strings` de la biblioteca estándar proporciona muchas
// funciones útiles relacionadas con cadenas. Aquí hay algunos ejemplos
// para que tengas una idea del paquete.

package main

import (
	"fmt"
	s "strings"
)

// Alias de `fmt.Println` con un nombre más corto ya que lo usaremos
// mucho más adelante.
var p = fmt.Println

func main() {

	// Aquí hay un ejemplo de las funciones disponibles en
	// `strings`. Dado que estas son funciones del
	// paquete, no métodos del objeto string en sí mismo,
	// debemos pasar la cadena en cuestión como el primer
	// argumento a la función. Puedes encontrar más
	// funciones en la documentación del paquete [`strings`](https://pkg.go.dev/strings).
	p("Contains:  ", s.Contains("test", "es"))
	p("Count:     ", s.Count("test", "t"))
	p("HasPrefix: ", s.HasPrefix("test", "te"))
	p("HasSuffix: ", s.HasSuffix("test", "st"))
	p("Index:     ", s.Index("test", "e"))
	p("Join:      ", s.Join([]string{"a", "b"}, "-"))
	p("Repeat:    ", s.Repeat("a", 5))
	p("Replace:   ", s.Replace("foo", "o", "0", -1))
	p("Replace:   ", s.Replace("foo", "o", "0", 1))
	p("Split:     ", s.Split("a-b-c-d-e", "-"))
	p("ToLower:   ", s.ToLower("TEST"))
	p("ToUpper:   ", s.ToUpper("test"))
}

```
