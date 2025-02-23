# Iteración sobre canales

Se te pide escribir una función que tome un canal de enteros y devuelva la suma de todos los enteros recibidos a través del canal.

- La función debe llamarse `sumInts`.
- La función debe tomar un solo parámetro de tipo `chan int`.
- La función debe devolver un solo valor entero.
- No se permite utilizar ningún bucle o recursión dentro del cuerpo de la función.
- No se permite utilizar ningún paquete externo.

```sh
$ go run range-over-channels.go
uno
dos

# Este ejemplo también mostró que es posible cerrar
# un canal no vacío pero aún así recibir los valores restantes.
```

A continuación está el código completo:

```go
// En un [ejemplo anterior](range) vimos cómo `for` y
// `range` proporcionan iteración sobre estructuras de datos básicas.
// También podemos utilizar esta sintaxis para iterar sobre
// los valores recibidos a través de un canal.

package main

import "fmt"

func main() {

	// Iteraremos sobre 2 valores en el canal `queue`.
	queue := make(chan string, 2)
	queue <- "uno"
	queue <- "dos"
	close(queue)

	// Esta `range` itera sobre cada elemento a medida que
	// es recibido de `queue`. Debido a que cerramos el
	// canal anteriormente, la iteración termina después
	// de recibir los 2 elementos.
	for elem := range queue {
		fmt.Println(elem)
	}
}

```
