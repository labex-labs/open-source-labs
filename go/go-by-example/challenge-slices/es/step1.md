# Slices

El problema que se debe resolver en este desafío es crear y manipular slices en Go. Necesitará crear un slice vacío con longitud no nula, establecer y obtener valores en el slice, usar la función `len` para obtener la longitud del slice, usar la función `append` para agregar nuevos valores al slice, usar la función `copy` para copiar un slice y usar el operador de slice para obtener un subslice de elementos de un slice existente.

## Requisitos

Para completar este desafío, necesitará tener un conocimiento básico de la sintaxis de Go y el tipo de datos slice. También necesitará estar familiarizado con las funciones `make`, `append` y `copy`, así como con el operador de slice.

## Ejemplo

```sh
# Tenga en cuenta que aunque los slices son de tipos diferentes que los arrays,
# se representan de manera similar por `fmt.Println`.
$ go run slices.go
emp: [ ]
set: [a b c]
get: c
len: 3
apd: [a b c d e f]
cpy: [a b c d e f]
sl1: [c d e]
sl2: [a b c d e]
sl3: [c d e f]
dcl: [g h i]
2d: [[0] [1 2] [2 3 4]]

# Eche un vistazo a esta [excelente publicación en el blog](https://go.dev/blog/slices-intro)
# del equipo de Go para obtener más detalles sobre el diseño y
# la implementación de slices en Go.

# Ahora que hemos visto arrays y slices, veremos
# la otra estructura de datos integrada clave de Go: mapas.
```
