# Múltiplos Valores de Retorno

Complete a função `swap` para retornar dois parâmetros de entrada em ordem inversa.

- A função `swap` deve receber dois inteiros como parâmetros de entrada.
- A função `swap` deve retornar dois inteiros em ordem inversa.

```sh
$ go run multiple-return-values.go
3
7
7

# Aceitar um número variável de argumentos é outra boa
# característica das funções Go; veremos isso a seguir.
```

Abaixo está o código completo:

```go
// Go tem suporte embutido para _múltiplos valores de retorno_.
// Este recurso é usado frequentemente em Go idiomático, por exemplo,
// para retornar tanto o resultado quanto os valores de erro de uma função.

package main

import "fmt"

// O `(int, int)` na assinatura desta função mostra que
// a função retorna 2 `int`s.
func vals() (int, int) {
	return 3, 7
}

func main() {

	// Aqui usamos os 2 diferentes valores de retorno da
	// chamada com _atribuição múltipla_.
	a, b := vals()
	fmt.Println(a)
	fmt.Println(b)

	// Se você só quer um subconjunto dos valores retornados,
	// use o identificador em branco `_`.
	_, c := vals()
	fmt.Println(c)
}
```
