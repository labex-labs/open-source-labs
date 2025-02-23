# Cronómetros y Tickers

En este desafío, debes crear un ticker que marque cada 500 ms hasta que lo detengamos. Utilizarás un canal para esperar los valores a medida que llegan.

## Requisitos

- Utiliza el paquete `time` para crear un ticker.
- Utiliza un canal para esperar los valores a medida que llegan.
- Utiliza la declaración `select` para recibir valores del canal.
- Detén el ticker después de 1600 ms.

## Ejemplo

```sh
# Cuando ejecutamos este programa, el ticker debería marcar 3 veces
# antes de detenerlo.
$ go run tickers.go
Tick at 2012-09-23 11:29:56.487625 -0700 PDT
Tick at 2012-09-23 11:29:56.988063 -0700 PDT
Tick at 2012-09-23 11:29:57.488076 -0700 PDT
Ticker stopped
```
