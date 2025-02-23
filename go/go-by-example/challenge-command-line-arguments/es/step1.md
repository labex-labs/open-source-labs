# Argumentos de línea de comandos

El programa actualmente imprime los argumentos de línea de comandos brutos que se le pasan. Sin embargo, se debe modificar para imprimir argumentos específicos según su índice.

## Requisitos

- Conocimientos básicos de Golang
- Familiaridad con los argumentos de línea de comandos

## Ejemplo

```sh
# Para experimentar con los argumentos de línea de comandos es mejor
# compilar un binario con `go build` primero.
$ go build command-line-arguments.go
$./command-line-arguments a b c d
[./command-line-arguments a b c d]
[a b c d]
c

# A continuación, veremos un procesamiento de línea de comandos más avanzado
# con flags.
```
