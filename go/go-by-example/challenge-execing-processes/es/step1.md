# Ejecución de procesos

El problema consiste en reemplazar el proceso actual de Go con otro proceso, como un proceso no escrito en Go.

## Requisitos

- Lenguaje de programación Go
- Conocimientos básicos de la función `exec` de Go
- Familiaridad con las variables de entorno

## Ejemplo

```sh
# Cuando ejecutamos nuestro programa, es reemplazado por `ls`.
$ go run execing-processes.go
total 16
drwxr-xr-x 4 mark 136B Oct 3 16:29.
drwxr-xr-x 91 mark 3.0K Oct 3 12:50..
-rw-r--r-- 1 mark 1.3K Oct 3 16:28 execing-processes.go

# Tenga en cuenta que Go no ofrece una función `fork` clásica de Unix.
# Por lo general, esto no es un problema, ya que
# iniciar gorutinas, crear procesos y ejecutar
# procesos cubre la mayoría de los casos de uso de `fork`.
```
