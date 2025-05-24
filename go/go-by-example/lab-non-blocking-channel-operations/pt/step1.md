# Operações de Canal Não Bloqueantes

O problema a ser resolvido neste laboratório é implementar operações de canal não bloqueantes usando a instrução `select` com uma cláusula `default`.

- Implementar um recebimento (receive) não bloqueante em um canal usando a instrução `select` com uma cláusula `default`.
- Implementar um envio (send) não bloqueante em um canal usando a instrução `select` com uma cláusula `default`.
- Implementar uma seleção (select) multi-vias não bloqueante usando a instrução `select` com múltiplas cláusulas `case` e uma cláusula `default`.

```sh
$ go run non-blocking-channel-operations.go
no message received
no message sent
no activity
```

A seguir, o código completo:

```go
// Envios (sends) e recebimentos (receives) básicos em canais são bloqueantes.
// No entanto, podemos usar `select` com uma cláusula `default` para
// implementar envios (sends), recebimentos (receives) e até mesmo
// `select`s multi-vias _não bloqueantes_.

package main

import "fmt"

func main() {
	messages := make(chan string)
	signals := make(chan bool)

	// Aqui está um recebimento (receive) não bloqueante. Se um valor estiver
	// disponível em `messages`, então `select` tomará
	// o `<-messages` `case` com esse valor. Se não,
	// ele imediatamente tomará o `default` case.
	select {
	case msg := <-messages:
		fmt.Println("received message", msg)
	default:
		fmt.Println("no message received")
	}

	// Um envio (send) não bloqueante funciona de forma semelhante. Aqui `msg`
	// não pode ser enviado para o canal `messages`, porque
	// o canal não tem buffer e não há receptor.
	// Portanto, o `default` case é selecionado.
	msg := "hi"
	select {
	case messages <- msg:
		fmt.Println("sent message", msg)
	default:
		fmt.Println("no message sent")
	}

	// Podemos usar múltiplos `case`s acima do `default`
	// clause para implementar um `select` multi-vias não bloqueante.
	// Aqui tentamos recebimentos (receives) não bloqueantes
	// em `messages` e `signals`.
	select {
	case msg := <-messages:
		fmt.Println("received message", msg)
	case sig := <-signals:
		fmt.Println("received signal", sig)
	default:
		fmt.Println("no activity")
	}
}
```
