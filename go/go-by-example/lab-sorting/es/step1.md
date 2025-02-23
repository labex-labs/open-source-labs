# Clasificación

El problema que se debe resolver en este laboratorio es clasificar rebanadas de cadenas y enteros utilizando el paquete `sort`.

- El paquete `sort` debe ser importado.
- La función `sort.Strings()` debe ser utilizada para clasificar una rebanada de cadenas.
- La función `sort.Ints()` debe ser utilizada para clasificar una rebanada de enteros.
- La función `sort.IntsAreSorted()` debe ser utilizada para comprobar si una rebanada de enteros ya está clasificada.

```sh
# Ejecutar nuestro programa imprime las rebanadas de cadenas y enteros clasificadas
# y `true` como resultado de nuestra prueba `AreSorted`.
$ go run sorting.go
Strings: [a b c]
Ints: [2 4 7]
Sorted: true
```

A continuación está el código completo:

```go
// El paquete `sort` de Go implementa la clasificación para tipos integrados
// y definidos por el usuario. Primero veremos la clasificación para
// tipos integrados.

package main

import (
	"fmt"
	"sort"
)

func main() {

	// Los métodos de clasificación son específicos del tipo integrado;
	// aquí hay un ejemplo para cadenas. Tenga en cuenta que la clasificación es
	// en el lugar, por lo que cambia la rebanada dada y no
	// devuelve una nueva.
	strs := []string{"c", "a", "b"}
	sort.Strings(strs)
	fmt.Println("Strings:", strs)

	// Un ejemplo de clasificación de `int`s.
	ints := []int{7, 2, 4}
	sort.Ints(ints)
	fmt.Println("Ints:   ", ints)

	// También podemos utilizar `sort` para comprobar si una rebanada está
	// ya en orden clasificador.
	s := sort.IntsAreSorted(ints)
	fmt.Println("Sorted: ", s)
}

```
