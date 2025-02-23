# Cadenas y runas

El problema que se debe resolver en esta práctica es entender cómo trabajar con cadenas y runas en Go. En particular, la práctica cubrirá cómo obtener la longitud de una cadena, cómo acceder a un índice de una cadena, cómo contar el número de runas en una cadena y cómo iterar sobre las runas en una cadena.

Para completar esta práctica, se necesitará:

- Un conocimiento básico de la sintaxis de Go
- Conocimiento de las cadenas y runas de Go
- La biblioteca estándar de Go

```sh
$ go run strings-and-runes.go
Longitud: 18
e0 b8 aa e0 b8 a7 e0 b8 b1 e0 b8 aa e0 b8 94 e0 b8 b5
Número de runas: 6
U+0E2A 'ส' comienza en 0
U+0E27 'ว' comienza en 3
U+0E31 'ั' comienza en 6
U+0E2A 'ส' comienza en 9
U+0E14 'ด' comienza en 12
U+0E35 'ี' comienza en 15

Usando DecodeRuneInString
U+0E2A 'ส' comienza en 0
encontrado so sua
U+0E27 'ว' comienza en 3
U+0E31 'ั' comienza en 6
U+0E2A 'ส' comienza en 9
encontrado so sua
U+0E14 'ด' comienza en 12
U+0E35 'ี' comienza en 15
```

A continuación, se muestra el código completo:

```go
// Una cadena de Go es una rebanada de bytes de solo lectura. El lenguaje
// y la biblioteca estándar tratan las cadenas de manera especial, como
// contenedores de texto codificado en [UTF-8](https://en.wikipedia.org/wiki/UTF-8).
// En otros lenguajes, las cadenas están formadas por "caracteres".
// En Go, el concepto de carácter se denomina `rune`; es
// un entero que representa un punto de código Unicode.
// [Esta publicación del blog de Go](https://go.dev/blog/strings) es una buena
// introducción al tema.

package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {

	// `s` es una `cadena` a la que se le asigna un valor literal
	// que representa la palabra "hola" en el idioma tailandés.
	// Los literales de cadena de Go son texto codificado en UTF-8.
	const s = "สวัสดี"

	// Dado que las cadenas son equivalentes a `[]byte`, esto
	// producirá la longitud de los bytes crudos almacenados dentro.
	fmt.Println("Longitud:", len(s))

	// La indexación en una cadena produce los valores de byte crudos en
	// cada índice. Este bucle genera los valores hexadecimales de todos
	// los bytes que constituyen los puntos de código en `s`.
	for i := 0; i < len(s); i++ {
		fmt.Printf("%x ", s[i])
	}
	fmt.Println()

	// Para contar cuántas _runas_ hay en una cadena, podemos usar
	// el paquete `utf8`. Tenga en cuenta que el tiempo de ejecución de
	// `RuneCountInString` depende del tamaño de la cadena,
	// porque tiene que decodificar cada runa UTF-8 secuencialmente.
	// Algunos caracteres tailandeses se representan por múltiples
	// puntos de código UTF-8, por lo que el resultado de esta cuenta puede ser sorprendente.
	fmt.Println("Número de runas:", utf8.RuneCountInString(s))

	// Un bucle `range` maneja las cadenas de manera especial y decodifica
	// cada `runa` junto con su desplazamiento en la cadena.
	for idx, runeValue := range s {
		fmt.Printf("%#U comienza en %d\n", runeValue, idx)
	}

	// Podemos lograr la misma iteración utilizando la
	// función `utf8.DecodeRuneInString` explícitamente.
	fmt.Println("\nUsando DecodeRuneInString")
	for i, w := 0, 0; i < len(s); i += w {
		runeValue, width := utf8.DecodeRuneInString(s[i:])
		fmt.Printf("%#U comienza en %d\n", runeValue, i)
		w = width

		// Esto demuestra pasar un valor de `runa` a una función.
		examineRune(runeValue)
	}
}

func examineRune(r rune) {

	// Los valores encerrados entre comillas simples son _literales de runa_.
	// Podemos comparar un valor de `runa` con un literal de runa directamente.
	if r == 't' {
		fmt.Println("encontrado tee")
	} else if r == 'ส' {
		fmt.Println("encontrado so sua")
	}
}

```
