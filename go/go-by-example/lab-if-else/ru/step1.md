# if-else

Требуется реализовать функцию `checkNumber`, которая принимает целое число в качестве входных данных и возвращает строку. Если число четное, возвращается "even", в противном случае возвращается "odd".

- Функция должна называться `checkNumber`.
- Функция должна принимать целое число в качестве входных данных.
- Функция должна возвращать строку.
- Если число четное, возвращается "even".
- Если число нечетное, возвращается "odd".

```sh
$ go run if-else.go
7 is odd
8 is divisible by 4
9 has 1 digit

# В Go нет [тернарного if](https://en.wikipedia.org/wiki/%3F:),
# поэтому для базовых условий вам нужно использовать полный `if` statement.
```

Ниже представлен полный код:

```go
// Ветвление с использованием `if` и `else` в Go
// простое.

package main

import "fmt"

func main() {

	// Вот базовый пример.
	if 7%2 == 0 {
		fmt.Println("7 is even")
	} else {
		fmt.Println("7 is odd")
	}

	// Можно использовать `if` statement без `else`.
	if 8%4 == 0 {
		fmt.Println("8 is divisible by 4")
	}

	// Перед условными операторами может быть любая инструкция; любые переменные,
	// объявленные в этой инструкции, доступны в текущем и всех последующих ветвях.
	if num := 9; num < 0 {
		fmt.Println(num, "is negative")
	} else if num < 10 {
		fmt.Println(num, "has 1 digit")
	} else {
		fmt.Println(num, "has multiple digits")
	}
}

// Обратите внимание, что в Go не нужно использовать скобки вокруг условий,
// но фигурные скобки обязательны.

```
