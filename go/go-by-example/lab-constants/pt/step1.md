# Constantes

O problema a ser resolvido é demonstrar o uso de constantes em Golang para valores de caractere, string, booleano e numéricos.

O laboratório possui os seguintes requisitos:

- Use a palavra-chave `const` para declarar um valor constante.
- As constantes devem ser de valores de caractere, string, booleano e numéricos.
- Uma declaração de constante pode aparecer em qualquer lugar onde uma declaração `var` possa.
- Demonstre que expressões constantes realizam aritmética com precisão arbitrária.
- Uma constante numérica não tem tipo até que lhe seja dado um, como por uma conversão explícita.
- Um número pode receber um tipo usando-o em um contexto que o exige, como uma atribuição de variável ou chamada de função.

```sh
$ go run constant.go
constant
6e+11
600000000000
-0.28470407323754404
```

A seguir, o código completo:

```go
// Go suporta _constantes_ de valores de caractere, string, booleano,
// e numéricos.

package main

import (
	"fmt"
	"math"
)

// `const` declara um valor constante.
const s string = "constant"

func main() {
	fmt.Println(s)

	// Uma declaração `const` pode aparecer em qualquer lugar onde uma declaração `var`
	// possa.
	const n = 500000000

	// Expressões constantes realizam aritmética com
	// precisão arbitrária.
	const d = 3e20 / n
	fmt.Println(d)

	// Uma constante numérica não tem tipo até que lhe seja dado
	// um, como por uma conversão explícita.
	fmt.Println(int64(d))

	// Um número pode receber um tipo usando-o em um
	// contexto que o exige, como uma atribuição de variável
	// ou chamada de função. Por exemplo, aqui
	// `math.Sin` espera um `float64`.
	fmt.Println(math.Sin(n))
}
```
