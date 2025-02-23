# Range

El problema que se debe resolver en este laboratorio es demostrar cómo utilizar `range` con slices, arrays, maps y strings.

Para completar este laboratorio, necesitarás:

- Conocimientos básicos de la sintaxis de Golang
- Golang instalado en tu máquina

```sh
$ go run range.go
sum: 9
index: 1
a - > apple
b - > banana
key: a
key: b
0 103
1 111
```

A continuación está el código completo:

```go
// _range_ itera sobre los elementos en una variedad de datos
// estructuras. Veamos cómo usar `range` con algunas
// de las estructuras de datos que ya hemos aprendido.

package main

import "fmt"

func main() {

	// Aquí usamos `range` para sumar los números de un slice.
	// Los arrays funcionan de la misma manera.
	nums := []int{2, 3, 4}
	sum := 0
	for _, num := range nums {
		sum += num
	}
	fmt.Println("sum:", sum)

	// `range` en arrays y slices proporciona tanto el
	// índice como el valor para cada entrada. Anteriormente no
	// necesitábamos el índice, así que lo ignoramos con el
	// identificador en blanco `_`. A veces, sin embargo, realmente
	// queremos los índices.
	for i, num := range nums {
		if num == 3 {
			fmt.Println("index:", i)
		}
	}

	// `range` en map itera sobre pares clave/valor.
	kvs := map[string]string{"a": "apple", "b": "banana"}
	for k, v := range kvs {
		fmt.Printf("%s -> %s\n", k, v)
	}

	// `range` también puede iterar solo sobre las claves de un map.
	for k := range kvs {
		fmt.Println("key:", k)
	}

	// `range` en strings itera sobre los puntos de código Unicode.
	// El primer valor es el índice de byte de inicio del `rune` y el
	// segundo el `rune` mismo.
	// Consulte [Strings and Runes](strings-and-runes) para obtener más
	// detalles.
	for i, c := range "go" {
		fmt.Println(i, c)
	}
}

```
