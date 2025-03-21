# Несколько возвращаемых значений

Завершите функцию `swap`, чтобы она возвращала два входных параметра в обратном порядке.

- Функция `swap` должна принимать два целых числа в качестве входных параметров.
- Функция `swap` должна возвращать два целых числа в обратном порядке.

```sh
$ go run multiple-return-values.go
3
7
7

# Прием переменного количества аргументов - это еще одна полезная
# особенность функций Go; рассмотрим ее далее.
```

Ниже представлен полный код:

```go
// Go имеет встроенную поддержку для _нескольких возвращаемых значений_.
// Эта особенность часто используется в идиоматическом Go, например,
// чтобы возвращать как результат, так и значения ошибок из функции.

package main

import "fmt"

// `(int, int)` в сигнатуре этой функции показывает, что
// функция возвращает 2 целых числа (`int`).
func vals() (int, int) {
	return 3, 7
}

func main() {

	// Здесь мы используем 2 различных возвращаемых значения из
	// вызова с _множественным присваиванием_.
	a, b := vals()
	fmt.Println(a)
	fmt.Println(b)

	// Если вам нужны только некоторые возвращаемые значения,
	// используйте пустой идентификатор `_`.
	_, c := vals()
	fmt.Println(c)
}

```
