# Arrays (Arrays)

Você precisará criar um array (array) de inteiros com um comprimento de 5. Em seguida, você definirá um valor em um índice específico e recuperará um valor de um índice específico. Você também precisará encontrar o comprimento do array e declarar e inicializar um array em uma linha. Finalmente, você criará um array bidimensional e o inicializará com valores.

- Criar um array de inteiros com um comprimento de 5
- Definir um valor em um índice específico e recuperar um valor de um índice específico
- Encontrar o comprimento do array
- Declarar e inicializar um array em uma linha
- Criar um array bidimensional e inicializá-lo com valores

```sh
# Note that arrays appear in the form `[v1 v2 v3 ...]`
# when printed with `fmt.Println`.
$ go run arrays.go
emp: [0 0 0 0 0]
set: [0 0 0 0 100]
get: 100
len: 5
dcl: [1 2 3 4 5]
2d: [[0 1 2] [1 2 3]]
```

Abaixo está o código completo:

```go
// In Go, an _array_ is a numbered sequence of elements of a
// specific length. In typical Go code, [slices](slices) are
// much more common; arrays are useful in some special
// scenarios.

package main

import "fmt"

func main() {

	// Here we create an array `a` that will hold exactly
	// 5 `int`s. The type of elements and length are both
	// part of the array's type. By default an array is
	// zero-valued, which for `int`s means `0`s.
	var a [5]int
	fmt.Println("emp:", a)

	// We can set a value at an index using the
	// `array[index] = value` syntax, and get a value with
	// `array[index]`.
	a[4] = 100
	fmt.Println("set:", a)
	fmt.Println("get:", a[4])

	// The builtin `len` returns the length of an array.
	fmt.Println("len:", len(a))

	// Use this syntax to declare and initialize an array
	// in one line.
	b := [5]int{1, 2, 3, 4, 5}
	fmt.Println("dcl:", b)

	// Array types are one-dimensional, but you can
	// compose types to build multi-dimensional data
	// structures.
	var twoD [2][3]int
	for i := 0; i < 2; i++ {
		for j := 0; j < 3; j++ {
			twoD[i][j] = i + j
		}
	}
	fmt.Println("2d: ", twoD)
}
```
