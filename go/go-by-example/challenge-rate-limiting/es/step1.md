# Limitación de Velocidad

El problema consiste en limitar el procesamiento de solicitudes entrantes para mantener la calidad del servicio y controlar el uso de recursos.

## Requisitos

- Lenguaje de programación Go
- Comprensión básica de gorutinas, canales y temporizadores

## Ejemplo

```sh
# Al ejecutar nuestro programa, vemos que la primera
# lote de solicitudes se procesa una vez cada ~200
# milisegundos, como se esperaba.
$ go run rate-limiting.go
solicitud 1 2012-10-19 00:38:18.687438 +0000 UTC
solicitud 2 2012-10-19 00:38:18.887471 +0000 UTC
solicitud 3 2012-10-19 00:38:19.087238 +0000 UTC
solicitud 4 2012-10-19 00:38:19.287338 +0000 UTC
solicitud 5 2012-10-19 00:38:19.487331 +0000 UTC

# Para el segundo lote de solicitudes, atendemos las
# primeras 3 inmediatamente debido a la limitación de
# velocidad con ráfaga, luego atendemos las 2 restantes
# con retrasos de ~200ms cada una.
solicitud 1 2012-10-19 00:38:20.487578 +0000 UTC
solicitud 2 2012-10-19 00:38:20.487645 +0000 UTC
solicitud 3 2012-10-19 00:38:20.487676 +0000 UTC
solicitud 4 2012-10-19 00:38:20.687483 +0000 UTC
solicitud 5 2012-10-19 00:38:20.887542 +0000 UTC
```
