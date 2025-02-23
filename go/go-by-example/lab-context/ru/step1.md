# Контекст

Функция `hello` имитирует некоторую работу, выполняемую сервером, ожидая несколько секунд перед отправкой ответа клиенту. Во время работы следите за каналом `Done()` контекста на сигнал о том, что мы должны отменить работу и вернуться как можно скорее.

- Версия Golang 1.13 или выше.

```sh
# Запустите сервер в фоновом режиме.
$ go run context-in-http-servers.go &

# Имитируйте запрос клиента к `/hello`, нажав
# Ctrl+C вскоре после запуска для сигнализации
# отмены.
$ curl localhost:8090/hello
server: hello handler started
^C
server: context canceled
server: hello handler ended
```

Ниже представлен полный код:

```go
// В предыдущем примере мы рассматривали настройку простого
// [HTTP-сервера](http-servers). HTTP-сервера полезны для
// демонстрации использования `context.Context` для
// управления отменой. `Context` переносит даты окончания,
// сигналы отмены и другие значения, относящиеся к запросу,
// через границы API и goroutine.
package main

import (
	"fmt"
	"net/http"
	"time"
)

func hello(w http.ResponseWriter, req *http.Request) {

	// `context.Context` создается для каждого запроса
	// механизмом `net/http` и доступен с помощью
	// метода `Context()`.
	ctx := req.Context()
	fmt.Println("server: hello handler started")
	defer fmt.Println("server: hello handler ended")

	// Подождите несколько секунд перед отправкой ответа
	// клиенту. Это может имитировать некоторую работу,
	// выполняемую сервером. Во время работы следите за
	// каналом `Done()` контекста на сигнал о том, что мы
	// должны отменить работу и вернуться как можно скорее.
	select {
	case <-time.After(10 * time.Second):
		fmt.Fprintf(w, "hello\n")
	case <-ctx.Done():
		// Метод `Err()` контекста возвращает ошибку,
		// которая объясняет, почему канал `Done()` был
		// закрыт.
		err := ctx.Err()
		fmt.Println("server:", err)
		internalError := http.StatusInternalServerError
		http.Error(w, err.Error(), internalError)
	}
}

func main() {

	// Как и раньше, мы регистрируем наш обработчик на
	// маршруте "/hello" и начинаем обслуживание.
	http.HandleFunc("/hello", hello)
	http.ListenAndServe(":8090", nil)
}

```
