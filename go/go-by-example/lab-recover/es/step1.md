# Recuperar

La función `mayPanic` en el código proporcionado causará un pánico cuando se invoque. Tu tarea es modificar la función `main` para recuperar del pánico e imprimir el mensaje de error.

- Utiliza la función `recover` para manejar el pánico en la función `mayPanic`.
- Imprime el mensaje de error cuando ocurre un pánico.

```sh
$ go run recover.go
Recuperado. Error:
un problema
```

A continuación está el código completo:

```go
// Go permite _recuperarse_ de un pánico, mediante
// el uso de la función integrada `recover`. Un `recover` puede
// detener un `pánico` que abortaría el programa y permitirle
// continuar con la ejecución en su lugar.

// Un ejemplo de dónde esto puede ser útil: un servidor
// no querría detenerse si una de las conexiones de cliente
// presenta un error crítico. En cambio, el servidor
// querría cerrar esa conexión y continuar atendiendo
// a otros clientes. De hecho, esto es lo que hace por defecto
// Go's `net/http` para los servidores HTTP.

package main

import "fmt"

// Esta función produce un pánico.
func mayPanic() {
	panic("un problema")
}

func main() {
	// `recover` debe ser llamado dentro de una función deferrada.
	// Cuando la función envolvente entra en pánico, la defer
	// se activará y una llamada a `recover` dentro de ella capturará
	// el pánico.
	defer func() {
		if r := recover(); r!= nil {
			// El valor de retorno de `recover` es el error generado en
			// la llamada a `panic`.
			fmt.Println("Recuperado. Error:\n", r)
		}
	}()

	mayPanic()

	// Este código no se ejecutará, porque `mayPanic` produce un pánico.
	// La ejecución de `main` se detiene en el punto del
	// pánico y se reanuda en la cláusula deferrada.
	fmt.Println("Después de mayPanic()")
}

```
