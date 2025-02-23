# Temporizadores

La práctica requiere la implementación de un temporizador que espere una duración especificada y luego active. Además, el temporizador debe ser anulable antes de activarse.

- Se debe importar el paquete `time`.
- Se deben crear dos temporizadores, uno que espere 2 segundos y otro que espere 1 segundo.
- El primer temporizador debe imprimir "Temporizador 1 activado" cuando se active.
- El segundo temporizador debe imprimir "Temporizador 2 activado" cuando se active.
- El segundo temporizador debe ser anulado antes de activarse.
- El programa debe esperar 2 segundos para demostrar que el segundo temporizador no se activó.

```sh
// El primer temporizador se activará ~2s después de que
// iniciemos el programa, pero el segundo debe detenerse
// antes de tener la oportunidad de activarse.
$ go run timers.go
Temporizador 1 activado
Temporizador 2 detenido
```

A continuación está el código completo:

```go
// A menudo queremos ejecutar código de Go en algún momento
// en el futuro, o repetidamente en un intervalo. Las
// características integradas de _temporizador_ y _cronómetro_
// de Go facilitan ambas tareas. Primero veremos los
// temporizadores y luego los [cronómetros](tickers).

package main

import (
	"fmt"
	"time"
)

func main() {

	// Los temporizadores representan un solo evento en el
	// futuro. Le indicas al temporizador cuánto tiempo
	// quieres esperar, y te proporciona un canal que se
	// notificará en ese momento. Este temporizador esperará
	// 2 segundos.
	timer1 := time.NewTimer(2 * time.Second)

	// El `<-timer1.C` se bloquea en el canal `C` del
	// temporizador hasta que envía un valor que indica que
	// el temporizador se activó.
	<-timer1.C
	fmt.Println("Temporizador 1 activado")

	// Si solo quisieras esperar, podrías haber usado
	// `time.Sleep`. Una razón por la que un temporizador
	// puede ser útil es que puedes cancelar el temporizador
	// antes de que se active. Aquí hay un ejemplo de eso.
	timer2 := time.NewTimer(time.Second)
	go func() {
		<-timer2.C
		fmt.Println("Temporizador 2 activado")
	}()
	stop2 := timer2.Stop()
	if stop2 {
		fmt.Println("Temporizador 2 detenido")
	}

	// Dale al `timer2` suficiente tiempo para activarse, si
	// alguna vez iba a hacerlo, para demostrar que en
	// realidad está detenido.
	time.Sleep(2 * time.Second)
}

```
