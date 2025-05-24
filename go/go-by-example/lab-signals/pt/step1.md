# Sinais

Em alguns casos, queremos que nossos programas Go lidem com sinais Unix de forma inteligente. Por exemplo, podemos querer que um servidor desligue graciosamente quando receber um `SIGTERM`, ou que uma ferramenta de linha de comando pare de processar a entrada se receber um `SIGINT`.

- Crie um canal com buffer para receber notificações `os.Signal`.
- Registre o canal para receber notificações de sinais especificados usando `signal.Notify`.
- Crie uma goroutine para executar uma recepção bloqueante para sinais.
- Imprima o sinal recebido e notifique o programa de que ele pode finalizar.
- Aguarde o sinal esperado e, em seguida, saia.

```sh
# Quando executamos este programa, ele bloqueará esperando por um
# sinal. Ao digitar `ctrl-C` (que o
# terminal mostra como `^C`), podemos enviar um sinal `SIGINT`,
# fazendo com que o programa imprima `interrupt` e, em seguida, saia.
$ go run signals.go
awaiting signal
^C
interrupt
exiting
```

Aqui está o código completo:

```go
// Às vezes, gostaríamos que nossos programas Go lidassem de forma inteligente com
// [sinais Unix](https://en.wikipedia.org/wiki/Unix_signal).
// Por exemplo, podemos querer que um servidor desligue graciosamente
// quando receber um `SIGTERM`, ou que uma ferramenta de linha de comando
// pare de processar a entrada se receber um `SIGINT`.
// Veja como lidar com sinais em Go com canais.

package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
)

func main() {

	// A notificação de sinal Go funciona enviando valores `os.Signal`
	// em um canal. Criaremos um canal para
	// receber essas notificações. Observe que este canal
	// deve ser com buffer.
	sigs := make(chan os.Signal, 1)

	// `signal.Notify` registra o canal fornecido para
	// receber notificações dos sinais especificados.
	signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM)

	// Poderíamos receber de `sigs` aqui na função principal,
	// mas vamos ver como isso também pode ser
	// feito em uma goroutine separada, para demonstrar
	// um cenário mais realista de desligamento gracioso.
	done := make(chan bool, 1)

	go func() {
		// Esta goroutine executa uma recepção bloqueante para
		// sinais. Quando recebe um, ele o imprimirá
		// e, em seguida, notificará o programa de que ele pode finalizar.
		sig := <-sigs
		fmt.Println()
		fmt.Println(sig)
		done <- true
	}()

	// O programa esperará aqui até receber o
	// sinal esperado (conforme indicado pela goroutine
	// acima enviando um valor em `done`) e, em seguida, sairá.
	fmt.Println("awaiting signal")
	<-done
	fmt.Println("exiting")
}
```
