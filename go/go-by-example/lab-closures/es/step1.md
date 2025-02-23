# Closures

Necesita crear una función que devuelva otra función. La función devuelta debe incrementar una variable en uno cada vez que se llama. La variable debe ser única para cada función devuelta.

- La función `intSeq` debe devolver otra función.
- La función devuelta debe incrementar una variable en uno cada vez que se llama.
- La variable debe ser única para cada función devuelta.

```sh
$ go run closures.go
1
2
3
1

# La última característica de las funciones que veremos por ahora es
# la recursión.
```

A continuación está el código completo:

```go
// Go admite [_funciones anónimas_](https://en.wikipedia.org/wiki/Anonymous_function),
// que pueden formar <a href="https://en.wikipedia.org/wiki/Closure_(computer_science)"><em>closures</em></a>.
// Las funciones anónimas son útiles cuando se desea definir
// una función en línea sin tener que nombrarla.

package main

import "fmt"

// Esta función `intSeq` devuelve otra función, que
// definimos anónimamente en el cuerpo de `intSeq`. La
// función devuelta _cierra_ la variable `i` para
// formar un closure.
func intSeq() func() int {
	i := 0
	return func() int {
		i++
		return i
	}
}

func main() {

	// Llamamos a `intSeq`, asignando el resultado (una función)
	// a `nextInt`. Este valor de función captura su
	// propio valor de `i`, que se actualizará cada vez
	// que llamemos a `nextInt`.
	nextInt := intSeq()

	// Veamos el efecto del closure llamando a `nextInt`
	// un par de veces.
	fmt.Println(nextInt())
	fmt.Println(nextInt())
	fmt.Println(nextInt())

	// Para confirmar que el estado es único para esa
	// función en particular, creamos y probamos una nueva.
	newInts := intSeq()
	fmt.Println(newInts())
}

```
