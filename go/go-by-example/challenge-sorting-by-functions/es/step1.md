# Ordenamiento por Funciones

El problema que se debe resolver en este desafío es implementar una función de ordenamiento personalizada en Go que ordene una slice de cadenas por su longitud.

## Requisitos

- El tipo `byLength` debe crearse como un alias del tipo `[]string`.
- La interfaz `sort.Interface` debe implementarse en el tipo `byLength`.
- Las funciones `Len` y `Swap` deben implementarse en el tipo `byLength`.
- La función `Less` debe implementarse en el tipo `byLength` para contener la lógica de ordenamiento personalizada real.
- La función `main` debe convertir la slice original `fruits` a `byLength`, y luego usar `sort.Sort` en esa slice tipada.

## Ejemplo

```sh
# Ejecutar nuestro programa muestra una lista ordenada por
# la longitud de la cadena, como se desea.
$ go run sorting-by-functions.go
[kiwi peach banana]

# Siguiendo este mismo patrón de creación de un tipo
# personalizado, implementación de los tres métodos
# `Interface` en ese tipo, y luego llamada a sort.Sort en
# una colección de ese tipo personalizado, podemos
# ordenar slices de Go por funciones arbitrarias.
```
