# Неблокирующие операции с каналами

Задача, которую необходимо решить в этом лабораторном проекте, - это реализация неблокирующих операций с каналами с использованием оператора `select` с предложением `default`.

- Реализовать неблокирующее получение из канала с использованием оператора `select` с предложением `default`.
- Реализовать неблокирующую отправку в канал с использованием оператора `select` с предложением `default`.
- Реализовать многонаправленное неблокирующее ветвление с использованием оператора `select` с несколькими предложениями `case` и предложением `default`.

```sh
$ go run non-blocking-channel-operations.go
no message received
no message sent
no activity
```

Ниже представлен полный код:

```go
// Базовые отправки и получение из каналов блокирующие.
// Однако, мы можем использовать `select` с предложением `default` для
// реализации _неблокирующих_ отправок, получений и даже
// неблокирующих многонаправленных `select`.

package main

import "fmt"

func main() {
	messages := make(chan string)
	signals := make(chan bool)

	// Вот неблокирующее получение. Если значение доступно в `messages`,
	// то `select` будет использовать вариант `<-messages` с этим значением.
	// Если нет, то немедленно будет использоваться вариант `default`.
	select {
	case msg := <-messages:
		fmt.Println("received message", msg)
	default:
		fmt.Println("no message received")
	}

	// Неблокирующая отправка работает аналогично. Здесь `msg`
	// не может быть отправлено в канал `messages`, потому что
	// канал не имеет буфера и нет приемника.
	// Поэтому выбирается вариант `default`.
	msg := "hi"
	select {
	case messages <- msg:
		fmt.Println("sent message", msg)
	default:
		fmt.Println("no message sent")
	}

	// Мы можем использовать несколько вариантов `case` выше предложения `default`
	// для реализации многонаправленного неблокирующего ветвления.
	// Здесь мы пытаемся выполнить неблокирующие получение из обоих `messages` и `signals`.
	select {
	case msg := <-messages:
		fmt.Println("received message", msg)
	case sig := <-signals:
		fmt.Println("received signal", sig)
	default:
		fmt.Println("no activity")
	}
}

```
