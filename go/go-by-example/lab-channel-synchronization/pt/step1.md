# Sincronização de Canais (Channel Synchronization)

O problema a ser resolvido neste laboratório é criar uma goroutine que realiza algum trabalho e notifica outra goroutine quando ele termina, usando um canal (channel).

Para completar este laboratório, você precisará:

- Criar uma função chamada `worker` que recebe um canal do tipo `bool` como parâmetro.
- Dentro da função `worker`, realizar algum trabalho e, em seguida, enviar um valor para o canal para notificar que o trabalho foi concluído.
- Na função `main`, criar um canal do tipo `bool` com um tamanho de buffer de 1.
- Iniciar uma goroutine que chama a função `worker` e passa o canal como parâmetro.
- Bloquear a função `main` até que um valor seja recebido do canal.

```sh
$ go run channel-synchronization.go
working...done

# Se você remover a linha `<- done` deste programa, o
# programa sairá antes mesmo do `worker` ter
# começado.
```

A seguir, o código completo:

```go
// Podemos usar canais para sincronizar a execução
// entre goroutines. Aqui está um exemplo de como usar uma
// recepção bloqueante para esperar que uma goroutine termine.
// Ao esperar que várias goroutines terminem,
// você pode preferir usar um [WaitGroup](waitgroups).

package main

import (
	"fmt"
	"time"
)

// Esta é a função que executaremos em uma goroutine. O
// canal `done` será usado para notificar outra
// goroutine que o trabalho desta função foi concluído.
func worker(done chan bool) {
	fmt.Print("working...")
	time.Sleep(time.Second)
	fmt.Println("done")

	// Enviar um valor para notificar que terminamos.
	done <- true
}

func main() {

	// Iniciar uma goroutine worker, dando a ela o canal para
	// notificar.
	done := make(chan bool, 1)
	go worker(done)

	// Bloquear até recebermos uma notificação do
	// worker no canal.
	<-done
}
```
