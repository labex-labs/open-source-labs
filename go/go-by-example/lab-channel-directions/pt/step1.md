# Direções de Canal (Channel Directions)

O problema a ser resolvido neste laboratório é modificar o código fornecido para garantir que os canais usados como parâmetros de função sejam especificados para apenas enviar ou receber valores.

- Conhecimento básico de Golang
- Compreensão de canais e seu uso em Golang

```sh
$ go run channel-directions.go
passed message
```

A seguir, o código completo:

```go
// Ao usar canais como parâmetros de função, você pode
// especificar se um canal é destinado apenas a enviar ou receber
// valores. Essa especificidade aumenta a segurança de tipo (type-safety) do
// programa.

package main

import "fmt"

// Esta função `ping` aceita apenas um canal para enviar
// valores. Seria um erro de compilação tentar
// receber neste canal.
func ping(pings chan<- string, msg string) {
	pings <- msg
}

// A função `pong` aceita um canal para receber
// (`pings`) e um segundo para enviar (`pongs`).
func pong(pings <-chan string, pongs chan<- string) {
	msg := <-pings
	pongs <- msg
}

func main() {
	pings := make(chan string, 1)
	pongs := make(chan string, 1)
	ping(pings, "passed message")
	pong(pings, pongs)
	fmt.Println(<-pongs)
}
```
