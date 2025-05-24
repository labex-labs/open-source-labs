# Mutexes (Mutexes)

O problema a ser resolvido neste laboratório é incrementar um contador nomeado em um loop usando múltiplas goroutines, e garantir que o acesso ao contador seja sincronizado.

- Use uma struct `Container` para conter um mapa de contadores.
- Use um `Mutex` para sincronizar o acesso ao mapa `counters`.
- A struct `Container` deve ter um método `inc` que recebe uma string `name` e incrementa o contador correspondente no mapa `counters`.
- O método `inc` deve travar o mutex antes de acessar o mapa `counters` e destravá-lo no final da função usando uma declaração `defer`.
- Use a struct `sync.WaitGroup` para esperar que as goroutines terminem.
- Use a função `fmt.Println` para imprimir o mapa `counters`.

```sh
# Executar o programa mostra que os contadores
# foram atualizados como esperado.

# Em seguida, veremos como implementar esta mesma tarefa de
# gerenciamento de estado usando apenas goroutines e canais.
```

Aqui está o código completo:

```go
// No exemplo anterior, vimos como gerenciar um estado de contador simples
// usando [operações atômicas](atomic-counters).
// Para um estado mais complexo, podemos usar um [_mutex_](https://en.wikipedia.org/wiki/Mutual_exclusion)
// para acessar dados com segurança em múltiplas goroutines.

package main

import (
	"fmt"
	"sync"
)

// Container contém um mapa de contadores; como queremos
// atualizá-lo concorrentemente de múltiplas goroutines, nós
// adicionamos um `Mutex` para sincronizar o acesso.
// Observe que mutexes não devem ser copiados, então se esta
// `struct` for passada, ela deve ser feita por
// ponteiro.
type Container struct {
	mu       sync.Mutex
	counters map[string]int
}

func (c *Container) inc(name string) {
	// Trave o mutex antes de acessar `counters`; destrave-o
	// no final da função usando uma declaração [defer](defer)
	c.mu.Lock()
	defer c.mu.Unlock()
	c.counters[name]++
}

func main() {
	c := Container{
		// Observe que o valor zero de um mutex é utilizável como está, então nenhuma
		// inicialização é necessária aqui.
		counters: map[string]int{"a": 0, "b": 0},
	}

	var wg sync.WaitGroup

	// Esta função incrementa um contador nomeado
	// em um loop.
	doIncrement := func(name string, n int) {
		for i := 0; i < n; i++ {
			c.inc(name)
		}
		wg.Done()
	}

	// Execute várias goroutines concorrentemente; observe
	// que todas elas acessam o mesmo `Container`,
	// e duas delas acessam o mesmo contador.
	wg.Add(3)
	go doIncrement("a", 10000)
	go doIncrement("a", 10000)
	go doIncrement("b", 10000)

	// Espere as goroutines terminarem
	wg.Wait()
	fmt.Println(c.counters)
}

```
