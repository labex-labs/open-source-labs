# Arrays

Se te pide crear un array de enteros con una longitud de 5. Luego establecerás un valor en un índice específico y recuperará un valor de un índice específico. También se te pedirá encontrar la longitud del array y declarar e inicializar un array en una sola línea. Finalmente, crearás un array bidimensional e inicializarás con valores.

- Crear un array de enteros con una longitud de 5
- Establecer un valor en un índice específico y recuperar un valor de un índice específico
- Encontrar la longitud del array
- Declarar e inicializar un array en una sola línea
- Crear un array bidimensional e inicializarlo con valores

```sh
# Tenga en cuenta que los arrays aparecen en la forma `[v1 v2 v3...]`
# cuando se imprime con `fmt.Println`.
$ go run arrays.go
emp: [0 0 0 0 0]
set: [0 0 0 0 100]
get: 100
len: 5
dcl: [1 2 3 4 5]
2d: [[0 1 2] [1 2 3]]
```

A continuación está el código completo:

```go
// En Go, un _array_ es una secuencia numerada de elementos de un
// longitud específica. En el código típico de Go, [slices](slices) son
// mucho más comunes; los arrays son útiles en algunos casos especiales.

package main

import "fmt"

func main() {

	// Aquí creamos un array `a` que contendrá exactamente
	// 5 `int`s. El tipo de elementos y la longitud son ambos
	// parte del tipo de array. Por defecto, un array está
	// con valores cero, lo que para `int`s significa `0`s.
	var a [5]int
	fmt.Println("emp:", a)

	// Podemos establecer un valor en un índice usando la
	// sintaxis `array[index] = value`, y obtener un valor con
	// `array[index]`.
	a[4] = 100
	fmt.Println("set:", a)
	fmt.Println("get:", a[4])

	// La función interna `len` devuelve la longitud de un array.
	fmt.Println("len:", len(a))

	// Utilice esta sintaxis para declarar e inicializar un array
	// en una sola línea.
	b := [5]int{1, 2, 3, 4, 5}
	fmt.Println("dcl:", b)

	// Los tipos de array son unidimensionales, pero puede
	// componer tipos para construir estructuras de datos
	// multidimensionales.
	var twoD [2][3]int
	for i := 0; i < 2; i++ {
		for j := 0; j < 3; j++ {
			twoD[i][j] = i + j
		}
	}
	fmt.Println("2d: ", twoD)
}

```
