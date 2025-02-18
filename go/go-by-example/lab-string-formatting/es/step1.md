# Formato de Cadenas

Se te pide que formes diferentes tipos de datos utilizando diversos verbos de formato en Golang.

- Debes utilizar el paquete `fmt` para formatear los datos.
- Debes utilizar el verbo de formato correcto para cada tipo de dato.
- Debes ser capaz de formatear enteros, números de punto flotante, cadenas y estructuras.
- Debes ser capaz de controlar el ancho y la precisión de la salida.
- Debes ser capaz de justificar la salida a la izquierda o a la derecha.

```sh
$ go run string-formatting.go
struct1: {1 2}
struct2: {x:1 y:2}
struct3: main.point{x:1, y:2}
type: main.point
bool: true
int: 123
bin: 1110
char:!
hex: 1c8
float1: 78.900000
float2: 1.234000e+08
float3: 1.234000E+08
str1: "string"
str2: "\"string\""
str3: 6865782074686973
pointer: 0xc0000ba000
width1: | 12 | 345 \
  | width2: | 1.20 | 3.45 \
  | width3: | 1.20 | 3.45 \
  | width4: | foo | b \
  | width5: | foo | b \
  | sprintf: a string
io: an error
```

A continuación, se muestra el código completo:

```go
// Go ofrece una excelente compatibilidad para el formato de cadenas
// en la tradición de `printf`. Aquí hay algunos ejemplos de
// tareas comunes de formato de cadenas.

package main

import (
	"fmt"
	"os"
)

type point struct {
	x, y int
}

func main() {

	// Go ofrece varios "verbos" de impresión diseñados para
	// formatear valores generales de Go. Por ejemplo, esto imprime
	// una instancia de nuestra estructura `point`.
	p := point{1, 2}
	fmt.Printf("struct1: %v\n", p)

	// Si el valor es una estructura, la variante `%+v` incluirá
	// los nombres de los campos de la estructura.
	fmt.Printf("struct2: %+v\n", p)

	// La variante `%#v` imprime una representación de sintaxis de Go
	// del valor, es decir, el fragmento de código fuente que
	// produciría ese valor.
	fmt.Printf("struct3: %#v\n", p)

	// Para imprimir el tipo de un valor, utiliza `%T`.
	fmt.Printf("type: %T\n", p)

	// Formatear booleanos es sencillo.
	fmt.Printf("bool: %t\n", true)

	// Hay muchas opciones para formatear enteros.
	// Utiliza `%d` para el formato estándar en base 10.
	fmt.Printf("int: %d\n", 123)

	// Esto imprime una representación binaria.
	fmt.Printf("bin: %b\n", 14)

	// Esto imprime el carácter correspondiente al
	// entero dado.
	fmt.Printf("char: %c\n", 33)

	// `%x` proporciona codificación hexadecimal.
	fmt.Printf("hex: %x\n", 456)

	// También hay varias opciones de formato para
	// números de punto flotante. Para el formato decimal básico, utiliza `%f`.
	fmt.Printf("float1: %f\n", 78.9)

	// `%e` y `%E` formatean el número de punto flotante en (ligeramente
	// diferentes versiones de) notación científica.
	fmt.Printf("float2: %e\n", 123400000.0)
	fmt.Printf("float3: %E\n", 123400000.0)

	// Para la impresión básica de cadenas, utiliza `%s`.
	fmt.Printf("str1: %s\n", "\"string\"")

	// Para poner comillas dobles a las cadenas como en el código fuente de Go, utiliza `%q`.
	fmt.Printf("str2: %q\n", "\"string\"")

	// Al igual que con los enteros vistos anteriormente, `%x` representa
	// la cadena en base 16, con dos caracteres de salida por byte de entrada.
	fmt.Printf("str3: %x\n", "hex this")

	// Para imprimir una representación de un puntero, utiliza `%p`.
	fmt.Printf("pointer: %p\n", &p)

	// Al formatear números, a menudo querrás
	// controlar el ancho y la precisión del resultado.
	// Para especificar el ancho de un entero, utiliza un número después del `%` en el verbo.
	// Por defecto, el resultado se justificará a la derecha y se rellenará con espacios.
	fmt.Printf("width1: |%6d|%6d|\n", 12, 345)

	// También puedes especificar el ancho de los números de punto flotante impresos,
	// aunque generalmente también querrás restringir la precisión decimal al mismo tiempo
	// con la sintaxis ancho.precisión.
	fmt.Printf("width2: |%6.2f|%6.2f|\n", 1.2, 3.45)

	// Para justificar a la izquierda, utiliza la bandera `-`.
	fmt.Printf("width3: |%-6.2f|%-6.2f|\n", 1.2, 3.45)

	// También es posible que desees controlar el ancho al formatear cadenas,
	// especialmente para asegurarte de que se alineen en una salida similar a una tabla.
	// Para un ancho básico justificado a la derecha.
	fmt.Printf("width4: |%6s|%6s|\n", "foo", "b")

	// Para justificar a la izquierda, utiliza la bandera `-` como con los números.
	fmt.Printf("width5: |%-6s|%-6s|\n", "foo", "b")

	// Hasta ahora hemos visto `Printf`, que imprime la cadena formateada en `os.Stdout`.
	// `Sprintf` formatea y devuelve una cadena sin imprimirla en ningún lugar.
	s := fmt.Sprintf("sprintf: a %s", "string")
	fmt.Println(s)

	// Puedes formatear e imprimir en `io.Writers` diferentes de `os.Stdout` utilizando `Fprintf`.
	fmt.Fprintf(os.Stderr, "io: an %s\n", "error")
}

```
