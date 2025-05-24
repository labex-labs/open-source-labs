# `for`

O código abaixo contém diferentes tipos de laços `for`. No entanto, algumas partes do código estão incompletas, e você precisa preencher os espaços em branco para fazer o código funcionar corretamente.

- Conhecimento básico da sintaxe Golang
- Familiaridade com laços `for` em Golang

```sh
$ go run for.go
1
2
3
7
8
9
loop
1
3
5

# Veremos outras formas de `for` mais tarde, quando analisarmos
# as declarações `range`, canais e outras estruturas de dados.
```

Aqui está o código completo:

```go
// `for` é a única construção de loop do Go. Aqui estão
// alguns tipos básicos de laços `for`.

package main

import "fmt"

func main() {

	// O tipo mais básico, com uma única condição.
	i := 1
	for i <= 3 {
		fmt.Println(i)
		i = i + 1
	}

	// Um laço `for` clássico inicial/condição/após.
	for j := 7; j <= 9; j++ {
		fmt.Println(j)
	}

	// `for` sem uma condição irá iterar repetidamente
	// até que você `break` fora do laço ou `return` da
	// função que o envolve.
	for {
		fmt.Println("loop")
		break
	}

	// Você também pode `continue` para a próxima iteração do
	// laço.
	for n := 0; n <= 5; n++ {
		if n%2 == 0 {
			continue
		}
		fmt.Println(n)
	}
}
```
