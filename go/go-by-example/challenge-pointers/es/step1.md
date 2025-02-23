# Punteros

El problema es entender cómo funcionan los punteros en contraste con los valores mediante dos funciones: `zeroval` y `zeroptr`. `zeroval` tiene un parámetro de tipo `int`, por lo que los argumentos se pasarán a ella por valor. `zeroval` obtendrá una copia de `ival` distinta de la que existe en la función llamante. En contraste, `zeroptr` tiene un parámetro de tipo `*int`, lo que significa que toma un puntero a `int`. El código `*iptr` en el cuerpo de la función luego _desreferencia_ el puntero desde su dirección de memoria hasta el valor actual en esa dirección. Asignar un valor a un puntero desreferenciado cambia el valor en la dirección de memoria referenciada.

## Requisitos

- Debería tener un conocimiento básico de Golang.
- Debería saber cómo definir y usar funciones en Golang.
- Debería saber cómo usar punteros en Golang.

## Ejemplo

```sh
# `zeroval` no cambia la variable `i` en `main`, pero
# `zeroptr` sí lo hace porque tiene una referencia a
# la dirección de memoria de esa variable.
$ go run pointers.go
inicial: 1
zeroval: 1
zeroptr: 0
puntero: 0x42131100
```
