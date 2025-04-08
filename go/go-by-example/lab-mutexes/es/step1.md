# Mutexes

El problema que se debe resolver en este laboratorio es incrementar un contador nombrado en un bucle utilizando múltiples goroutines y asegurarse de que el acceso al contador esté sincronizado.

- Utilice una estructura `Container` para almacenar un mapa de contadores.
- Utilice un `Mutex` para sincronizar el acceso al mapa `counters`.
- La estructura `Container` debe tener un método `inc` que tome una cadena `name` e incremente el contador correspondiente en el mapa `counters`.
- El método `inc` debe bloquear el mutex antes de acceder al mapa `counters` y desbloquearlo al final de la función utilizando una declaración `defer`.
- Utilice la estructura `sync.WaitGroup` para esperar a que las goroutines terminen.
- Utilice la función `fmt.Println` para imprimir el mapa `counters`.

```sh
# Ejecutar el programa muestra que los contadores
# se actualizan como se esperaba.

# A continuación, veremos cómo implementar esta misma tarea
# de administración de estado utilizando solo goroutines y canales.
```

A continuación se muestra el código completo:

```go
// En el ejemplo anterior vimos cómo administrar un estado
// de contador simple utilizando [operaciones atómicas](atomic-counters).
// Para un estado más complejo, podemos utilizar un [_mutex_](https://en.wikipedia.org/wiki/Mutual_exclusion)
// para acceder de manera segura a datos a través de múltiples goroutines.

package main

import (
	"fmt"
	"sync"
)

// Container almacena un mapa de contadores; dado que queremos
// actualizarlo concurrentemente desde múltiples goroutines,
// agregamos un `Mutex` para sincronizar el acceso.
// Tenga en cuenta que los mutexes no deben ser copiados,
// por lo que si esta `struct` se pasa por ahí, debe hacerse
// por puntero.
type Container struct {
	mu       sync.Mutex
	counters map[string]int
}

func (c *Container) inc(name string) {
	// Bloque el mutex antes de acceder a `counters`; desbloque
	// it al final de la función utilizando una declaración [defer](defer).
	c.mu.Lock()
	defer c.mu.Unlock()
	c.counters[name]++
}

func main() {
	c := Container{
		// Tenga en cuenta que el valor cero de un mutex es usable tal cual,
		// por lo que no es necesario inicializarlo aquí.
		counters: map[string]int{"a": 0, "b": 0},
	}

	var wg sync.WaitGroup

	// Esta función incrementa un contador nombrado
	// en un bucle.
	doIncrement := func(name string, n int) {
		for i := 0; i < n; i++ {
			c.inc(name)
		}
		wg.Done()
	}

	// Ejecute varias goroutines concurrentemente; tenga en cuenta
	// que todas acceden al mismo `Container`,
	// y dos de ellas acceden al mismo contador.
	wg.Add(3)
	go doIncrement("a", 10000)
	go doIncrement("a", 10000)
	go doIncrement("b", 10000)

	// Espere a que las goroutines terminen
	wg.Wait()
	fmt.Println(c.counters)
}

```
