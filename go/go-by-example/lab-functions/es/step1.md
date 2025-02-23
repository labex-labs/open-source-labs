# Funciones

En el código dado, tenemos dos funciones `plus` y `plusPlus`. La función `plus` toma dos enteros como argumentos y devuelve su suma. La función `plusPlus` toma tres enteros como argumentos y devuelve su suma. Tu tarea es completar la función `plusPlus` sumando el tercer entero a la suma de los primeros dos enteros.

- La función `plus` debe tomar dos enteros como argumentos y devolver su suma como un entero.
- La función `plusPlus` debe tomar tres enteros como argumentos y devolver su suma como un entero.
- La función `plusPlus` debe utilizar la función `plus` para calcular la suma de los primeros dos enteros.

```sh
$ go run functions.go
1+2 = 3
1+2+3 = 6

# Hay varias otras características de las funciones de Go. Una es
# los múltiples valores de retorno, que veremos a continuación.
```

A continuación está el código completo:

```go
// Las _Funciones_ son centrales en Go. Vamos a aprender sobre
// funciones con algunos ejemplos diferentes.

package main

import "fmt"

// Aquí hay una función que toma dos `int`s y devuelve
// su suma como un `int`.
func plus(a int, b int) int {

	// Go requiere retornos explícitos, es decir, no
	// devolverá automáticamente el valor de la última
	// expresión.
	return a + b
}

// Cuando tienes múltiples parámetros consecutivos del
// mismo tipo, puedes omitir el nombre del tipo para los
// parámetros de tipo similar hasta el último parámetro que
// declara el tipo.
func plusPlus(a, b, c int) int {
	return a + b + c
}

func main() {

	// Llama a una función como se esperaría, con
	// `name(args)`.
	res := plus(1, 2)
	fmt.Println("1+2 =", res)

	res = plusPlus(1, 2, 3)
	fmt.Println("1+2+3 =", res)
}

```
