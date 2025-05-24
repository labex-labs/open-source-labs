# Iteração sobre Canais (Range Over Channels)

Você deve escrever uma função que recebe um canal de inteiros e retorna a soma de todos os inteiros recebidos do canal.

- A função deve ser chamada `sumInts`.
- A função deve receber um único parâmetro do tipo `chan int`.
- A função deve retornar um único valor inteiro.
- Você não pode usar nenhum loop ou recursão dentro do corpo da função.
- Você não pode usar nenhum pacote externo.

```sh
$ go run range-over-channels.go
one
two

# Este exemplo também mostrou que é possível fechar
# um canal não vazio, mas ainda ter os valores
# restantes recebidos.
```

Abaixo está o código completo:

```go
// Em um exemplo [anterior](range), vimos como `for` e
// `range` fornecem iteração sobre estruturas de dados básicas.
// Também podemos usar esta sintaxe para iterar sobre
// valores recebidos de um canal.

package main

import "fmt"

func main() {

	// Vamos iterar sobre 2 valores no canal `queue`.
	queue := make(chan string, 2)
	queue <- "one"
	queue <- "two"
	close(queue)

	// Este `range` itera sobre cada elemento conforme ele é
	// recebido de `queue`. Como nós `close`amos o
	// canal acima, a iteração termina após
	// receber os 2 elementos.
	for elem := range queue {
		fmt.Println(elem)
	}
}
```
