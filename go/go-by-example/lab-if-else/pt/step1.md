# if-else

Você deve completar a função `checkNumber` que recebe um inteiro como entrada e retorna uma string. Se o número for par, retorne "even", caso contrário, retorne "odd".

- A função deve ser chamada `checkNumber`.
- A função deve receber um inteiro como entrada.
- A função deve retornar uma string.
- Se o número for par, retorne "even".
- Se o número for ímpar, retorne "odd".

```sh
$ go run if-else.go
7 is odd
8 is divisible by 4
9 has 1 digit

# Não existe [ternary if](https://en.wikipedia.org/wiki/%3F:)
# em Go, então você precisará usar uma instrução `if` completa mesmo
# para condições básicas.
```

Abaixo está o código completo:

```go
// A ramificação com `if` e `else` em Go é
// direta.

package main

import "fmt"

func main() {

	// Aqui está um exemplo básico.
	if 7%2 == 0 {
		fmt.Println("7 is even")
	} else {
		fmt.Println("7 is odd")
	}

	// Você pode ter uma instrução `if` sem um else.
	if 8%4 == 0 {
		fmt.Println("8 is divisible by 4")
	}

	// Uma instrução pode preceder condicionais; quaisquer variáveis
	// declaradas nesta instrução estão disponíveis na atual
	// e em todas as ramificações subsequentes.
	if num := 9; num < 0 {
		fmt.Println(num, "is negative")
	} else if num < 10 {
		fmt.Println(num, "has 1 digit")
	} else {
		fmt.Println(num, "has multiple digits")
	}
}

// Observe que você não precisa de parênteses em torno das condições
// em Go, mas que as chaves são obrigatórias.
```
