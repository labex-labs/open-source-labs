# Errores

El laboratorio proporciona dos funciones que devuelven un error si el argumento de entrada es 42. La primera función devuelve un valor de error básico, mientras que la segunda función utiliza un tipo personalizado para representar el error.

- El paquete `errors` debe ser importado.
- La función `f1` debe devolver un error si el argumento de entrada es 42.
- La función `f2` debe devolver un error del tipo `argError` si el argumento de entrada es 42.
- El tipo `argError` debe tener dos campos: `arg` y `prob`.
- El tipo `argError` debe implementar el método `Error()`.
- La función `main` debe llamar a ambas `f1` y `f2` con argumentos de entrada de 7 y 42.
- La función `main` debe imprimir el resultado de cada llamada a función, junto con cualquier error que haya sido devuelto.
- La función `main` debe demostrar cómo utilizar programáticamente los datos en un error personalizado.

```sh
$ go run errors.go
f1 funcionó: 10
f1 falló: no se puede trabajar con 42
f2 funcionó: 10
f2 falló: 42 - no se puede trabajar con él
42
no se puede trabajar con él

# Consulte esta [gran publicación](https://go.dev/blog/error-handling-and-go)
# en el blog de Go para obtener más información sobre el manejo de errores.
```

A continuación está el código completo:

```go
// En Go es idiomático comunicar errores a través de un
// valor de retorno explícito y separado. Esto contrasta con
// las excepciones utilizadas en lenguajes como Java y Ruby y
// el valor de resultado / error sobrecargado y único que
// a veces se utiliza en C. El enfoque de Go hace que sea
// fácil ver qué funciones devuelven errores y manejarlos
// utilizando las mismas estructuras de lenguaje empleadas
// para cualquier otra tarea no de error.

package main

import (
	"errors"
	"fmt"
)

// Por convención, los errores son el último valor de retorno y
// tienen el tipo `error`, una interfaz incorporada.
func f1(arg int) (int, error) {
	if arg == 42 {

		// `errors.New` construye un valor básico de `error`
		// con el mensaje de error dado.
		return -1, errors.New("no se puede trabajar con 42")

	}

	// Un valor `nil` en la posición de error indica que
	// no hubo error.
	return arg + 3, nil
}

// Es posible utilizar tipos personalizados como `error`s al
// implementar el método `Error()` en ellos. Aquí hay una
// variante del ejemplo anterior que utiliza un tipo
// personalizado para representar explícitamente un error de
// argumento.
type argError struct {
	arg  int
	prob string
}

func (e *argError) Error() string {
	return fmt.Sprintf("%d - %s", e.arg, e.prob)
}

func f2(arg int) (int, error) {
	if arg == 42 {

		// En este caso usamos la sintaxis `&argError` para
		// construir un nuevo struct, suministrando valores
		// para los dos campos `arg` y `prob`.
		return -1, &argError{arg, "no se puede trabajar con él"}
	}
	return arg + 3, nil
}

func main() {

	// Los dos bucles siguientes prueban cada una de nuestras
	// funciones que devuelven errores. Tenga en cuenta que
	// el uso de una comprobación de error en línea en la
	// línea `if` es un idioma común en el código de Go.
	for _, i := range []int{7, 42} {
		if r, e := f1(i); e!= nil {
			fmt.Println("f1 falló:", e)
		} else {
			fmt.Println("f1 funcionó:", r)
		}
	}
	for _, i := range []int{7, 42} {
		if r, e := f2(i); e!= nil {
			fmt.Println("f2 falló:", e)
		} else {
			fmt.Println("f2 funcionó:", r)
		}
	}

	// Si desea utilizar programáticamente los datos en un
	// error personalizado, necesitará obtener el error como
	// una instancia del tipo de error personalizado a través
	// de una afirmación de tipo.
	_, e := f2(42)
	if ae, ok := e.(*argError); ok {
		fmt.Println(ae.arg)
		fmt.Println(ae.prob)
	}
}

```
