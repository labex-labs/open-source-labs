# Строковые функции

Завершите код ниже, чтобы вывести результат работы различных строковых функций, предоставляемых пакетом `strings`.

- Используйте пакет `strings` для завершения лабораторной работы.
- Используйте функцию `fmt.Println` для вывода результата.
- Не изменяйте имя функции или параметры.

```sh
$ go run string-functions.go
Contains: true
Count: 2
HasPrefix: true
HasSuffix: true
Index: 1
Join: a-b
Repeat: aaaaa
Replace: f00
Replace: f0o
Split: [a b c d e]
ToLower: test
ToUpper: TEST
```

Ниже представлен полный код:

```go
// Стандартная библиотека Go имеет пакет `strings`,
// который предоставляет множество полезных функций
// для работы со строками. Вот несколько примеров,
// чтобы дать представление о том, как этот пакет используется.

package main

import (
	"fmt"
	s "strings"
)

// Мы создаем псевдоним для `fmt.Println`, чтобы упростить
// его использование в дальнейшем.
var p = fmt.Println

func main() {

	// Вот пример некоторых функций, доступных в пакете `strings`.
	// Поскольку это функции пакета, а не методы на самой строке,
	// мы должны передавать строку, с которой работаем,
	// в качестве первого аргумента функции.
	// Вы можете найти больше функций в документации по пакету
	// [`strings`](https://pkg.go.dev/strings).
	p("Contains:  ", s.Contains("test", "es"))
	p("Count:     ", s.Count("test", "t"))
	p("HasPrefix: ", s.HasPrefix("test", "te"))
	p("HasSuffix: ", s.HasSuffix("test", "st"))
	p("Index:     ", s.Index("test", "e"))
	p("Join:      ", s.Join([]string{"a", "b"}, "-"))
	p("Repeat:    ", s.Repeat("a", 5))
	p("Replace:   ", s.Replace("foo", "o", "0", -1))
	p("Replace:   ", s.Replace("foo", "o", "0", 1))
	p("Split:     ", s.Split("a-b-c-d-e", "-"))
	p("ToLower:   ", s.ToLower("TEST"))
	p("ToUpper:   ", s.ToUpper("test"))
}

```
