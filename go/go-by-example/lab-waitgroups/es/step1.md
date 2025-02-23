# waitgroups

El problema que se debe resolver en este laboratorio es lanzar varias goroutines e incrementar el contador del WaitGroup para cada una. Luego, debemos esperar a que terminen todas las goroutines lanzadas.

- Conocimientos básicos de Golang.
- Comprensión de la concurrencia en Golang.
- Familiaridad con el paquete `sync`.

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

# El orden en que los trabajadores se inician y terminan
# es probable que sea diferente para cada invocación.
```

A continuación está el código completo:

```go
// Para esperar a que múltiples goroutines terminen, podemos
// utilizar un *grupo de espera*.

package main

import (
	"fmt"
	"sync"
	"time"
)

// Esta es la función que ejecutaremos en cada goroutine.
func worker(id int) {
	fmt.Printf("Worker %d starting\n", id)

	// Dormir para simular una tarea costosa.
	time.Sleep(time.Second)
	fmt.Printf("Worker %d done\n", id)
}

func main() {

	// Este WaitGroup se utiliza para esperar a que todas las
	// goroutines lanzadas aquí terminen. Nota: si un WaitGroup se
	// pasa explícitamente a funciones, debe hacerse *por puntero*.
	var wg sync.WaitGroup

	// Lanzar varias goroutines e incrementar el contador del WaitGroup
	// para cada una.
	for i := 1; i <= 5; i++ {
		wg.Add(1)
		// Evitar el reuso del mismo valor de `i` en cada cierre de goroutine.
		// Consulte [la FAQ](https://golang.org/doc/faq#closures_and_goroutines)
		// para obtener más detalles.
		i := i

		// Envolver la llamada al trabajador en un cierre que se asegure de decir
		// al WaitGroup que este trabajador ha terminado. De esta manera, el trabajador
		// en sí mismo no tiene que ser consciente de los primitivos de concurrencia
		// involucrados en su ejecución.
		go func() {
			defer wg.Done()
			worker(i)
		}()
	}

	// Bloquear hasta que el contador del WaitGroup vuelva a 0;
	// todos los trabajadores notificados de que han terminado.
	wg.Wait()

	// Tenga en cuenta que este enfoque no tiene una forma directa
	// de propagar errores de los trabajadores. Para casos de uso más
	// avanzados, considere utilizar el paquete [errgroup](https://pkg.go.dev/golang.org/x/sync/errgroup).
}

```
