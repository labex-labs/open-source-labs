# Funções Variádicas (Variadic Functions)

Neste laboratório, você precisa implementar uma função chamada `max` que recebe um número arbitrário de inteiros como argumentos e retorna o valor máximo.

- A função `max` deve receber um número arbitrário de inteiros como argumentos.
- A função `max` deve retornar o valor máximo dos inteiros passados como argumentos.

```sh
$ go run variadic-functions.go
[1 2] 3
[1 2 3] 6
[1 2 3 4] 10

# Outro aspecto chave das funções em Go é sua capacidade
# de formar closures, que veremos a seguir.
```

A seguir, o código completo:

```go
// [_Funções variádicas_](https://en.wikipedia.org/wiki/Variadic_function)
// podem ser chamadas com qualquer número de argumentos finais.
// Por exemplo, `fmt.Println` é uma função variádica comum.

package main

import "fmt"

// Aqui está uma função que receberá um número arbitrário
// de `int`s como argumentos.
func sum(nums ...int) {
	fmt.Print(nums, " ")
	total := 0
	// Dentro da função, o tipo de `nums` é
	// equivalente a `[]int`. Podemos chamar `len(nums)`,
	// iterar sobre ele com `range`, etc.
	for _, num := range nums {
		total += num
	}
	fmt.Println(total)
}

func main() {

	// Funções variádicas podem ser chamadas da maneira usual
	// com argumentos individuais.
	sum(1, 2)
	sum(1, 2, 3)

	// Se você já tem múltiplos argumentos em uma slice,
	// aplique-os a uma função variádica usando
	// `func(slice...)` assim.
	nums := []int{1, 2, 3, 4}
	sum(nums...)
}
```
