# Formato y análisis de fechas

El problema consiste en formatear y analizar fechas en Golang utilizando los diseños proporcionados.

## Requisitos

- Utilizar el paquete `time` para formatear y analizar fechas.
- Utilizar el diseño `time.RFC3339` para formatear y analizar fechas.
- Utilizar la fecha de referencia `Mon Jan 2 15:04:05 MST 2006` para mostrar el patrón con el que se formatea/analiza una fecha/cadena dada.
- Utilizar la función `Parse` para analizar fechas.
- Utilizar la función `Format` para formatear fechas.
- Utilizar la función `fmt.Println` para imprimir la fecha formateada.
- Utilizar la función `fmt.Printf` para imprimir la fecha formateada con los componentes extraídos.

## Ejemplo

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
