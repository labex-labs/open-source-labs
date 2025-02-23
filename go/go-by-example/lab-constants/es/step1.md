# Constantes

El problema a resolver es demostrar el uso de constantes en Golang para valores de carácter, cadena, booleano y numéricos.

El laboratorio tiene los siguientes requisitos:

- Utilice la palabra clave `const` para declarar un valor constante.
- Las constantes deben ser de valores de carácter, cadena, booleano y numéricos.
- Una declaración de constante puede aparecer en cualquier lugar donde una declaración `var` pueda aparecer.
- Demuestre que las expresiones constantes realizan operaciones aritméticas con precisión arbitraria.
- Una constante numérica no tiene tipo hasta que se le asigna uno, por ejemplo, mediante una conversión explícita.
- Un número puede ser dado un tipo al usarlo en un contexto que lo requiera, como una asignación de variable o una llamada a función.

```sh
$ go run constant.go
constant
6e+11
600000000000
-0.28470407323754404
```

A continuación está el código completo:

```go
// Go admite _constantes_ de valores de carácter, cadena,
// booleano y numéricos.

package main

import (
	"fmt"
	"math"
)

// `const` declara un valor constante.
const s string = "constant"

func main() {
	fmt.Println(s)

	// Una declaración `const` puede aparecer en cualquier lugar donde una declaración `var`
	// pueda aparecer.
	const n = 500000000

	// Las expresiones constantes realizan operaciones aritméticas con
	// precisión arbitraria.
	const d = 3e20 / n
	fmt.Println(d)

	// Una constante numérica no tiene tipo hasta que se le asigna
	// uno, por ejemplo, mediante una conversión explícita.
	fmt.Println(int64(d))

	// Un número puede ser dado un tipo al usarlo en un
	// contexto que lo requiera, como una asignación de variable
	// o una llamada a función. Por ejemplo, aquí
	// `math.Sin` espera un `float64`.
	fmt.Println(math.Sin(n))
}

```
