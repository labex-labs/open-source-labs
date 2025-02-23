# Gorutinas con Estado

En la programación concurrente, es esencial sincronizar el acceso al estado compartido para evitar condiciones de carrera y corrupción de datos. Este laboratorio presenta un escenario en el que una sola gorutina posee el estado y otras gorutinas envían mensajes para leer o escribir el estado.

- Utilice canales para emitir solicitudes de lectura y escritura a la gorutina que posee el estado.
- Utilice los structs `readOp` y `writeOp` para encapsular solicitudes y respuestas.
- Utilice un mapa para almacenar el estado.
- Utilice canales `resp` para indicar éxito y devolver valores.
- Utilice el paquete `atomic` para contar operaciones de lectura y escritura.
- Utilice el paquete `time` para agregar un retraso entre operaciones.

```sh
# Ejecutar nuestro programa muestra que el ejemplo de
# administración de estado basado en gorutinas completa
# aproximadamente 80.000 operaciones en total.
$ go run stateful-goroutines.go
readOps: 71708
writeOps: 7177

# En este caso particular, el enfoque basado en gorutinas
# fue un poco más complejo que el basado en mutex.
# Puede ser útil en ciertos casos, por ejemplo, donde
# haya otros canales involucrados o cuando la gestión
# de múltiples mutexes sea propensa a errores. Debe
# utilizar el enfoque que sea más natural para usted,
# especialmente con respecto a la comprensión de la
# corrección de su programa.
```

A continuación está el código completo:

```go
// En el ejemplo anterior utilizamos un bloqueo explícito con
// [mutexes](mutexes) para sincronizar el acceso al estado
// compartido entre múltiples gorutinas. Otra opción es
// utilizar las características de sincronización integradas
// de las gorutinas y los canales para obtener el mismo
// resultado. Este enfoque basado en canales está en
// línea con las ideas de Go de compartir memoria
// comunicándose y que cada pieza de datos sea propiedad
// de exactamente 1 gorutina.

package main

import (
	"fmt"
	"math/rand"
	"sync/atomic"
	"time"
)

// En este ejemplo, nuestro estado será propiedad de una
// sola gorutina. Esto garantizará que los datos nunca se
// corrompan con el acceso concurrente. Para leer o
// escribir ese estado, otras gorutinas enviarán mensajes
// a la gorutina propietaria y recibirán respuestas
// correspondientes. Estos structs `readOp` y `writeOp`
// encapsulan esas solicitudes y una forma para que la
// gorutina propietaria responda.
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

	// Como antes, contaremos cuántas operaciones
	// realizamos.
	var readOps uint64
	var writeOps uint64

	// Los canales `reads` y `writes` serán utilizados por
	// otras gorutinas para emitir solicitudes de lectura y
	// escritura, respectivamente.
	reads := make(chan readOp)
	writes := make(chan writeOp)

	// Aquí está la gorutina que posee el `estado`, que es
	// un mapa como en el ejemplo anterior pero ahora
	// privado a la gorutina con estado. Esta gorutina
	// selecciona repetidamente en los canales `reads` y
	// `writes`, respondiendo a las solicitudes a medida
	// que llegan. Una respuesta se ejecuta primero
	// realizando la operación solicitada y luego enviando
	// un valor en el canal de respuesta `resp` para
	// indicar éxito (y el valor deseado en el caso de
	// `reads`).
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

	// Esto inicia 100 gorutinas para emitir lecturas a la
	// gorutina que posee el estado a través del canal
	// `reads`. Cada lectura requiere construir un `readOp`,
	// enviarlo a través del canal `reads` y luego recibir
	// el resultado a través del canal `resp` proporcionado.
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

	// También iniciamos 10 escrituras, utilizando un
	// enfoque similar.
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

	// Deje que las gorutinas trabajen durante un segundo.
	time.Sleep(time.Second)

	// Finalmente, capture y reporte los conteos de
	// operaciones.
	readOpsFinal := atomic.LoadUint64(&readOps)
	fmt.Println("readOps:", readOpsFinal)
	writeOpsFinal := atomic.LoadUint64(&writeOps)
	fmt.Println("writeOps:", writeOpsFinal)
}

```
