# Funciones variádicas

En esta práctica, debes implementar una función llamada `max` que tome un número arbitrario de enteros como argumentos y devuelva el valor máximo.

- La función `max` debe tomar un número arbitrario de enteros como argumentos.
- La función `max` debe devolver el valor máximo de los enteros pasados como argumentos.

```sh
$ go run variadic-functions.go
[1 2] 3
[1 2 3] 6
[1 2 3 4] 10

# Otro aspecto clave de las funciones en Go es su capacidad
# para formar closures, que veremos a continuación.
```

A continuación está el código completo:

```go
// [_Funciones variádicas_](https://en.wikipedia.org/wiki/Variadic_function)
// se pueden llamar con cualquier número de argumentos finales.
// Por ejemplo, `fmt.Println` es una función variádica común.

package main

import "fmt"

// Aquí hay una función que tomará un número arbitrario
// de `int`s como argumentos.
func sum(nums...int) {
	fmt.Print(nums, " ")
	total := 0
	// Dentro de la función, el tipo de `nums` es
	// equivalente a `[]int`. Podemos llamar a `len(nums)`,
	// iterar sobre él con `range`, etc.
	for _, num := range nums {
		total += num
	}
	fmt.Println(total)
}

func main() {

	// Las funciones variádicas se pueden llamar de la manera
	// habitual con argumentos individuales.
	sum(1, 2)
	sum(1, 2, 3)

	// Si ya tienes múltiples argumentos en un slice,
	// aplícalos a una función variádica usando
	// `func(slice...)` de esta manera.
	nums := []int{1, 2, 3, 4}
	sum(nums...)
}

```
