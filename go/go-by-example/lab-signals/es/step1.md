# Señales

En algunos casos, queremos que nuestros programas Go manejen inteligentemente las señales Unix. Por ejemplo, podríamos querer que un servidor se detenga de manera elegante cuando recibe un `SIGTERM`, o que una herramienta de línea de comandos deje de procesar la entrada si recibe un `SIGINT`.

- Crea un canal bufferizado para recibir notificaciones de `os.Signal`.
- Registra el canal para recibir notificaciones de señales específicas usando `signal.Notify`.
- Crea una goroutine para ejecutar una recepción bloqueante de señales.
- Imprime la señal recibida y notifica al programa que puede finalizar.
- Espera la señal esperada y luego sale.

```sh
# Cuando ejecutamos este programa, se bloqueará esperando una
# señal. Al presionar `ctrl-C` (que la terminal muestra como `^C`),
# podemos enviar una señal `SIGINT`, lo que hará que el programa
# imprima `interrupt` y luego salga.
$ go run signals.go
awaiting signal
^C
interrupt
exiting
```

A continuación está el código completo:

```go
// A veces queremos que nuestros programas Go maneen inteligentemente
// [señales Unix](https://en.wikipedia.org/wiki/Unix_signal).
// Por ejemplo, podríamos querer que un servidor se detenga de manera
// elegante cuando recibe un `SIGTERM`, o que una herramienta de línea
// de comandos deje de procesar la entrada si recibe un `SIGINT`.
// Aquí está cómo manejar señales en Go con canales.

package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
)

func main() {

	// La notificación de señales de Go funciona enviando valores de
	// `os.Signal` en un canal. Crearemos un canal para recibir
	// estas notificaciones. Tenga en cuenta que este canal debe
	// ser bufferizado.
	sigs := make(chan os.Signal, 1)

	// `signal.Notify` registra el canal dado para recibir
	// notificaciones de las señales especificadas.
	signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM)

	// Podríamos recibir de `sigs` aquí en la función principal,
	// pero veamos cómo también se podría hacer en una goroutine
	// separada, para demostrar un escenario más realista de
	// apagado elegante.
	done := make(chan bool, 1)

	go func() {
		// Esta goroutine ejecuta una recepción bloqueante de
		// señales. Cuando recibe una, la imprimirá y luego
		// notificará al programa que puede finalizar.
		sig := <-sigs
		fmt.Println()
		fmt.Println(sig)
		done <- true
	}()

	// El programa esperará aquí hasta que reciba la
	// señal esperada (como se indica por la goroutine
	// anterior enviando un valor en `done`) y luego saldrá.
	fmt.Println("awaiting signal")
	<-done
	fmt.Println("exiting")
}

```
