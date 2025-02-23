# Contadores atómicos

El problema consiste en incrementar un contador exactamente 1000 veces utilizando 50 goroutines y el paquete `sync/atomic`.

- Utilice el paquete `sync/atomic` para incrementar el contador.
- Utilice un WaitGroup para esperar a que todas las goroutines terminen su trabajo.

```sh
# Esperamos obtener exactamente 50.000 operaciones. Si hubiéramos
# utilizado el no atómico `ops++` para incrementar el contador,
# probablemente obtendríamos un número diferente, que variaría
# entre ejecuciones, porque las goroutines se interpondrían
# entre sí. Además, obtendríamos errores de carrera de datos
# al ejecutar con la bandera `-race`.
$ go run atomic-counters.go
ops: 50000

# A continuación veremos los mutexes, otra herramienta para
# la gestión del estado.
```

A continuación se muestra el código completo:

```go
// El principal mecanismo para la gestión del estado en Go es
// la comunicación a través de canales. Vimos esto por ejemplo
// con [piscinas de trabajadores](worker-pools). Sin embargo,
// hay otras opciones para la gestión del estado. Aquí
// veremos cómo utilizar el paquete `sync/atomic` para
// _contadores atómicos_ accedidos por múltiples goroutines.

package main

import (
	"fmt"
	"sync"
	"sync/atomic"
)

func main() {

	// Utilizaremos un entero sin signo para representar nuestro
	// contador (que siempre es positivo).
	var ops uint64

	// Un WaitGroup nos ayudará a esperar a que todas las goroutines
	// terminen su trabajo.
	var wg sync.WaitGroup

	// Iniciaremos 50 goroutines que cada una incrementará el
	// contador exactamente 1000 veces.
	for i := 0; i < 50; i++ {
		wg.Add(1)

		go func() {
			for c := 0; c < 1000; c++ {
				// Para incrementar el contador de forma atómica
				// utilizamos `AddUint64`, pasándole la dirección
				// de memoria de nuestro contador `ops` con la
				// sintaxis `&`.
				atomic.AddUint64(&ops, 1)
			}
			wg.Done()
		}()
	}

	// Espera hasta que todas las goroutines hayan terminado.
	wg.Wait()

	// Ahora es seguro acceder a `ops` porque sabemos
	// que ninguna otra goroutine está escribiendo en él.
	// También es posible leer atómicos de forma segura
	// mientras se están actualizando, utilizando funciones
	// como `atomic.LoadUint64`.
	fmt.Println("ops:", ops)
}

```
