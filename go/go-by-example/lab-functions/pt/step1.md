# Funções

No código fornecido, temos duas funções `plus` e `plusPlus`. A função `plus` recebe dois inteiros como argumentos e retorna sua soma. A função `plusPlus` recebe três inteiros como argumentos e retorna sua soma. Sua tarefa é completar a função `plusPlus` adicionando o terceiro inteiro à soma dos dois primeiros inteiros.

- A função `plus` deve receber dois inteiros como argumentos e retornar sua soma como um inteiro.
- A função `plusPlus` deve receber três inteiros como argumentos e retornar sua soma como um inteiro.
- A função `plusPlus` deve usar a função `plus` para calcular a soma dos dois primeiros inteiros.

```sh
$ go run functions.go
1+2 = 3
1+2+3 = 6

# Existem vários outros recursos para as funções Go. Um deles é
# múltiplos valores de retorno, que veremos a seguir.
```

Abaixo está o código completo:

```go
// _Funções_ são centrais em Go. Aprenderemos sobre
// funções com alguns exemplos diferentes.

package main

import "fmt"

// Aqui está uma função que recebe dois `int`s e retorna
// sua soma como um `int`.
func plus(a int, b int) int {

	// Go requer retornos explícitos, ou seja, não
	// retornará automaticamente o valor da última
	// expressão.
	return a + b
}

// Quando você tem múltiplos parâmetros consecutivos do
// mesmo tipo, você pode omitir o nome do tipo para os
// parâmetros do mesmo tipo até o parâmetro final que
// declara o tipo.
func plusPlus(a, b, c int) int {
	return a + b + c
}

func main() {

	// Chame uma função como você esperaria, com
	// `name(args)`.
	res := plus(1, 2)
	fmt.Println("1+2 =", res)

	res = plusPlus(1, 2, 3)
	fmt.Println("1+2+3 =", res)
}
```
