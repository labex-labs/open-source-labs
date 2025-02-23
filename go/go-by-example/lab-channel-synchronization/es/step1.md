# Sincronización de canales

El problema que se debe resolver en este laboratorio es crear una goroutine que realice alguna tarea y notifique a otra goroutine cuando haya terminado, utilizando un canal.

Para completar este laboratorio, deberá:

- Crear una función llamada `worker` que tome un canal de tipo `bool` como parámetro.
- Dentro de la función `worker`, realizar alguna tarea y luego enviar un valor al canal para notificar que la tarea ha terminado.
- En la función `main`, crear un canal de tipo `bool` con un tamaño de búfer de 1.
- Iniciar una goroutine que llame a la función `worker` y pase el canal como parámetro.
- Bloquear la función `main` hasta que se reciba un valor del canal.

```sh
$ go run channel-synchronization.go
working...done

# Si eliminó la línea `<- done` de este programa, el
# programa se cerraría antes de que la `worker` incluso
# comenzara.
```

A continuación está el código completo:

```go
// Podemos utilizar canales para sincronizar la ejecución
// entre goroutines. Aquí hay un ejemplo de uso de una
// recepción bloqueante para esperar a que una goroutine
// termine. Cuando se espera a que múltiples goroutines
// terminen, es posible que prefiera utilizar un [WaitGroup](waitgroups).

package main

import (
	"fmt"
	"time"
)

// Esta es la función que ejecutaremos en una goroutine. El
// canal `done` se utilizará para notificar a otra
// goroutine que la tarea de esta función ha terminado.
func worker(done chan bool) {
	fmt.Print("working...")
	time.Sleep(time.Second)
	fmt.Println("done")

	// Envía un valor para notificar que hemos terminado.
	done <- true
}

func main() {

	// Inicia una goroutine de trabajador, pasándole el canal para
	// notificar.
	done := make(chan bool, 1)
	go worker(done)

	// Bloquea hasta que recibamos una notificación del
	// trabajador en el canal.
	<-done
}

```
