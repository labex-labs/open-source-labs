# Salida

El problema que se debe resolver en este desafío es salir de un programa de Go con un código de estado específico utilizando la función `os.Exit`.

## Requisitos

Para completar este desafío, necesitarás tener un conocimiento básico de la programación en Go y del paquete `os`.

## Ejemplo

```sh
# Si ejecutas `exit.go` usando `go run`, la salida
# será capturada por `go` y mostrada.
$ go run exit.go
estado de salida 3

# Al compilar y ejecutar un binario, puedes ver
# el estado en la terminal.
$ go build exit.go
$./exit
$ echo $?
3

# Observa que el `!` de nuestro programa nunca se imprimió.
```
