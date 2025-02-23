# if-else

Se te pide que completes la función `checkNumber` que toma un entero como entrada y devuelve una cadena. Si el número es par, devuelve "even" (par), de lo contrario devuelve "odd" (impar).

- La función debe llamarse `checkNumber`.
- La función debe tomar un entero como entrada.
- La función debe devolver una cadena.
- Si el número es par, devuelve "even".
- Si el número es impar, devuelve "odd".

```sh
$ go run if-else.go
7 es impar
8 es divisible por 4
9 tiene 1 dígito

# No hay [ternario if](https://en.wikipedia.org/wiki/%3F:)
# en Go, por lo que necesitarás usar una declaración `if` completa incluso
# para condiciones básicas.
```

A continuación está el código completo:

```go
// La bifurcación con `if` y `else` en Go es
// directa.

package main

import "fmt"

func main() {

	// Aquí hay un ejemplo básico.
	if 7%2 == 0 {
		fmt.Println("7 es par")
	} else {
		fmt.Println("7 es impar")
	}

	// Puedes tener una declaración `if` sin un else.
	if 8%4 == 0 {
		fmt.Println("8 es divisible por 4")
	}

	// Una declaración puede preceder a las condicionales; cualquier variable
	// declarada en esta declaración está disponible en la actual
	// y en todas las ramas subsiguientes.
	if num := 9; num < 0 {
		fmt.Println(num, "es negativo")
	} else if num < 10 {
		fmt.Println(num, "tiene 1 dígito")
	} else {
		fmt.Println(num, "tiene múltiples dígitos")
	}
}

// Tenga en cuenta que no necesita paréntesis alrededor de las condiciones
// en Go, pero que se requieren las llaves.

```
