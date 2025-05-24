# Goroutines com Estado

Na programação concorrente, é essencial sincronizar o acesso ao estado compartilhado para evitar condições de corrida (race conditions) e corrupção de dados. Este laboratório apresenta um cenário onde uma única goroutine possui o estado, e outras goroutines enviam mensagens para ler ou escrever o estado.

- Use canais (channels) para emitir pedidos de leitura e escrita para a goroutine que possui o estado.
- Use as structs `readOp` e `writeOp` para encapsular pedidos e respostas.
- Use um mapa (map) para armazenar o estado.
- Use canais `resp` para indicar sucesso e retornar valores.
- Use o pacote `atomic` para contar operações de leitura e escrita.
- Use o pacote `time` para adicionar um atraso entre as operações.

```sh
# Executar nosso programa mostra que o exemplo de gerenciamento
# de estado baseado em goroutine completa cerca de 80.000
# operações no total.
$ go run stateful-goroutines.go
readOps: 71708
writeOps: 7177

# Para este caso particular, a abordagem baseada em goroutine
# foi um pouco mais complexa do que a baseada em mutex.
# No entanto, pode ser útil em certos casos, por exemplo,
# onde você tem outros canais envolvidos ou quando gerenciar
# vários mutexes seria propenso a erros. Você deve
# usar a abordagem que parecer mais natural, especialmente
# em relação à compreensão da correção do seu
# programa.
```

A seguir, o código completo:

```go
// No exemplo anterior, usamos bloqueio explícito com
// [mutexes](mutexes) para sincronizar o acesso ao estado compartilhado
// entre várias goroutines. Outra opção é usar os
// recursos de sincronização embutidos de goroutines e
// canais para obter o mesmo resultado. Esta abordagem baseada em canal
// alinha-se com as ideias do Go de compartilhar memória por
// comunicação e ter cada pedaço de dados pertencente
// a exatamente 1 goroutine.

package main

import (
	"fmt"
	"math/rand"
	"sync/atomic"
	"time"
)

// Neste exemplo, nosso estado será de propriedade de uma única
// goroutine. Isso garantirá que os dados nunca sejam
// corrompidos com acesso concorrente. Para ler ou
// escrever esse estado, outras goroutines enviarão mensagens
// para a goroutine proprietária e receberão as
// respostas correspondentes. Estas `readOp` e `writeOp` `struct`s
// encapsulam esses pedidos e uma maneira para o proprietário
// goroutine responder.
type readOp struct {
	key  int
	resp chan int
}
type writeOp struct {
	key  int
	val  int
	resp chan bool
}

func main() {

	// Como antes, contaremos quantas operações realizamos.
	var readOps uint64
	var writeOps uint64

	// Os canais `reads` e `writes` serão usados por
	// outras goroutines para emitir pedidos de leitura e escrita,
	// respectivamente.
	reads := make(chan readOp)
	writes := make(chan writeOp)

	// Aqui está a goroutine que possui o `state`, que
	// é um mapa como no exemplo anterior, mas agora privado
	// para a goroutine com estado. Esta goroutine repetidamente
	// seleciona nos canais `reads` e `writes`,
	// respondendo aos pedidos à medida que chegam. Uma resposta
	// é executada primeiro realizando o solicitado
	// operação e, em seguida, enviando um valor no canal de resposta
	// `resp` para indicar sucesso (e o desejado
	// valor no caso de `reads`).
	go func() {
		var state = make(map[int]int)
		for {
			select {
			case read := <-reads:
				read.resp <- state[read.key]
			case write := <-writes:
				state[write.key] = write.val
				write.resp <- true
			}
		}
	}()

	// Isso inicia 100 goroutines para emitir leituras para o
	// goroutine proprietário do estado via o canal `reads`.
	// Cada leitura requer a construção de um `readOp`, enviando
	// ele sobre o canal `reads` e, em seguida, recebendo o
	// resultado sobre o canal `resp` fornecido.
	for r := 0; r < 100; r++ {
		go func() {
			for {
				read := readOp{
					key:  rand.Intn(5),
					resp: make(chan int)}
				reads <- read
				<-read.resp
				atomic.AddUint64(&readOps, 1)
				time.Sleep(time.Millisecond)
			}
		}()
	}

	// Também iniciamos 10 escritas, usando uma abordagem
	// semelhante.
	for w := 0; w < 10; w++ {
		go func() {
			for {
				write := writeOp{
					key:  rand.Intn(5),
					val:  rand.Intn(100),
					resp: make(chan bool)}
				writes <- write
				<-write.resp
				atomic.AddUint64(&writeOps, 1)
				time.Sleep(time.Millisecond)
			}
		}()
	}

	// Deixe as goroutines trabalharem por um segundo.
	time.Sleep(time.Second)

	// Finalmente, capture e relate as contagens de operações.
	readOpsFinal := atomic.LoadUint64(&readOps)
	fmt.Println("readOps:", readOpsFinal)
	writeOpsFinal := atomic.LoadUint64(&writeOps)
	fmt.Println("writeOps:", writeOpsFinal)
}
```
