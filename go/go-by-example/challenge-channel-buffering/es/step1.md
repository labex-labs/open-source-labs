# Bufferización de canales

Por defecto, los canales en Golang no están bufferizados, lo que significa que solo aceptan envíos si hay una recepción correspondiente lista para recibir el valor enviado. Sin embargo, los canales bufferizados aceptan un número limitado de valores sin un receptor correspondiente para esos valores. En este desafío, se te pide crear un canal bufferizado y enviar valores al canal sin una recepción concurrente correspondiente.

## Requisitos

- Conocimientos básicos de los canales de Golang
- Comprensión de los canales bufferizados

## Ejemplo

```sh
$ go run channel-buffering.go
buffered
channel
```
