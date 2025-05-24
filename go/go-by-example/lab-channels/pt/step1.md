# Canais (Channels)

Neste laboratório, você deve criar um novo canal (channel) e enviar um valor para ele a partir de uma nova goroutine. Em seguida, você receberá o valor do canal e o imprimirá.

- Você deve usar a sintaxe `make(chan val-type)` para criar um novo canal.
- O canal deve ser tipado pelos valores que ele transmite.
- Você deve usar a sintaxe `channel <-` para enviar um valor para o canal.
- Você deve usar a sintaxe `<-channel` para receber um valor do canal.
- Você deve usar uma nova goroutine para enviar o valor para o canal.

```sh
# Quando executamos o programa, a mensagem `"ping"` é
# passada com sucesso de uma goroutine para outra via
# nosso canal.
$ go run channels.go
ping

# Por padrão, envios e recebimentos bloqueiam até que tanto o
# remetente quanto o receptor estejam prontos. Essa propriedade permitiu
# que esperássemos no final do nosso programa pela mensagem `"ping"`
# sem ter que usar qualquer outra sincronização.
```

Aqui está o código completo:

```go
// _Canais_ são os canos que conectam goroutines concorrentes.
// Você pode enviar valores para canais de uma
// goroutine e receber esses valores em outra
// goroutine.

package main

import "fmt"

func main() {

	// Crie um novo canal com `make(chan val-type)`.
	// Canais são tipados pelos valores que eles transmitem.
	messages := make(chan string)

	// _Envie_ um valor para um canal usando a sintaxe `channel <-`.
	// Aqui enviamos `"ping"` para o canal `messages`
	// que criamos acima, a partir de uma nova goroutine.
	go func() { messages <- "ping" }()

	// A sintaxe `<-channel` _recebe_ um valor do
	// canal. Aqui receberemos a mensagem `"ping"`
	// que enviamos acima e a imprimiremos.
	msg := <-messages
	fmt.Println(msg)
}
```
