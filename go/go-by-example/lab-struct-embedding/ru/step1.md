# Встраивание структур

Создайте структуру под названием `container`, которая встраивает структуру под названием `base`. Структура `base` должна иметь поле `num` типа `int` и метод `describe()`, который возвращает строку. Структура `container` должна иметь поле `str` типа `string`. Структура `container` должна быть способна обращаться к полю `num` и методу `describe()` структуры `base`.

- Структура `base` должна иметь поле `num` типа `int`.
- Структура `base` должна иметь метод `describe()`, который возвращает строку.
- Структура `container` должна иметь поле `str` типа `string`.
- Структура `container` должна встраивать структуру `base`.
- Структура `container` должна быть способна обращаться к полю `num` и методу `describe()` структуры `base`.

```sh
$ go run struct-embedding.go
co={num: 1, str: some name}
also num: 1
describe: base with num=1
describer: base with num=1
```

Ниже представлен полный код:

```go
// Go поддерживает _встраивание_ структур и интерфейсов
// для более无缝ного _композирования_ типов.
// Это не должно путаться с [`//go:embed`](embed-directive), который
// является директивой Go, введенной в Go версии 1.16+ для встраивания
// файлов и папок в бинарный файл приложения.

package main

import "fmt"

type base struct {
	num int
}

func (b base) describe() string {
	return fmt.Sprintf("base with num=%v", b.num)
}

// Структура `container` _встраивает_ структуру `base`. Встраивание выглядит
// как поле без имени.
type container struct {
	base
	str string
}

func main() {

	// При создании структур с помощью литералов мы должны
	// явно инициализировать встраивание; здесь
	// встроенный тип служит именем поля.
	co := container{
		base: base{
			num: 1,
		},
		str: "some name",
	}

	// Мы можем напрямую обращаться к полям `base` на `co`,
	// например, `co.num`.
	fmt.Printf("co={num: %v, str: %v}\n", co.num, co.str)

	// Альтернативно, мы можем указать полный путь, используя
	// имя встроенного типа.
	fmt.Println("also num:", co.base.num)

	// Поскольку `container` встраивает `base`, методы
	// `base` также становятся методами `container`. Здесь
	// мы вызываем метод, встроенный из `base`,
	// напрямую на `co`.
	fmt.Println("describe:", co.describe())

	type describer interface {
		describe() string
	}

	// Встраивание структур с методами может использоваться для предоставления
	// реализаций интерфейсов другим структурам. Здесь
	// мы видим, что структура `container` теперь реализует
	// интерфейс `describer`, потому что она встраивает `base`.
	var d describer = co
	fmt.Println("describer:", d.describe())
}

```
