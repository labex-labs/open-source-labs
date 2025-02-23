# Filtros de línea

El problema que se debe resolver en este desafío es escribir un programa en Go que lea el texto de entrada desde stdin, ponga en mayúsculas todas las letras del texto y luego imprima el texto modificado en stdout.

## Requisitos

- El programa debe leer el texto de entrada desde stdin.
- El programa debe poner en mayúsculas todas las letras del texto de entrada.
- El programa debe imprimir el texto modificado en stdout.

## Ejemplo

```sh
# Para probar nuestro filtro de línea, primero crea un archivo con
# algunas líneas en minúsculas.
$ echo 'hello' > /tmp/lines
$ echo 'filter' >> /tmp/lines

# Luego utiliza el filtro de línea para obtener líneas en mayúsculas.
$ cat /tmp/lines | go run line-filters.go
HELLO
FILTER
```
