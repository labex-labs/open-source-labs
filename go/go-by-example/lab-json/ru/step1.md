# JSON

Вам нужно завершить предоставленный код для кодирования и декодирования JSON-данных в Golang. Код содержит примеры кодирования и декодирования базовых типов данных, а также пользовательских типов данных.

- Основы программирования на языке Golang.
- Знание кодирования и декодирования JSON-данных в Golang.
- Способность читать и понимать существующий код на Golang.

```sh
# Здесь мы рассмотрели основы JSON в Go, но ознакомьтесь
# с статьёй [JSON and Go](https://go.dev/blog/json)
# и документацией по пакету [JSON](https://pkg.go.dev/encoding/json)
# для получения дополнительной информации.
```

Ниже представлен полный код:

```go
// Go предоставляет встроенную поддержку для кодирования и
// декодирования JSON, включая преобразование встроенных и
// пользовательских типов данных.

package main

import (
	"encoding/json"
	"fmt"
	"os"
)

// Мы будем использовать эти два struct для демонстрации
// кодирования и декодирования пользовательских типов ниже.
type response1 struct {
	Page   int
	Fruits []string
}

// Только экспортированные поля будут кодированы/декодированы
// в JSON. Поля должны начинаться с заглавной буквы, чтобы
// быть экспортируемыми.
type response2 struct {
	Page   int      `json:"page"`
	Fruits []string `json:"fruits"`
}

func main() {

	// Во - первых, рассмотрим кодирование базовых типов данных
	// в JSON - строки. Вот несколько примеров для атомарных
	// значений.
	bolB, _ := json.Marshal(true)
	fmt.Println(string(bolB))

	intB, _ := json.Marshal(1)
	fmt.Println(string(intB))

	fltB, _ := json.Marshal(2.34)
	fmt.Println(string(fltB))

	strB, _ := json.Marshal("gopher")
	fmt.Println(string(strB))

	// А вот несколько примеров для срезов и картежей, которые
	// кодируются в JSON - массивы и объекты, как можно ожидать.
	slcD := []string{"apple", "peach", "pear"}
	slcB, _ := json.Marshal(slcD)
	fmt.Println(string(slcB))

	mapD := map[string]int{"apple": 5, "lettuce": 7}
	mapB, _ := json.Marshal(mapD)
	fmt.Println(string(mapB))

	// Пакет JSON может автоматически кодировать ваши
	// пользовательские типы данных. Он будет включать только
	// экспортированные поля в закодированный вывод и по
	// умолчанию будет использовать эти имена в качестве
	// ключей JSON.
	res1D := &response1{
		Page:   1,
		Fruits: []string{"apple", "peach", "pear"}}
	res1B, _ := json.Marshal(res1D)
	fmt.Println(string(res1B))

	// Вы можете использовать теги при объявлении полей struct
	// для настройки имен ключей в закодированном JSON.
	// Проверьте определение `response2` выше, чтобы увидеть
	// пример таких тегов.
	res2D := &response2{
		Page:   1,
		Fruits: []string{"apple", "peach", "pear"}}
	res2B, _ := json.Marshal(res2D)
	fmt.Println(string(res2B))

	// Теперь рассмотрим декодирование JSON - данных в значения
	// Go. Вот пример для общего структуры данных.
	byt := []byte(`{"num":6.13,"strs":["a","b"]}`)

	// Мы должны предоставить переменную, в которую пакет JSON
	// сможет поместить декодированные данные. Эта
	// `map[string]interface{}` будет содержать карту строк
	// к произвольным типам данных.
	var dat map[string]interface{}

	// Вот само декодирование и проверка на связанные ошибки.
	if err := json.Unmarshal(byt, &dat); err!= nil {
		panic(err)
	}
	fmt.Println(dat)

	// Чтобы использовать значения в декодированной картеже,
	// нам нужно преобразовать их в соответствующий тип.
	// Например, здесь мы преобразуем значение в `num` в
	// ожидаемый тип `float64`.
	num := dat["num"].(float64)
	fmt.Println(num)

	// Доступ к вложенным данным требует серии
	// преобразований.
	strs := dat["strs"].([]interface{})
	str1 := strs[0].(string)
	fmt.Println(str1)

	// Мы также можем декодировать JSON в пользовательские типы
	// данных. Это имеет преимущество в том, что добавляет
	// дополнительную типизацию в наши программы и устраняет
	// необходимость в утверждениях типов при доступе к
	// декодированным данным.
	str := `{"page": 1, "fruits": ["apple", "peach"]}`
	res := response2{}
	json.Unmarshal([]byte(str), &res)
	fmt.Println(res)
	fmt.Println(res.Fruits[0])

	// В примерах выше мы всегда использовали байты и
	// строки в качестве промежуточных элементов между
	// данными и JSON - представлением на стандартном выводе.
	// Мы также можем потоково кодировать JSON непосредственно
	// в `os.Writer`'ы, такие как `os.Stdout`, или даже в
	// тело HTTP - ответа.
	enc := json.NewEncoder(os.Stdout)
	d := map[string]int{"apple": 5, "lettuce": 7}
	enc.Encode(d)
}

```
