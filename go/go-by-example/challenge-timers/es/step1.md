# Temporizadores

El desafío requiere la implementación de un temporizador que espere una duración especificada y luego active. Además, el temporizador debe ser anulable antes de activarse.

## Requisitos

- El paquete `time` debe ser importado.
- Dos temporizadores deben ser creados, uno que espere 2 segundos y otro que espere 1 segundo.
- El primer temporizador debe imprimir "Timer 1 fired" cuando se active.
- El segundo temporizador debe imprimir "Timer 2 fired" cuando se active.
- El segundo temporizador debe ser cancelado antes de activarse.
- El programa debe esperar 2 segundos para mostrar que el segundo temporizador no se activó.

## Ejemplo

```sh
// El primer temporizador se activará ~2s después de que
// iniciemos el programa, pero el segundo debe detenerse antes
// de tener la oportunidad de activarse.
$ go run timers.go
Timer 1 fired
Timer 2 stopped
```
