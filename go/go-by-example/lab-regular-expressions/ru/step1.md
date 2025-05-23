# Регулярные выражения

В этом практическом занятии требуется завершить код для выполнения различных задач, связанных с регулярными выражениями, в Golang.

- Используйте пакет `regexp` для выполнения задач, связанных с регулярными выражениями.
- Используйте `MatchString`, чтобы проверить, соответствует ли строка шаблону.
- Используйте `Compile`, чтобы оптимизировать структуру `Regexp`.
- Используйте `MatchString`, чтобы проверить соответствие, как `Compile`.
- Используйте `FindString`, чтобы найти соответствие для регулярного выражения.
- Используйте `FindStringIndex`, чтобы найти первое соответствие и вернуть индексы начала и конца соответствия вместо совпадающего текста.
- Используйте `FindStringSubmatch`, чтобы вернуть информацию для обоих `p([a-z]+)ch` и `([a-z]+)`.
- Используйте `FindStringSubmatchIndex`, чтобы вернуть информацию о индексах совпадений и подсовпадений.
- Используйте `FindAllString`, чтобы найти все совпадения для регулярного выражения.
- Используйте `FindAllStringSubmatchIndex`, чтобы применить к всем совпадениям в вводе, а не только к первому.
- Используйте `Match`, чтобы проверить соответствие с аргументами `[]byte` и убрать `String` из имени функции.
- Используйте `MustCompile`, чтобы создать глобальные переменные с регулярными выражениями.
- Используйте `ReplaceAllString`, чтобы заменить подмножества строк на другие значения.
- Используйте `ReplaceAllFunc`, чтобы преобразовать совпадающий текст с помощью заданной функции.

```sh
# Для получения полного справочника по регулярным выражениям в Go проверьте
# документацию по пакету [`regexp`](https://pkg.go.dev/regexp).
```

Ниже представлен полный код:

```go
// Go предоставляет встроенную поддержку для [регулярных выражений](https://en.wikipedia.org/wiki/Regular_expression).
// Вот некоторые примеры распространенных задач, связанных с регулярными выражениями
// в Go.

package main

import (
	"bytes"
	"fmt"
	"regexp"
)

func main() {

	// Это проверяет, соответствует ли строка шаблону.
	match, _ := regexp.MatchString("p([a-z]+)ch", "peach")
	fmt.Println(match)

	// Выше мы напрямую использовали строковый шаблон, но для
	// других задач с регулярными выражениями вам понадобится `Compile`
	// оптимизированную структуру `Regexp`.
	r, _ := regexp.Compile("p([a-z]+)ch")

	// На этих структурах доступно много методов. Вот
	// тест соответствия, как мы видели ранее.
	fmt.Println(r.MatchString("peach"))

	// Это находит соответствие для регулярного выражения.
	fmt.Println(r.FindString("peach punch"))

	// Это также находит первое соответствие, но возвращает
	// индексы начала и конца соответствия вместо
	// совпадающего текста.
	fmt.Println("idx:", r.FindStringIndex("peach punch"))

	// Варианты `Submatch` включают информацию о
	// совпадениях по всему шаблону и подсовпадениях
	// внутри этих совпадений. Например, это вернет
	// информацию для обоих `p([a-z]+)ch` и `([a-z]+)`.
	fmt.Println(r.FindStringSubmatch("peach punch"))

	// Аналогично это вернет информацию о
	// индексах совпадений и подсовпадений.
	fmt.Println(r.FindStringSubmatchIndex("peach punch"))

	// Варианты `All` этих функций применяются ко всем
	// совпадениям в вводе, а не только к первому. Например, чтобы найти все совпадения для регулярного выражения.
	fmt.Println(r.FindAllString("peach punch pinch", -1))

	// Эти варианты `All` также доступны для других
	// функций, которые мы видели выше.
	fmt.Println("all:", r.FindAllStringSubmatchIndex(
		"peach punch pinch", -1))

	// Передача неотрицательного целого числа в качестве второго
	// аргумента для этих функций ограничивает количество
	// совпадений.
	fmt.Println(r.FindAllString("peach punch pinch", 2))

	// Наши примеры выше имели строковые аргументы и использовали
	// имена, такие как `MatchString`. Мы также можем передать
	// аргументы `[]byte` и убрать `String` из имени функции.
	fmt.Println(r.Match([]byte("peach")))

	// При создании глобальных переменных с регулярными
	// выражениями вы можете использовать вариант `MustCompile`
	// от `Compile`. `MustCompile` завершает работу с ошибкой вместо
	// возврата ошибки, что делает его безопаснее для использования
	// в глобальных переменных.
	r = regexp.MustCompile("p([a-z]+)ch")
	fmt.Println("regexp:", r)

	// Пакет `regexp` также можно использовать для замены
	// подмножеств строк на другие значения.
	fmt.Println(r.ReplaceAllString("a peach", "<fruit>"))

	// Вариант `Func` позволяет преобразовать совпадающий
	// текст с помощью заданной функции.
	in := []byte("a peach")
	out := r.ReplaceAllFunc(in, bytes.ToUpper)
	fmt.Println(string(out))
}

```
