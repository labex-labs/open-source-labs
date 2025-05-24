# Tipos de Valor

Sua tarefa é completar a função `calculate` que recebe dois inteiros e retorna sua soma e produto.

- A função `calculate` deve receber dois inteiros como parâmetros.
- A função `calculate` deve retornar dois inteiros, a soma e o produto dos parâmetros de entrada.

```sh
$ go run values.go
golang
1+1 = 2
7.0/3.0 = 2.3333333333333335
false
true
false
```

A seguir, o código completo:

```go
// Go tem vários tipos de valor, incluindo strings,
// inteiros, floats, booleanos, etc. Aqui estão alguns
// exemplos básicos.

package main

import "fmt"

func main() {

	// Strings, que podem ser adicionadas com `+`.
	fmt.Println("go" + "lang")

	// Inteiros e floats.
	fmt.Println("1+1 =", 1+1)
	fmt.Println("7.0/3.0 =", 7.0/3.0)

	// Booleanos, com operadores booleanos como você esperaria.
	fmt.Println(true && false)
	fmt.Println(true || false)
	fmt.Println(!true)
}
```
