# Creación de procesos

El desafío requiere la implementación de un programa de Go que cree procesos externos y recopile su salida.

## Requisitos

- El programa debe ser capaz de crear procesos externos.
- El programa debe ser capaz de recopilar la salida de los procesos externos.
- El programa debe manejar los errores que pueden surgir durante la ejecución de los procesos externos.

## Ejemplo

```sh
# Los programas creados devuelven una salida que es la misma
# que si los hubiéramos ejecutado directamente desde la línea de comandos.
$ go run spawning-processes.go
> date
Thu 05 May 2022 10:10:12 PM PDT

# date no tiene una bandera `-x` por lo que saldrá con
# un mensaje de error y un código de retorno distinto de cero.
command exited with rc = 1
hello > grep
hello grep

-a > ls -l -h
drwxr-xr-x 4 mark 136B Oct 3 16:29.
drwxr-xr-x 91 mark 3.0K Oct 3 12:50..
-rw-r--r-- 1 mark 1.3K Oct 3 16:28 spawning-processes.go
```
