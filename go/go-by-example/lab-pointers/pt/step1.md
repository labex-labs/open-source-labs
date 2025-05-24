# Ponteiros

O problema é entender como os ponteiros funcionam em contraste com os valores, com duas funções: `zeroval` e `zeroptr`. `zeroval` tem um parâmetro `int`, então os argumentos serão passados por valor. `zeroval` obterá uma cópia de `ival` distinta daquela na função de chamada. `zeroptr`, em contraste, tem um parâmetro `*int`, o que significa que ele recebe um ponteiro `int`. O código `*iptr` no corpo da função então _desreferencia_ o ponteiro de seu endereço de memória para o valor atual nesse endereço. Atribuir um valor a um ponteiro desreferenciado altera o valor no endereço referenciado.

- Você deve ter uma compreensão básica de Golang.
- Você deve saber como definir e usar funções em Golang.
- Você deve saber como usar ponteiros em Golang.

```sh
# `zeroval` não altera o `i` em `main`, mas
# `zeroptr` altera porque tem uma referência ao
# endereço de memória para essa variável.
$ go run pointers.go
initial: 1
zeroval: 1
zeroptr: 0
pointer: 0x42131100
```

Aqui está o código completo:

```go
// Go suporta <em><a href="https://en.wikipedia.org/wiki/Pointer_(computer_programming)">ponteiros</a></em>,
// permitindo que você passe referências a valores e registros
// dentro do seu programa.

package main

import "fmt"

// Vamos mostrar como os ponteiros funcionam em contraste com os valores com
// 2 funções: `zeroval` e `zeroptr`. `zeroval` tem um
// parâmetro `int`, então os argumentos serão passados por
// valor. `zeroval` obterá uma cópia de `ival` distinta
// daquela na função de chamada.
func zeroval(ival int) {
	ival = 0
}

// `zeroptr` em contraste tem um parâmetro `*int`, significando
// que ele recebe um ponteiro `int`. O código `*iptr` no
// corpo da função então _desreferencia_ o ponteiro de seu
// endereço de memória para o valor atual nesse endereço.
// Atribuir um valor a um ponteiro desreferenciado altera o
// valor no endereço referenciado.
func zeroptr(iptr *int) {
	*iptr = 0
}

func main() {
	i := 1
	fmt.Println("initial:", i)

	zeroval(i)
	fmt.Println("zeroval:", i)

	// A sintaxe `&i` fornece o endereço de memória de `i`,
	// ou seja, um ponteiro para `i`.
	zeroptr(&i)
	fmt.Println("zeroptr:", i)

	// Ponteiros também podem ser impressos.
	fmt.Println("pointer:", &i)
}

```
