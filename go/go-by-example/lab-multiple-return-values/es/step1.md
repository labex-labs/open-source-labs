# Varios valores de retorno

Complete la función `swap` para devolver dos parámetros de entrada en orden inverso.

- La función `swap` debe tomar dos enteros como parámetros de entrada.
- La función `swap` debe devolver dos enteros en orden inverso.

```sh
$ go run multiple-return-values.go
3
7
7

# Aceptar un número variable de argumentos es otra característica
# agradable de las funciones de Go; veremos esto a continuación.
```

A continuación está el código completo:

```go
// Go tiene soporte integrado para _varios valores de retorno_.
// Esta característica se utiliza a menudo en Go idomático, por ejemplo
// para devolver tanto el resultado como los valores de error de una función.

package main

import "fmt"

// El `(int, int)` en esta firma de función muestra que
// la función devuelve 2 `int`s.
func vals() (int, int) {
	return 3, 7
}

func main() {

	// Aquí usamos los 2 diferentes valores de retorno de la
	// llamada con _asignación múltiple_.
	a, b := vals()
	fmt.Println(a)
	fmt.Println(b)

	// Si solo quieres un subconjunto de los valores devueltos,
	// utiliza el identificador en blanco `_`.
	_, c := vals()
	fmt.Println(c)
}

```
