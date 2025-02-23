# HTTP-клиент

Требуется написать программу, которая отправляет HTTP GET-запрос на сервер и выводит HTTP-ответный статус и первые 5 строк тела ответа.

- Программа должна использовать пакет `net/http` для отправки HTTP GET-запроса.
- Программа должна выводить HTTP-ответный статус.
- Программа должна выводить первые 5 строк тела ответа.
- Программа должна обрабатывать ошибки грамотно.

```sh
$ go run http-clients.go
Статус ответа: 200 OK
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Go by Example</title>

```

Ниже представлен полный код:

```go
// В стандартной библиотеке Go есть отличная поддержка
// для HTTP-клиентов и серверов в пакете `net/http`.
// В этом примере мы будем использовать его для отправки
// простых HTTP-запросов.
package main

import (
	"bufio"
	"fmt"
	"net/http"
)

func main() {

	// Отправить HTTP GET-запрос на сервер. `http.Get` - это
	// удобный способ вместо создания объекта `http.Client`
	// и вызова его метода `Get`; он использует объект
	// `http.DefaultClient`, который имеет полезные настройки
	// по умолчанию.
	resp, err := http.Get("https://gobyexample.com")
	if err!= nil {
		panic(err)
	}
	defer resp.Body.Close()

	// Вывести HTTP-ответный статус.
	fmt.Println("Статус ответа:", resp.Status)

	// Вывести первые 5 строк тела ответа.
	scanner := bufio.NewScanner(resp.Body)
	for i := 0; scanner.Scan() && i < 5; i++ {
		fmt.Println(scanner.Text())
	}

	if err := scanner.Err(); err!= nil {
		panic(err)
	}
}

```
