# Números aleatorios

Se te pide escribir un programa que genere enteros y flotantes aleatorios dentro de un rango especificado. El programa también debería ser capaz de producir secuencias variables de números cambiando la semilla.

- El programa debe utilizar el paquete `math/rand` para generar números aleatorios.
- El programa debe generar enteros aleatorios dentro de un rango especificado.
- El programa debe generar flotantes aleatorios dentro de un rango especificado.
- El programa debe ser capaz de producir secuencias variables de números cambiando la semilla.

```sh
# Dependiendo de donde ejecutes este ejemplo, algunos de los
# números generados pueden ser diferentes. Tenga en cuenta que en
# el Go playground sembrando con `time.Now()` todavía
# produce resultados deterministas debido a la forma en que
# está implementado el playground.
$ go run random-numbers.go
81,87
0.6645600532184904
7.123187485356329,8.434115364335547
0,28
5,87
5,87

# Consulte la documentación del paquete [`math/rand`](https://pkg.go.dev/math/rand)
# para obtener referencias sobre otras cantidades aleatorias
# que Go puede proporcionar.
```

A continuación está el código completo:

```go
// El paquete `math/rand` de Go proporciona
// [generación de números pseudoaleatorios](https://en.wikipedia.org/wiki/Pseudorandom_number_generator).

package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {

	// Por ejemplo, `rand.Intn` devuelve un `int` aleatorio n,
	// `0 <= n < 100`.
	fmt.Print(rand.Intn(100), ",")
	fmt.Print(rand.Intn(100))
	fmt.Println()

	// `rand.Float64` devuelve un `float64` `f`,
	// `0.0 <= f < 1.0`.
	fmt.Println(rand.Float64())

	// Esto se puede utilizar para generar flotantes aleatorios en
	// otros rangos, por ejemplo `5.0 <= f' < 10.0`.
	fmt.Print((rand.Float64()*5)+5, ",")
	fmt.Print((rand.Float64() * 5) + 5)
	fmt.Println()

	// El generador de números predeterminado es determinista, por lo que
	// producirá la misma secuencia de números cada vez por defecto.
	// Para producir secuencias variables, dale una semilla que cambie.
	// Tenga en cuenta que esto no es seguro de utilizar para números aleatorios que
	// desees que sean secretos; utilice `crypto/rand` para aquellos.
	s1 := rand.NewSource(time.Now().UnixNano())
	r1 := rand.New(s1)

	// Llame al resultado `rand.Rand` de la misma manera que
	// las funciones del paquete `rand`.
	fmt.Print(r1.Intn(100), ",")
	fmt.Print(r1.Intn(100))
	fmt.Println()

	// Si semillas una fuente con el mismo número,
	// produce la misma secuencia de números aleatorios.
	s2 := rand.NewSource(42)
	r2 := rand.New(s2)
	fmt.Print(r2.Intn(100), ",")
	fmt.Print(r2.Intn(100))
	fmt.Println()
	s3 := rand.NewSource(42)
	r3 := rand.New(s3)
	fmt.Print(r3.Intn(100), ",")
	fmt.Print(r3.Intn(100))
}

```
