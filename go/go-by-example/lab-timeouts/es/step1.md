# Tiempos de espera

Los tiempos de espera son importantes para los programas que se conectan a recursos externos o que de otra manera necesitan limitar el tiempo de ejecución. En este laboratorio, se implementarán tiempos de espera en Go utilizando canales y `select`.

- Implementar tiempos de espera en Go utilizando canales y `select`.
- Utilizar un canal con búfer para evitar fugas de gorutinas en caso de que el canal nunca se lea.
- Utilizar `time.After` para esperar a que se envíe un valor después del tiempo de espera.
- Utilizar `select` para continuar con la primera recepción lista.

```sh
# Ejecutar este programa muestra que la primera operación
# agota el tiempo y la segunda tiene éxito.
$ go run timeouts.go
timeout 1
result 2
```

A continuación, se muestra el código completo:

```go
// Los _tiempos de espera_ son importantes para los programas
// que se conectan a recursos externos o que de otra manera
// necesitan limitar el tiempo de ejecución. Implementar
// tiempos de espera en Go es fácil y elegante gracias a
// los canales y `select`.

package main

import (
	"fmt"
	"time"
)

func main() {

	// Para nuestro ejemplo, supongamos que estamos
	// ejecutando una llamada externa que devuelve su
	// resultado en un canal `c1` después de 2s. Tenga en
	// cuenta que el canal tiene búfer, por lo que el envío
	// en la gorutina no bloquea. Este es un patrón común
	// para evitar fugas de gorutinas en caso de que el
	// canal nunca se lea.
	c1 := make(chan string, 1)
	go func() {
		time.Sleep(2 * time.Second)
		c1 <- "result 1"
	}()

	// Aquí está el `select` que implementa un tiempo de
	// espera. `res := <-c1` espera el resultado y
	// `<-time.After` espera a que se envíe un valor
	// después del tiempo de espera de 1s. Dado que
	// `select` continúa con la primera recepción lista,
	// tomaremos el caso de tiempo de espera si la
	// operación tarda más de los 1s permitidos.
	select {
	case res := <-c1:
		fmt.Println(res)
	case <-time.After(1 * time.Second):
		fmt.Println("timeout 1")
	}

	// Si permitimos un tiempo de espera más largo de 3s,
	// entonces la recepción de `c2` tendrá éxito y
	// mostraremos el resultado.
	c2 := make(chan string, 1)
	go func() {
		time.Sleep(2 * time.Second)
		c2 <- "result 2"
	}()
	select {
	case res := <-c2:
		fmt.Println(res)
	case <-time.After(3 * time.Second):
		fmt.Println("timeout 2")
	}
}

```
