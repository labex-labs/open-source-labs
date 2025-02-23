# Operaciones no bloqueantes de canales

El problema que se debe resolver en este desafío es implementar operaciones no bloqueantes de canales utilizando la instrucción `select` con una cláusula `default`.

## Requisitos

- Implementar una recepción no bloqueante en un canal utilizando la instrucción `select` con una cláusula `default`.
- Implementar un envío no bloqueante en un canal utilizando la instrucción `select` con una cláusula `default`.
- Implementar una selección multi-vía no bloqueante utilizando la instrucción `select` con múltiples cláusulas `case` y una cláusula `default`.

## Ejemplo

```sh
$ go run non-blocking-channel-operations.go
no message received
no message sent
no activity
```
