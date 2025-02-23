# Formato y análisis de fechas

El problema consiste en formatear y analizar fechas en Golang utilizando los diseños proporcionados.

- Utilice el paquete `time` para formatear y analizar fechas.
- Utilice el diseño `time.RFC3339` para formatear y analizar fechas.
- Utilice la fecha de referencia `Mon Jan 2 15:04:05 MST 2006` para mostrar el patrón con el que se debe formatear/análizar una fecha/cadena dada.
- Utilice la función `Parse` para analizar fechas.
- Utilice la función `Format` para formatear fechas.
- Utilice la función `fmt.Println` para imprimir la fecha formateada.
- Utilice la función `fmt.Printf` para imprimir la fecha formateada con los componentes extraídos.

```sh
$ go run time-formatting-parsing.go
2014-04-15T18:00:15-07:00
2012-11-01 22:08:41 +0000 +0000
6:00PM
Tue Apr 15 18:00:15 2014
2014-04-15T18:00:15.161182-07:00
0000-01-01 20:41:00 +0000 UTC
2014-04-15T18:00:15-00:00
parsing time "8:41PM" as "Mon Jan _2 15:04:05 2006":...
```

A continuación se muestra el código completo:

```go
// Go admite el formateo y el análisis de fechas a través de
// diseños basados en patrones.

package main

import (
	"fmt"
	"time"
)

func main() {
	p := fmt.Println

	// Aquí hay un ejemplo básico de formateo de una fecha
	// de acuerdo con RFC3339, utilizando la constante de diseño
	// correspondiente.
	t := time.Now()
	p(t.Format(time.RFC3339))

	// El análisis de fechas utiliza los mismos valores de diseño que `Format`.
	t1, e := time.Parse(
		time.RFC3339,
		"2012-11-01T22:08:41+00:00")
	p(t1)

	// `Format` y `Parse` utilizan diseños basados en ejemplos. Por lo general
	// se utilizará una constante de `time` para estos diseños, pero
	// también se puede proporcionar diseños personalizados. Los diseños deben utilizar la
	// fecha de referencia `Mon Jan 2 15:04:05 MST 2006` para mostrar el
	// patrón con el que se debe formatear/análizar una fecha/cadena dada.
	// La fecha de ejemplo debe ser exactamente como se muestra: el año 2006,
	// 15 para la hora, lunes para el día de la semana, etc.
	p(t.Format("3:04PM"))
	p(t.Format("Mon Jan _2 15:04:05 2006"))
	p(t.Format("2006-01-02T15:04:05.999999-07:00"))
	form := "3 04 PM"
	t2, e := time.Parse(form, "8 41 PM")
	p(t2)

	// Para representaciones puramente numéricas también se puede
	// utilizar el formateo de cadenas estándar con los
	// componentes extraídos del valor de la fecha.
	fmt.Printf("%d-%02d-%02dT%02d:%02d:%02d-00:00\n",
		t.Year(), t.Month(), t.Day(),
		t.Hour(), t.Minute(), t.Second())

	// `Parse` devolverá un error en caso de entrada con formato incorrecto
	// explicando el problema de análisis.
	ansic := "Mon Jan _2 15:04:05 2006"
	_, e = time.Parse(ansic, "8:41PM")
	p(e)
}

```
