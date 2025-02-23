# Escribiendo archivos

Necesitas escribir un programa en Go que escriba una cadena y bytes en un archivo y utilice escritores con búfer.

## Requisitos

- El programa debe escribir una cadena y bytes en un archivo.
- El programa debe utilizar escritores con búfer.

## Ejemplo

```sh
# Intenta ejecutar el código de escritura de archivos.
$ go run writing-files.go
escribió 5 bytes
escribió 7 bytes
escribió 9 bytes

# Luego, verifica el contenido de los archivos escritos.
$ cat /tmp/dat1
hello
go
$ cat /tmp/dat2
some
writes
buffered

# A continuación, veremos cómo aplicar algunas de las ideas de E/S de archivos
# que acabamos de ver a los flujos `stdin` y `stdout`.
```
