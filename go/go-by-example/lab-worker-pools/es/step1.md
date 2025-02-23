# Grupos de trabajadores

Implementa un grupo de trabajadores que reciba trabajos a través del canal `jobs` y envíe los resultados correspondientes a través del canal `results`. El grupo de trabajadores debe tener múltiples instancias concurrentes, y cada trabajador debe dormir un segundo por trabajo para simular una tarea costosa.

- Utiliza goroutines y canales para implementar el grupo de trabajadores.
- El grupo de trabajadores debe tener múltiples instancias concurrentes.
- Cada trabajador debe dormir un segundo por trabajo para simular una tarea costosa.
- El grupo de trabajadores debe recibir trabajos a través del canal `jobs` y enviar los resultados correspondientes a través del canal `results`.

```sh
# Nuestro programa en ejecución muestra los 5 trabajos
# siendo ejecutados por varios trabajadores. El programa
# solo tarda aproximadamente 2 segundos a pesar de
# realizar aproximadamente 5 segundos de trabajo en
# total porque hay 3 trabajadores operando
# concurrentemente.
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

A continuación está el código completo:

```go
// En este ejemplo veremos cómo implementar
// un _grupo de trabajadores_ utilizando goroutines y canales.

package main

import (
	"fmt"
	"time"
)

// Aquí está el trabajador, del cual ejecutaremos
// varias instancias concurrentes. Estos trabajadores
// recibirán trabajos a través del canal `jobs` y
// enviarán los resultados correspondientes a
// `results`. Dormiremos un segundo por trabajo para
// simular una tarea costosa.
func worker(id int, jobs <-chan int, results chan<- int) {
	for j := range jobs {
		fmt.Println("worker", id, "started  job", j)
		time.Sleep(time.Second)
		fmt.Println("worker", id, "finished job", j)
		results <- j * 2
	}
}

func main() {

	// Para utilizar nuestro grupo de trabajadores,
	// necesitamos enviarles trabajos y recopilar
	// sus resultados. Creamos 2 canales para esto.
	const numJobs = 5
	jobs := make(chan int, numJobs)
	results := make(chan int, numJobs)

	// Esto inicia 3 trabajadores, inicialmente bloqueados
	// porque no hay trabajos todavía.
	for w := 1; w <= 3; w++ {
		go worker(w, jobs, results)
	}

	// Aquí enviamos 5 `jobs` y luego `cerramos` ese
	// canal para indicar que ese es todo el trabajo que
	// tenemos.
	for j := 1; j <= numJobs; j++ {
		jobs <- j
	}
	close(jobs)

	// Finalmente, recopilamos todos los resultados del
	// trabajo. Esto también asegura que las goroutines
	// de los trabajadores hayan terminado. Una forma
	// alternativa de esperar a múltiples goroutines es
	// utilizar un [WaitGroup](waitgroups).
	for a := 1; a <= numJobs; a++ {
		<-results
	}
}

```
