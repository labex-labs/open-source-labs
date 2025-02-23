# Limitación de velocidad

El problema consiste en limitar el procesamiento de solicitudes entrantes para mantener la calidad del servicio y controlar la utilización de recursos.

- Lenguaje de programación Go
- Conocimiento básico de gorutinas, canales y temporizadores

```sh
# Al ejecutar nuestro programa, vemos que el primer lote de solicitudes
# se procesa una vez cada ~200 milisegundos, como se esperaba.
$ go run rate-limiting.go
solicitud 1 2012-10-19 00:38:18.687438 +0000 UTC
solicitud 2 2012-10-19 00:38:18.887471 +0000 UTC
solicitud 3 2012-10-19 00:38:19.087238 +0000 UTC
solicitud 4 2012-10-19 00:38:19.287338 +0000 UTC
solicitud 5 2012-10-19 00:38:19.487331 +0000 UTC

# Para el segundo lote de solicitudes, atendemos las primeras
# 3 inmediatamente debido a la limitación de velocidad con ráfaga,
# luego atendemos las 2 restantes con retrasos de ~200 ms cada una.
solicitud 1 2012-10-19 00:38:20.487578 +0000 UTC
solicitud 2 2012-10-19 00:38:20.487645 +0000 UTC
solicitud 3 2012-10-19 00:38:20.487676 +0000 UTC
solicitud 4 2012-10-19 00:38:20.687483 +0000 UTC
solicitud 5 2012-10-19 00:38:20.887542 +0000 UTC
```

A continuación se muestra el código completo:

```go
// La [_limitación de velocidad_](https://en.wikipedia.org/wiki/Rate_limiting)
// es un mecanismo importante para controlar la utilización de recursos
// y mantener la calidad del servicio. Go admite elegantemente la limitación
// de velocidad con gorutinas, canales y [temporizadores](tickers).

package main

import (
	"fmt"
	"time"
)

func main() {

	// Primero veremos la limitación de velocidad básica. Supongamos
	// que queremos limitar nuestro procesamiento de solicitudes entrantes.
	// Atenderemos estas solicitudes a partir de un canal con el
	// mismo nombre.
	solicitudes := make(chan int, 5)
	for i := 1; i <= 5; i++ {
		solicitudes <- i
	}
	close(solicitudes)

	// Este canal `limitador` recibirá un valor cada 200 milisegundos.
	// Este es el regulador en nuestro esquema de limitación de velocidad.
	limitador := time.Tick(200 * time.Millisecond)

	// Al bloquear la recepción del canal `limitador` antes de atender
	// cada solicitud, nos limitamos a 1 solicitud cada 200 milisegundos.
	for req := range solicitudes {
		<-limitador
		fmt.Println("solicitud", req, time.Now())
	}

	// Es posible que queramos permitir ráfagas cortas de solicitudes
	// en nuestro esquema de limitación de velocidad mientras se
	// conserva la limitación de velocidad global. Esto se puede
	// lograr mediante el almacenamiento en búfer del canal limitador.
	// Este canal `limitadorRáfaga` permitirá ráfagas de hasta 3 eventos.
	limitadorRáfaga := make(chan time.Time, 3)

	// Llena el canal para representar la ráfaga permitida.
	for i := 0; i < 3; i++ {
		limitadorRáfaga <- time.Now()
	}

	// Cada 200 milisegundos intentaremos agregar un nuevo valor
	// a `limitadorRáfaga`, hasta su límite de 3.
	go func() {
		for t := range time.Tick(200 * time.Millisecond) {
			limitadorRáfaga <- t
		}
	}()

	// Ahora simula 5 solicitudes entrantes más. Las primeras
	// 3 de estas se beneficiarán de la capacidad de ráfaga de
	// `limitadorRáfaga`.
	solicitudesRáfaga := make(chan int, 5)
	for i := 1; i <= 5; i++ {
		solicitudesRáfaga <- i
	}
	close(solicitudesRáfaga)
	for req := range solicitudesRáfaga {
		<-limitadorRáfaga
		fmt.Println("solicitud", req, time.Now())
	}
}

```
