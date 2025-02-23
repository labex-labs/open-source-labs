# Época

El problema que se debe resolver en este laboratorio es escribir un programa de Golang que pueda calcular el número de segundos, milisegundos o nanosegundos desde la época Unix.

Para completar este laboratorio, debes tener un conocimiento básico de Golang y cumplir con los siguientes requisitos:

- Conocimiento del paquete `time` en Golang.
- Conocimiento de cómo utilizar las funciones `Unix`, `UnixMilli` y `UnixNano` en el paquete `time`.

```sh
$ go run epoch.go
2012-10-31 16:13:58.292387 +0000 UTC
1351700038
1351700038292
1351700038292387000
2012-10-31 16:13:58 +0000 UTC
2012-10-31 16:13:58.292387 +0000 UTC

# A continuación, veremos otra tarea relacionada con la hora: la
# análisis y el formato de fechas y horas.
```

A continuación se muestra el código completo:

```go
// Una necesidad común en los programas es obtener el número
// de segundos, milisegundos o nanosegundos desde la
// [época Unix](https://en.wikipedia.org/wiki/Unix_time).
// Aquí está cómo hacerlo en Go.

package main

import (
	"fmt"
	"time"
)

func main() {

	// Utilice `time.Now` con `Unix`, `UnixMilli` o `UnixNano`
	// para obtener el tiempo transcurrido desde la época Unix en segundos,
	// milisegundos o nanosegundos, respectivamente.
	ahora := time.Now()
	fmt.Println(ahora)

	fmt.Println(ahora.Unix())
	fmt.Println(ahora.UnixMilli())
	fmt.Println(ahora.UnixNano())

	// También puede convertir segundos o nanosegundos enteros
	// desde la época en la `time` correspondiente.
	fmt.Println(time.Unix(ahora.Unix(), 0))
	fmt.Println(time.Unix(0, ahora.UnixNano()))
}

```
