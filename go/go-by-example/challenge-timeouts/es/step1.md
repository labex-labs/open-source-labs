# Timeouts

Cuando los programas se conectan a recursos externos o necesitan limitar el tiempo de ejecución, los timeouts son importantes. El desafío es implementar timeouts en Go utilizando canales y `select`.

## Requisitos

- Implementar timeouts en Go utilizando canales y `select`.
- Utilizar un canal con búfer para evitar fugas de goroutine en caso de que el canal nunca sea leído.
- Utilizar `time.After` para esperar a que se envíe un valor después del timeout.
- Utilizar `select` para continuar con la primera recepción lista.

## Ejemplo

```sh
# Ejecutar este programa muestra que la primera operación
# agota el tiempo y la segunda tiene éxito.
$ go run timeouts.go
timeout 1
result 2
```
