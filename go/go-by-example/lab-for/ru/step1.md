# `for`

Ниже приведенный код содержит различные виды циклов `for`. Однако некоторые части кода неполные, и вам нужно заполнить пропуски, чтобы код работал правильно.

- Основы синтаксиса Go
- Знание циклов `for` в Go

```sh
$ go run for.go
1
2
3
7
8
9
цикл
1
3
5

# Позже мы увидим другие формы цикла `for`, когда будем рассматривать
# операторы `range`, каналы и другие структуры данных.
```

Ниже представлен полный код:

```go
// `for` - единственная конструкция цикла в Go. Вот
// некоторые базовые виды циклов `for`.

package main

import "fmt"

func main() {

	// Самый базовый тип, с одним условием.
	i := 1
	for i <= 3 {
		fmt.Println(i)
		i = i + 1
	}

	// Классический цикл `for` с инициализацией/условием/действием после итерации.
	for j := 7; j <= 9; j++ {
		fmt.Println(j)
	}

	// `for` без условия будет повторяться
	// до тех пор, пока вы не выйдете из цикла с помощью `break` или не вернетесь из
	// окружающей функции.
	for {
		fmt.Println("цикл")
		break
	}

	// Также можно использовать `continue`, чтобы перейти к следующей итерации
	// цикла.
	for n := 0; n <= 5; n++ {
		if n%2 == 0 {
			continue
		}
		fmt.Println(n)
	}
}

```
