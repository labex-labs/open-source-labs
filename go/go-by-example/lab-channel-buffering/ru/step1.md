# Буферизация каналов

По умолчанию каналы в Golang не буферизированы, что означает, что они принимают отправку (`chan <-`), только если есть соответствующее получение (`<- chan`), готовое принять отправленное значение. Однако, буферизированные каналы могут принимать ограниченное количество значений без соответствующего приемника для этих значений. В этом лабораторном проекте вам нужно создать буферизированный канал и отправить в него значения без соответствующего параллельного приема.

- Основы знаний о каналах в Golang
- Понимание буферизированных каналов

```sh
$ go run channel-buffering.go
буферизированный
канал
```

Ниже представлен полный код:

```go
// По умолчанию каналы _не буферизированы_, что означает, что они
// будут принимать отправку (`chan <-`), только если есть
// соответствующее получение (`<- chan`), готовое принять
// отправленное значение. _Буферизированные каналы_ могут принимать
// ограниченное количество значений без соответствующего приемника
// для этих значений.

package main

import "fmt"

func main() {

	// Здесь мы `make` канал строк, буферизирующий до
	// 2 значений.
	messages := make(chan string, 2)

	// Поскольку этот канал буферизирован, мы можем отправить эти
	// значения в канал без соответствующего параллельного приема.
	messages <- "буферизированный"
	messages <- "канал"

	// Позже мы можем получить эти два значения, как обычно.
	fmt.Println(<-messages)
	fmt.Println(<-messages)
}

```
