# Switch

В этом практическом задании вам нужно завершить оператор `switch`, чтобы вывести соответствующее сообщение в зависимости от входного значения.

- Для решения задачи необходимо использовать оператор `switch`.
- В `default` блоке необходимо обрабатывать неожиданные входные значения.

```sh
$ go run switch.go
Write 2 as two
It's a weekday
It's after noon
I'm a bool
I'm an int
Don't know type string

```

Ниже представлен полный код:

```go
// Оператор `switch` позволяет выражать условия для многих
// ветвей.

package main

import (
	"fmt"
	"time"
)

func main() {

	// Вот простой `switch`.
	i := 2
	fmt.Print("Write ", i, " as ")
	switch i {
	case 1:
		fmt.Println("one")
	case 2:
		fmt.Println("two")
	case 3:
		fmt.Println("three")
	}

	// В одной инструкции `case` можно использовать запятые для
	// разделения нескольких выражений. В этом примере мы также
	// используем необязательный `default` блок.
	switch time.Now().Weekday() {
	case time.Saturday, time.Sunday:
		fmt.Println("It's the weekend")
	default:
		fmt.Println("It's a weekday")
	}

	// `switch` без выражения - это альтернативный способ
	// выражения if/else логики. Здесь мы также показываем, как
	// выражения `case` могут быть не константами.
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("It's before noon")
	default:
		fmt.Println("It's after noon")
	}

	// Типовой `switch` сравнивает типы, а не значения. Вы
	// можете использовать это, чтобы определить тип значения
	// интерфейса. В этом примере переменная `t` будет иметь
	// тип, соответствующий ее ветке.
	whatAmI := func(i interface{}) {
		switch t := i.(type) {
		case bool:
			fmt.Println("I'm a bool")
		case int:
			fmt.Println("I'm an int")
		default:
			fmt.Printf("Don't know type %T\n", t)
		}
	}
	whatAmI(true)
	whatAmI(1)
	whatAmI("hey")
}

```
