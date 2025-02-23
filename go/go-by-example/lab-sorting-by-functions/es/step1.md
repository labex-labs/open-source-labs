# Ordenamiento por Funciones

El problema que se debe resolver en este laboratorio es implementar una función de ordenamiento personalizada en Go que ordene una slice de cadenas por su longitud.

- El tipo `byLength` debe crearse como un alias del tipo `[]string`.
- La interfaz `sort.Interface` debe implementarse en el tipo `byLength`.
- Las funciones `Len` y `Swap` deben implementarse en el tipo `byLength`.
- La función `Less` debe implementarse en el tipo `byLength` para contener la lógica de ordenamiento personalizada real.
- La función `main` debe convertir la slice original `fruits` a `byLength`, y luego usar `sort.Sort` en esa slice tipada.

```sh
# Ejecutar nuestro programa muestra una lista ordenada por
# la longitud de la cadena, como se desea.
$ go run sorting-by-functions.go
[kiwi peach banana]

# Siguiendo este mismo patrón de creación de un tipo
# personalizado, implementación de los tres métodos
# `Interface` en ese tipo y luego llamada a sort.Sort en
# una colección de ese tipo personalizado, podemos
# ordenar slices de Go por funciones arbitrarias.
```

A continuación está el código completo:

```go
// A veces querremos ordenar una colección por algo
// diferente a su orden natural. Por ejemplo, supongamos
// que queremos ordenar cadenas por su longitud en lugar
// de alfabéticamente. Aquí hay un ejemplo de ordenamientos
// personalizados en Go.

package main

import (
	"fmt"
	"sort"
)

// Para ordenar por una función personalizada en Go,
// necesitamos un tipo correspondiente. Aquí hemos
// creado un tipo `byLength` que es solo un alias del
// tipo integrado `[]string`.
type byLength []string

// Implementamos la interfaz `sort.Interface` - `Len`,
// `Less` y `Swap` - en nuestro tipo para poder usar la
// función genérica `Sort` del paquete `sort`. `Len` y
// `Swap` suelen ser similares entre tipos y `Less`
// contendrá la lógica de ordenamiento personalizada real.
// En nuestro caso queremos ordenar en orden de
// longitud de cadena creciente, así que usamos
// `len(s[i])` y `len(s[j])` aquí.
func (s byLength) Len() int {
	return len(s)
}
func (s byLength) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}
func (s byLength) Less(i, j int) bool {
	return len(s[i]) < len(s[j])
}

// Con todo esto en su lugar, ahora podemos implementar
// nuestro ordenamiento personalizado convirtiendo la
// slice original `fruits` a `byLength`, y luego usar
// `sort.Sort` en esa slice tipada.
func main() {
	fruits := []string{"peach", "banana", "kiwi"}
	sort.Sort(byLength(fruits))
	fmt.Println(fruits)
}

```
