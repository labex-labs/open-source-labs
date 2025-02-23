# Tiempo

El código siguiente contiene ejemplos de cómo trabajar con el tiempo y la duración en Go. Sin embargo, algunas partes del código están faltando. Su tarea es completar el código para que funcione como se espera.

- Conocimientos básicos del lenguaje de programación Go.
- Familiaridad con el soporte de Go para el tiempo y la duración.

```sh
$ go run time.go
2012-10-31 15:50:13.793654 +0000 UTC
2009-11-17 20:34:58.651387237 +0000 UTC
2009
November
17
20
34
58
651387237
UTC
Tuesday
true
false
false
25891h15m15.142266763s
25891.25420618521
1.5534752523711128e+06
9.320851514226677e+07
93208515142266763
2012-10-31 15:50:13.793654 +0000 UTC
2006-12-05 01:19:43.509120474 +0000 UTC

# A continuación, veremos la idea relacionada del tiempo
# en relación con la época Unix.
```

A continuación está el código completo:

```go
// Go ofrece un amplio soporte para tiempos y duraciones;
// aquí hay algunos ejemplos.

package main

import (
	"fmt"
	"time"
)

func main() {
	p := fmt.Println

	// Comenzaremos obteniendo la hora actual.
	ahora := time.Now()
	p(ahora)

	// Puedes construir una estructura `time` proporcionando
	// el año, mes, día, etc. Los tiempos siempre están
	// asociados con una `Location`, es decir, una zona horaria.
	entonces := time.Date(
		2009, 11, 17, 20, 34, 58, 651387237, time.UTC)
	p(entonces)

	// Puedes extraer los diversos componentes del valor de tiempo
	// como se espera.
	p(entonces.Year())
	p(entonces.Month())
	p(entonces.Day())
	p(entonces.Hour())
	p(entonces.Minute())
	p(entonces.Second())
	p(entonces.Nanosecond())
	p(entonces.Location())

	// El `Weekday` de lunes a domingo también está disponible.
	p(entonces.Weekday())

	// Estos métodos comparan dos tiempos, probando si el
	// primero ocurre antes, después o al mismo tiempo
	// que el segundo, respectivamente.
	p(entonces.Before(ahora))
	p(entonces.After(ahora))
	p(entonces.Equal(ahora))

	// El método `Sub` devuelve una `Duration` que representa
	// el intervalo entre dos tiempos.
	diferencia := ahora.Sub(entonces)
	p(diferencia)

	// Podemos calcular la duración en
	// varios unidades.
	p(diferencia.Hours())
	p(diferencia.Minutes())
	p(diferencia.Seconds())
	p(diferencia.Nanoseconds())

	// Puedes usar `Add` para avanzar un tiempo en una
	// duración dada, o con un `-` para retroceder en una
	// duración.
	p(entonces.Add(diferencia))
	p(entonces.Add(-diferencia))
}

```
