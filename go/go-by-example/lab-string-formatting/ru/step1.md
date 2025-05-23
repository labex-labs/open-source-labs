# Форматирование строк

Вам необходимо форматировать различные типы данных, используя различные форматирующие глаголы в Golang.

- Вы должны использовать пакет `fmt` для форматирования данных.
- Вы должны использовать правильный форматирующий глагол для каждого типа данных.
- Вы должны уметь форматировать целые числа, числа с плавающей точкой, строки и структуры (structs).
- Вы должны уметь контролировать ширину и точность вывода.
- Вы должны уметь выравнивать вывод по левому или правому краю.

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

Ниже представлен полный код:

```go
// Go offers excellent support for string formatting in
// the `printf` tradition. Here are some examples of
// common string formatting tasks.

package main

import (
	"fmt"
	"os"
)

type point struct {
	x, y int
}

func main() {

	// Go offers several printing "verbs" designed to
	// format general Go values. For example, this prints
	// an instance of our `point` struct.
	p := point{1, 2}
	fmt.Printf("struct1: %v\n", p)

	// If the value is a struct, the `%+v` variant will
	// include the struct's field names.
	fmt.Printf("struct2: %+v\n", p)

	// The `%#v` variant prints a Go syntax representation
	// of the value, i.e. the source code snippet that
	// would produce that value.
	fmt.Printf("struct3: %#v\n", p)

	// To print the type of a value, use `%T`.
	fmt.Printf("type: %T\n", p)

	// Formatting booleans is straight-forward.
	fmt.Printf("bool: %t\n", true)

	// There are many options for formatting integers.
	// Use `%d` for standard, base-10 formatting.
	fmt.Printf("int: %d\n", 123)

	// This prints a binary representation.
	fmt.Printf("bin: %b\n", 14)

	// This prints the character corresponding to the
	// given integer.
	fmt.Printf("char: %c\n", 33)

	// `%x` provides hex encoding.
	fmt.Printf("hex: %x\n", 456)

	// There are also several formatting options for
	// floats. For basic decimal formatting use `%f`.
	fmt.Printf("float1: %f\n", 78.9)

	// `%e` and `%E` format the float in (slightly
	// different versions of) scientific notation.
	fmt.Printf("float2: %e\n", 123400000.0)
	fmt.Printf("float3: %E\n", 123400000.0)

	// For basic string printing use `%s`.
	fmt.Printf("str1: %s\n", "\"string\"")

	// To double-quote strings as in Go source, use `%q`.
	fmt.Printf("str2: %q\n", "\"string\"")

	// As with integers seen earlier, `%x` renders
	// the string in base-16, with two output characters
	// per byte of input.
	fmt.Printf("str3: %x\n", "hex this")

	// To print a representation of a pointer, use `%p`.
	fmt.Printf("pointer: %p\n", &p)

	// When formatting numbers you will often want to
	// control the width and precision of the resulting
	// figure. To specify the width of an integer, use a
	// number after the `%` in the verb. By default the
	// result will be right-justified and padded with
	// spaces.
	fmt.Printf("width1: |%6d|%6d|\n", 12, 345)

	// You can also specify the width of printed floats,
	// though usually you'll also want to restrict the
	// decimal precision at the same time with the
	// width.precision syntax.
	fmt.Printf("width2: |%6.2f|%6.2f|\n", 1.2, 3.45)

	// To left-justify, use the `-` flag.
	fmt.Printf("width3: |%-6.2f|%-6.2f|\n", 1.2, 3.45)

	// You may also want to control width when formatting
	// strings, especially to ensure that they align in
	// table-like output. For basic right-justified width.
	fmt.Printf("width4: |%6s|%6s|\n", "foo", "b")

	// To left-justify use the `-` flag as with numbers.
	fmt.Printf("width5: |%-6s|%-6s|\n", "foo", "b")

	// So far we've seen `Printf`, which prints the
	// formatted string to `os.Stdout`. `Sprintf` formats
	// and returns a string without printing it anywhere.
	s := fmt.Sprintf("sprintf: a %s", "string")
	fmt.Println(s)

	// You can format+print to `io.Writers` other than
	// `os.Stdout` using `Fprintf`.
	fmt.Fprintf(os.Stderr, "io: an %s\n", "error")
}

```
