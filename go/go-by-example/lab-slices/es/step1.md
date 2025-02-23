# Slices

El problema que se debe resolver en este laboratorio es crear y manipular slices en Go. Necesitará crear un slice vacío con longitud no nula, establecer y obtener valores en el slice, usar la función `len` para obtener la longitud del slice, usar la función `append` para agregar nuevos valores al slice, usar la función `copy` para copiar un slice y usar el operador de slice para obtener un slice de elementos de un slice existente.

Para completar este laboratorio, necesitará tener un conocimiento básico de la sintaxis de Go y el tipo de datos slice. También necesitará estar familiarizado con las funciones `make`, `append` y `copy`, así como con el operador de slice.

```sh
# Tenga en cuenta que aunque los slices son de un tipo diferente que las matrices,
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
# la implementación de los slices en Go.

# Ahora que hemos visto matrices y slices, veremos
# la otra estructura de datos integrada principal de Go: mapas.
```

A continuación está el código completo:

```go
// Los _Slices_ son un tipo de datos importante en Go, que
// ofrece una interfaz más potente para secuencias que las matrices.

package main

import "fmt"

func main() {

	// A diferencia de las matrices, los slices solo se tipifican por
	// los elementos que contienen (no por el número de elementos).
	// Para crear un slice vacío con longitud no nula, use
	// la función integrada `make`. Aquí creamos un slice de
	// `string`s de longitud `3` (inicialmente con valores cero).
	s := make([]string, 3)
	fmt.Println("emp:", s)

	// Podemos establecer y obtener valores igual que con las matrices.
	s[0] = "a"
	s[1] = "b"
	s[2] = "c"
	fmt.Println("set:", s)
	fmt.Println("get:", s[2])

	// `len` devuelve la longitud del slice como se esperaría.
	fmt.Println("len:", len(s))

	// Además de estas operaciones básicas, los slices
	// admiten varias más que los hacen más ricos que
	// las matrices. Una es la función integrada `append`, que
	// devuelve un slice que contiene uno o más nuevos valores.
	// Tenga en cuenta que necesitamos aceptar un valor de retorno de
	// `append` ya que puede que obtengamos un nuevo valor de slice.
	s = append(s, "d")
	s = append(s, "e", "f")
	fmt.Println("apd:", s)

	// Los slices también se pueden `copiar`. Aquí creamos un
	// slice vacío `c` de la misma longitud que `s` y copiamos
	// en `c` desde `s`.
	c := make([]string, len(s))
	copy(c, s)
	fmt.Println("cpy:", c)

	// Los slices admiten un operador de "slice" con la sintaxis
	// `slice[low:high]`. Por ejemplo, esto obtiene un slice
	// de los elementos `s[2]`, `s[3]` y `s[4]`.
	l := s[2:5]
	fmt.Println("sl1:", l)

	// Esto crea un slice hasta (pero sin incluir) `s[5]`.
	l = s[:5]
	fmt.Println("sl2:", l)

	// Y esto crea un slice a partir de (e incluyendo) `s[2]`.
	l = s[2:]
	fmt.Println("sl3:", l)

	// También podemos declarar e inicializar una variable para slice
	// en una sola línea.
	t := []string{"g", "h", "i"}
	fmt.Println("dcl:", t)

	// Los slices se pueden componer en estructuras de datos
	// multidimensionales. La longitud de los slices internos puede
	// variar, a diferencia de las matrices multidimensionales.
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
