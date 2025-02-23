# Cerrando canales

En esta práctica, debes modificar el código dado para cerrar el canal `jobs` cuando ya no hay más trabajos para el trabajador. También debes utilizar el canal `done` para notificar cuando todos los trabajos hayan sido completados.

- Utiliza un canal con búfer `jobs` para comunicar el trabajo por hacer desde la rutina `main()` a una rutina de trabajo.
- Utiliza un canal `done` para notificar cuando todos los trabajos hayan sido completados.
- Utiliza una rutina de trabajo para recibir repetidamente de `jobs` con `j, more := <-jobs`.
- Utiliza la forma especial de recepción de 2 valores para notificar en `done` cuando todos los trabajos hayan sido completados.
- Envía 3 trabajos al trabajador a través del canal `jobs`, luego cierra el canal.
- Utiliza el enfoque de [sincronización](channel-synchronization) para esperar a la rutina de trabajo.

```sh
$ go run closing-channels.go
sent job 1
received job 1
sent job 2
received job 2
sent job 3
received job 3
sent all jobs
received all jobs

# La idea de los canales cerrados conduce naturalmente a nuestro siguiente
# ejemplo: `range` sobre canales.
```

A continuación está el código completo:

```go
// _Cerrar_ un canal indica que ya no se enviarán más valores
// sobre él. Esto puede ser útil para comunicar la finalización
// a los receptores del canal.

package main

import "fmt"

// En este ejemplo utilizaremos un canal `jobs` para
// comunicar el trabajo por hacer desde la rutina `main()`
// a una rutina de trabajo. Cuando ya no tengamos más trabajos
// para el trabajador, cerraremos el canal `jobs`.
func main() {
	jobs := make(chan int, 5)
	done := make(chan bool)

	// Aquí está la rutina de trabajo. Recibe repetidamente
	// de `jobs` con `j, more := <-jobs`. En esta
	// forma especial de recepción de 2 valores, el valor
	// `more` será `false` si `jobs` ha sido `cerrado` y todos
	// los valores en el canal ya han sido recibidos.
	// Lo utilizamos para notificar en `done` cuando hayamos
	// terminado todos nuestros trabajos.
	go func() {
		for {
			j, more := <-jobs
			if more {
				fmt.Println("received job", j)
			} else {
				fmt.Println("received all jobs")
				done <- true
				return
			}
		}
	}()

	// Esto envía 3 trabajos al trabajador a través del canal `jobs`,
	// luego cierra el canal.
	for j := 1; j <= 3; j++ {
		jobs <- j
		fmt.Println("sent job", j)
	}
	close(jobs)
	fmt.Println("sent all jobs")

	// Esperamos a la rutina de trabajo utilizando el
	// enfoque de [sincronización](channel-synchronization)
	// que vimos anteriormente.
	<-done
}

```
