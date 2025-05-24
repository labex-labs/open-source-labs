# Slices (Fatias)

O problema a ser resolvido neste laboratório é criar e manipular slices (fatias) em Go. Você precisará criar um slice vazio com comprimento não nulo, definir e obter valores no slice, usar a função `len` para obter o comprimento do slice, usar a função `append` para adicionar novos valores ao slice, usar a função `copy` para copiar um slice e usar o operador de slice para obter um slice de elementos de um slice existente.

Para completar este laboratório, você precisará ter um conhecimento básico da sintaxe Go e do tipo de dado slice. Você também precisará estar familiarizado com as funções `make`, `append` e `copy`, bem como com o operador de slice.

```sh
# Note that while slices are different types than arrays,
# they are rendered similarly by `fmt.Println`.
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

# Check out this [great blog post](https://go.dev/blog/slices-intro)
# by the Go team for more details on the design and
# implementation of slices in Go.

# Now that we've seen arrays and slices we'll look at
# Go's other key builtin data structure: maps.
```

Aqui está o código completo:

```go
// _Slices_ are an important data type in Go, giving
// a more powerful interface to sequences than arrays.

package main

import "fmt"

func main() {

	// Unlike arrays, slices are typed only by the
	// elements they contain (not the number of elements).
	// To create an empty slice with non-zero length, use
	// the builtin `make`. Here we make a slice of
	// `string`s of length `3` (initially zero-valued).
	s := make([]string, 3)
	fmt.Println("emp:", s)

	// We can set and get just like with arrays.
	s[0] = "a"
	s[1] = "b"
	s[2] = "c"
	fmt.Println("set:", s)
	fmt.Println("get:", s[2])

	// `len` returns the length of the slice as expected.
	fmt.Println("len:", len(s))

	// In addition to these basic operations, slices
	// support several more that make them richer than
	// arrays. One is the builtin `append`, which
	// returns a slice containing one or more new values.
	// Note that we need to accept a return value from
	// `append` as we may get a new slice value.
	s = append(s, "d")
	s = append(s, "e", "f")
	fmt.Println("apd:", s)

	// Slices can also be `copy`'d. Here we create an
	// empty slice `c` of the same length as `s` and copy
	// into `c` from `s`.
	c := make([]string, len(s))
	copy(c, s)
	fmt.Println("cpy:", c)

	// Slices support a "slice" operator with the syntax
	// `slice[low:high]`. For example, this gets a slice
	// of the elements `s[2]`, `s[3]`, and `s[4]`.
	l := s[2:5]
	fmt.Println("sl1:", l)

	// This slices up to (but excluding) `s[5]`.
	l = s[:5]
	fmt.Println("sl2:", l)

	// And this slices up from (and including) `s[2]`.
	l = s[2:]
	fmt.Println("sl3:", l)

	// We can declare and initialize a variable for slice
	// in a single line as well.
	t := []string{"g", "h", "i"}
	fmt.Println("dcl:", t)

	// Slices can be composed into multi-dimensional data
	// structures. The length of the inner slices can
	// vary, unlike with multi-dimensional arrays.
	twoD := make([][]int, 3)
	for i := 0; i < 3; i++ {
		innerLen := i + 1
		twoD[i] = make([]int, innerLen)
		for j := 0; j < innerLen; j++ {
			twoD[i][j] = i + j
		}
	}
	fmt.Println("2d: ", twoD)
}
```
