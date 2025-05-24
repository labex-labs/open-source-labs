# Timeouts (Timeouts)

Quando os programas se conectam a recursos externos ou precisam limitar o tempo de execução, os timeouts são importantes. O laboratório é para implementar timeouts em Go usando canais (channels) e `select`.

- Implementar timeouts em Go usando canais e `select`.
- Usar um canal com buffer para evitar vazamentos de goroutine caso o canal nunca seja lido.
- Usar `time.After` para aguardar um valor a ser enviado após o timeout.
- Usar `select` para prosseguir com a primeira recepção que estiver pronta.

```sh
# Executar este programa mostra a primeira operação com timeout
# e a segunda com sucesso.
$ go run timeouts.go
timeout 1
result 2
```

A seguir, o código completo:

```go
// _Timeouts_ são importantes para programas que se conectam a
// recursos externos ou que de outra forma precisam limitar o
// tempo de execução. Implementar timeouts em Go é fácil e
// elegante graças aos canais e `select`.

package main

import (
	"fmt"
	"time"
)

func main() {

	// Para nosso exemplo, suponha que estamos executando uma chamada externa
	// que retorna seu resultado em um canal `c1`
	// após 2s. Observe que o canal é com buffer, então o
	// envio na goroutine é não bloqueante. Este é um
	// padrão comum para evitar vazamentos de goroutine caso o
	// canal nunca seja lido.
	c1 := make(chan string, 1)
	go func() {
		time.Sleep(2 * time.Second)
		c1 <- "result 1"
	}()

	// Aqui está o `select` implementando um timeout.
	// `res := <-c1` aguarda o resultado e `<-time.After`
	// aguarda um valor a ser enviado após o timeout de
	// 1s. Como `select` prossegue com a primeira
	// recepção que está pronta, pegaremos o caso de timeout
	// se a operação levar mais de 1s permitido.
	select {
	case res := <-c1:
		fmt.Println(res)
	case <-time.After(1 * time.Second):
		fmt.Println("timeout 1")
	}

	// Se permitirmos um timeout mais longo de 3s, então a recepção
	// de `c2` terá sucesso e imprimiremos o resultado.
	c2 := make(chan string, 1)
	go func() {
		time.Sleep(2 * time.Second)
		c2 <- "result 2"
	}()
	select {
	case res := <-c2:
		fmt.Println(res)
	case <-time.After(3 * time.Second):
		fmt.Println("timeout 2")
	}
}
```
