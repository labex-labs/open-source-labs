# _Worker Pools_

Implemente um _worker pool_ que recebe trabalho no _channel_ `jobs` e envia os resultados correspondentes no _channel_ `results`. O _worker pool_ deve ter múltiplas instâncias concorrentes, e cada _worker_ deve dormir por um segundo por _job_ para simular uma tarefa dispendiosa.

- Use _goroutines_ e _channels_ para implementar o _worker pool_.
- O _worker pool_ deve ter múltiplas instâncias concorrentes.
- Cada _worker_ deve dormir por um segundo por _job_ para simular uma tarefa dispendiosa.
- O _worker pool_ deve receber trabalho no _channel_ `jobs` e enviar os resultados correspondentes no _channel_ `results`.

```sh
# Nosso programa em execução mostra os 5 jobs sendo executados por
# vários workers. O programa leva apenas cerca de 2 segundos
# apesar de fazer cerca de 5 segundos de trabalho total porque
# existem 3 workers operando concorrentemente.
$ time go run worker-pools.go
worker 1 started job 1
worker 2 started job 2
worker 3 started job 3
worker 1 finished job 1
worker 1 started job 4
worker 2 finished job 2
worker 2 started job 5
worker 3 finished job 3
worker 1 finished job 4
worker 2 finished job 5

real 0m2.358s
```

Abaixo está o código completo:

```go
// Neste exemplo, veremos como implementar
// um _worker pool_ usando goroutines e channels.

package main

import (
	"fmt"
	"time"
)

// Aqui está o worker, do qual executaremos várias
// instâncias concorrentes. Esses workers receberão
// trabalho no channel `jobs` e enviarão os
// resultados correspondentes em `results`. Dormiremos um segundo por job para
// simular uma tarefa dispendiosa.
func worker(id int, jobs <-chan int, results chan<- int) {
	for j := range jobs {
		fmt.Println("worker", id, "started  job", j)
		time.Sleep(time.Second)
		fmt.Println("worker", id, "finished job", j)
		results <- j * 2
	}
}

func main() {

	// Para usar nosso pool de workers, precisamos enviar
	// trabalho para eles e coletar seus resultados. Fazemos 2
	// channels para isso.
	const numJobs = 5
	jobs := make(chan int, numJobs)
	results := make(chan int, numJobs)

	// Isso inicia 3 workers, inicialmente bloqueados
	// porque ainda não há jobs.
	for w := 1; w <= 3; w++ {
		go worker(w, jobs, results)
	}

	// Aqui enviamos 5 `jobs` e então `close` esse
	// channel para indicar que é todo o trabalho que temos.
	for j := 1; j <= numJobs; j++ {
		jobs <- j
	}
	close(jobs)

	// Finalmente, coletamos todos os resultados do trabalho.
	// Isso também garante que as goroutines dos workers tenham
	// terminado. Uma forma alternativa de esperar por múltiplas
	// goroutines é usar um [WaitGroup](waitgroups).
	for a := 1; a <= numJobs; a++ {
		<-results
	}
}
```
