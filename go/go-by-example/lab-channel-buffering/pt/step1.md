# Bufferização de Canais (Channel Buffering)

Por padrão, os canais em Golang são não bufferizados (unbuffered), o que significa que eles só aceitam envios se houver uma recepção correspondente pronta para receber o valor enviado. No entanto, os canais bufferizados aceitam um número limitado de valores sem um receptor correspondente para esses valores. Neste laboratório, você deve criar um canal bufferizado e enviar valores para o canal sem uma recepção concorrente correspondente.

- Conhecimento básico de canais Golang
- Compreensão de canais bufferizados

```sh
$ go run channel-buffering.go
buffered
channel
```

A seguir, o código completo:

```go
// Por padrão, os canais são _não bufferizados_, o que significa que eles
// só aceitarão envios (`chan <-`) se houver uma
// recepção correspondente (`<- chan`) pronta para receber o
// valor enviado. _Canais bufferizados_ aceitam um número
// limitado de valores sem um receptor correspondente para
// esses valores.

package main

import "fmt"

func main() {

	// Aqui nós `make` um canal de strings bufferizando até
	// 2 valores.
	messages := make(chan string, 2)

	// Como este canal é bufferizado, podemos enviar estes
	// valores para o canal sem uma
	// recepção concorrente correspondente.
	messages <- "buffered"
	messages <- "channel"

	// Mais tarde, podemos receber estes dois valores como de costume.
	fmt.Println(<-messages)
	fmt.Println(<-messages)
}
```
