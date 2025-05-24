# Recursão

A função `sum` recebe uma fatia de inteiros e retorna a soma de todos os inteiros na fatia. No entanto, a função está incompleta e precisa ser implementada usando recursão.

- A função `sum` deve ser implementada usando recursão.
- A função deve receber uma fatia de inteiros como entrada.
- A função deve retornar a soma de todos os inteiros na fatia.

```sh
$ go run recursion.go
5040
13
```

A seguir, o código completo:

```go
// Go suporta
// <a href="https://en.wikipedia.org/wiki/Recursion_(computer_science)"><em>funções recursivas</em></a>.
// Aqui está um exemplo clássico.

package main

import "fmt"

// Esta função `fact` chama a si mesma até atingir o
// caso base de `fact(0)`.
func fact(n int) int {
	if n == 0 {
		return 1
	}
	return n * fact(n-1)
}

func main() {
	fmt.Println(fact(7))

	// Closures também podem ser recursivos, mas isso requer que o
	// closure seja declarado com um `var` tipado explicitamente
	// antes de ser definido.
	var fib func(n int) int

	fib = func(n int) int {
		if n < 2 {
			return n
		}

		// Como `fib` foi previamente declarado em `main`, Go
		// sabe qual função chamar com `fib` aqui.
		return fib(n-1) + fib(n-2)
	}

	fmt.Println(fib(7))
}
```
