# Contadores Atômicos

O problema é incrementar um contador exatamente 1000 vezes usando 50 goroutines e o pacote `sync/atomic`.

- Use o pacote `sync/atomic` para incrementar o contador.
- Use um `WaitGroup` para esperar que todas as goroutines terminem seu trabalho.

```sh
# Esperamos obter exatamente 50.000 operações. Se tivéssemos
# usado o `ops++` não atômico para incrementar o contador,
# provavelmente obteríamos um número diferente, mudando entre
# as execuções, porque as goroutines interfeririam
# umas com as outras. Além disso, obteríamos falhas de data race
# ao executar com a flag `-race`.
$ go run atomic-counters.go
ops: 50000

# Em seguida, veremos mutexes, outra ferramenta para gerenciar
# estado.
```

Aqui está o código completo:

```go
// O principal mecanismo para gerenciar o estado em Go é
// a comunicação por meio de canais. Vimos isso, por exemplo,
// com [pools de trabalhadores](worker-pools). Existem algumas outras
// opções para gerenciar o estado, no entanto. Aqui, vamos
// analisar o uso do pacote `sync/atomic` para _contadores
// atômicos_ acessados por múltiplas goroutines.

package main

import (
	"fmt"
	"sync"
	"sync/atomic"
)

func main() {

	// Usaremos um inteiro sem sinal para representar nosso
	// contador (sempre positivo).
	var ops uint64

	// Um WaitGroup nos ajudará a esperar que todas as goroutines
	// terminem seu trabalho.
	var wg sync.WaitGroup

	// Iniciaremos 50 goroutines que cada uma incrementa o
	// contador exatamente 1000 vezes.
	for i := 0; i < 50; i++ {
		wg.Add(1)

		go func() {
			for c := 0; c < 1000; c++ {
				// Para incrementar atomicamente o contador, nós
				// usamos `AddUint64`, dando a ele o endereço de memória
				// do nosso contador `ops` com a sintaxe `&`.
				atomic.AddUint64(&ops, 1)
			}
			wg.Done()
		}()
	}

	// Espere até que todas as goroutines terminem.
	wg.Wait()

	// É seguro acessar `ops` agora porque sabemos
	// que nenhuma outra goroutine está escrevendo nele. Lendo
	// atômicos com segurança enquanto eles estão sendo atualizados é
	// também possível, usando funções como
	// `atomic.LoadUint64`.
	fmt.Println("ops:", ops)
}
```
