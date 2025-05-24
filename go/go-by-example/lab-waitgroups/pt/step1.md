# waitgroups

O problema a ser resolvido neste laboratório é lançar várias goroutines e incrementar o contador do WaitGroup para cada uma. Em seguida, precisamos aguardar a conclusão de todas as goroutines lançadas.

- Conhecimento básico de Golang.
- Compreensão de concorrência em Golang.
- Familiaridade com o pacote `sync`.

```sh
$ go run waitgroups.go
Worker 5 starting
Worker 3 starting
Worker 4 starting
Worker 1 starting
Worker 2 starting
Worker 4 done
Worker 1 done
Worker 2 done
Worker 5 done
Worker 3 done

# A ordem de início e término dos workers
# provavelmente será diferente a cada invocação.
```

A seguir, o código completo:

```go
// Para aguardar a conclusão de múltiplas goroutines, podemos
// usar um *wait group*.

package main

import (
	"fmt"
	"sync"
	"time"
)

// Esta é a função que executaremos em cada goroutine.
func worker(id int) {
	fmt.Printf("Worker %d starting\n", id)

	// Dormir para simular uma tarefa dispendiosa.
	time.Sleep(time.Second)
	fmt.Printf("Worker %d done\n", id)
}

func main() {

	// Este WaitGroup é usado para aguardar a conclusão de todas as
	// goroutines lançadas aqui. Observação: se um WaitGroup for
	// explicitamente passado para funções, isso deve ser feito *por ponteiro*.
	var wg sync.WaitGroup

	// Lançar várias goroutines e incrementar o WaitGroup
	// contador para cada uma.
	for i := 1; i <= 5; i++ {
		wg.Add(1)
		// Evitar a reutilização do mesmo valor `i` em cada closure de goroutine.
		// Veja [a FAQ](https://golang.org/doc/faq#closures_and_goroutines)
		// para mais detalhes.
		i := i

		// Envolver a chamada do worker em uma closure que garante informar
		// ao WaitGroup que este worker terminou. Desta forma, o worker
		// em si não precisa estar ciente das primitivas de concorrência
		// envolvidas em sua execução.
		go func() {
			defer wg.Done()
			worker(i)
		}()
	}

	// Bloquear até que o contador do WaitGroup volte a 0;
	// todos os workers notificaram que terminaram.
	wg.Wait()

	// Observe que esta abordagem não tem uma maneira direta
	// de propagar erros dos workers. Para casos de uso mais
	// avançados, considere usar o
	// [pacote errgroup](https://pkg.go.dev/golang.org/x/sync/errgroup).
}
```
