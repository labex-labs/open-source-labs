# Variáveis

Você deve completar o código para declarar e inicializar variáveis de diferentes tipos em Golang.

- Conhecimento básico da sintaxe Golang
- Familiaridade com a declaração e inicialização de variáveis em Golang

```sh
$ go run variables.go
initial
1 2
true
0
apple
```

A seguir, o código completo:

```go
// Em Go, _variáveis_ são explicitamente declaradas e usadas pelo
// compilador para, por exemplo, verificar a correção de tipo (type-correctness) das chamadas de função.

package main

import "fmt"

func main() {

	// `var` declara 1 ou mais variáveis.
	var a = "initial"
	fmt.Println(a)

	// Você pode declarar múltiplas variáveis de uma vez.
	var b, c int = 1, 2
	fmt.Println(b, c)

	// Go irá inferir o tipo das variáveis inicializadas.
	var d = true
	fmt.Println(d)

	// Variáveis declaradas sem uma
	// inicialização correspondente são _zero-valued_ (com valor zero). Por exemplo, o
	// valor zero para um `int` é `0`.
	var e int
	fmt.Println(e)

	// A sintaxe `:=` é uma abreviação para declarar e
	// inicializar uma variável, por exemplo, para
	// `var f string = "apple"` neste caso.
	// Esta sintaxe está disponível apenas dentro de funções.
	f := "apple"
	fmt.Println(f)
}
```
