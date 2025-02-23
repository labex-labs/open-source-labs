# Lectura de Archivos

Necesitas leer archivos en tu programa de Go y realizar diferentes operaciones en los datos del archivo.

## Requisitos

- Debes estar familiarizado con los conceptos básicos de programación en Go.
- Debes tener Go instalado en tu computadora.

## Ejemplo

```sh
$ echo "hello" > /tmp/dat
$ echo "go" >> /tmp/dat
$ go run reading-files.go
hello
go
5 bytes: hello
2 bytes @ 6: go
2 bytes @ 6: go
5 bytes: hello

# A continuación veremos cómo escribir archivos.
```
