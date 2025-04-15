# Expresiones regulares

Esta práctica requiere que completes el código para realizar varias tareas relacionadas con expresiones regulares en Golang.

- Utiliza el paquete `regexp` para realizar tareas relacionadas con expresiones regulares.
- Utiliza `MatchString` para probar si un patrón coincide con una cadena.
- Utiliza `Compile` para optimizar una estructura `Regexp`.
- Utiliza `MatchString` para probar una coincidencia como `Compile`.
- Utiliza `FindString` para encontrar la coincidencia de la expresión regular.
- Utiliza `FindStringIndex` para encontrar la primera coincidencia y devolver los índices de inicio y fin de la coincidencia en lugar del texto coincidente.
- Utiliza `FindStringSubmatch` para devolver información tanto para `p([a-z]+)ch` como para `([a-z]+)`.
- Utiliza `FindStringSubmatchIndex` para devolver información sobre los índices de coincidencias y subcoincidencias.
- Utiliza `FindAllString` para encontrar todas las coincidencias de una expresión regular.
- Utiliza `FindAllStringSubmatchIndex` para aplicarse a todas las coincidencias en la entrada, no solo a la primera.
- Utiliza `Match` para probar una coincidencia con argumentos de `[]byte` y eliminar `String` del nombre de la función.
- Utiliza `MustCompile` para crear variables globales con expresiones regulares.
- Utiliza `ReplaceAllString` para reemplazar subconjuntos de cadenas con otros valores.
- Utiliza `ReplaceAllFunc` para transformar el texto coincidente con una función dada.

```sh
# Para una referencia completa sobre las expresiones regulares de Go, consulte
# la documentación del paquete [`regexp`](https://pkg.go.dev/regexp).
```

A continuación está el código completo:

```go
// Go ofrece soporte integrado para [expresiones regulares](https://en.wikipedia.org/wiki/Regular_expression).
// Aquí hay algunos ejemplos de tareas comunes relacionadas con expresiones regulares
// en Go.

package main

import (
	"bytes"
	"fmt"
	"regexp"
)

func main() {

	// Esto prueba si un patrón coincide con una cadena.
	match, _ := regexp.MatchString("p([a-z]+)ch", "peach")
	fmt.Println(match)

	// Anteriormente usamos un patrón de cadena directamente, pero para
	// otras tareas de expresiones regulares necesitarás `Compilar` una
	// estructura `Regexp` optimizada.
	r, _ := regexp.Compile("p([a-z]+)ch")

	// Hay muchos métodos disponibles en estas estructuras. Aquí hay
	// una prueba de coincidencia como la que vimos anteriormente.
	fmt.Println(r.MatchString("peach"))

	// Esto encuentra la coincidencia de la expresión regular.
	fmt.Println(r.FindString("peach punch"))

	// Esto también encuentra la primera coincidencia pero devuelve los
	// índices de inicio y fin de la coincidencia en lugar del
	// texto coincidente.
	fmt.Println("idx:", r.FindStringIndex("peach punch"))

	// Las variantes `Submatch` incluyen información tanto sobre
	// las coincidencias de todo el patrón como sobre las subcoincidencias
	// dentro de esas coincidencias. Por ejemplo, esto devolverá
	// información tanto para `p([a-z]+)ch` como para `([a-z]+)`.
	fmt.Println(r.FindStringSubmatch("peach punch"))

	// Del mismo modo, esto devolverá información sobre los
	// índices de coincidencias y subcoincidencias.
	fmt.Println(r.FindStringSubmatchIndex("peach punch"))

	// Las variantes `All` de estas funciones se aplican a todas
	// las coincidencias en la entrada, no solo a la primera. Por
	// ejemplo, para encontrar todas las coincidencias de una expresión regular.
	fmt.Println(r.FindAllString("peach punch pinch", -1))

	// Estas variantes `All` también están disponibles para las otras
	// funciones que vimos anteriormente.
	fmt.Println("all:", r.FindAllStringSubmatchIndex(
		"peach punch pinch", -1))

	// Proporcionar un entero no negativo como segundo
	// argumento a estas funciones limitará el número
	// de coincidencias.
	fmt.Println(r.FindAllString("peach punch pinch", 2))

	// Nuestros ejemplos anteriores tenían argumentos de cadena y usaban
	// nombres como `MatchString`. También podemos proporcionar
	// argumentos de `[]byte` y eliminar `String` del
	// nombre de la función.
	fmt.Println(r.Match([]byte("peach")))

	// Al crear variables globales con expresiones regulares, puedes usar la variación
	// `MustCompile` de `Compile`. `MustCompile` produce un error en lugar de
	// devolver un error, lo que la hace más segura de usar para
	// variables globales.
	r = regexp.MustCompile("p([a-z]+)ch")
	fmt.Println("regexp:", r)

	// El paquete `regexp` también se puede usar para reemplazar
	// subconjuntos de cadenas con otros valores.
	fmt.Println(r.ReplaceAllString("a peach", "<fruit>"))

	// La variante `Func` te permite transformar el texto coincidente
	// con una función dada.
	in := []byte("a peach")
	out := r.ReplaceAllFunc(in, bytes.ToUpper)
	fmt.Println(string(out))
}

```
