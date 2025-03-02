# Panic

В данной лабораторной работе требуется использовать функцию `panic` для быстрого завершения программы при возникновении ошибок, которые не должны появляться в нормальной работе или которые вы не готовы обрабатывать优雅но.

- Основные знания языка программирования Golang.
- Ознакомленность с обработкой ошибок в Golang.
- Понимание функции `panic` в Golang.

```sh
# Запуск этой программы вызовет панику, выведет
# сообщение об ошибке и трассу горутин, а затем
# завершится с ненулевым статусом.

# Когда первый вызов `panic` в `main` срабатывает, программа
# завершается, не доходя до оставшейся части кода. Если вы
# хотите увидеть, как программа пытается создать временный файл,
# закомментируйте первый вызов `panic`.
$ go run panic.go
panic: a problem

goroutine 1 [running]:
main.main() /.../panic.go:12 +0x47
...
exit status 2

# Обратите внимание, что в отличие от некоторых языков, которые
# используют исключения для обработки многих ошибок, в Go
# по правилам лучше использовать возвращаемые значения с индикацией ошибок,
# когда это возможно.
```

Ниже представлен полный код:

```go
// `panic` обычно означает, что что-то пошло неожиданно
// не так. Большинство случаев использования этого - это быстрый
// выход из программы при ошибках, которые не должны появляться
// в нормальной работе или которые мы не готовы обрабатывать优雅но.

package main

import "os"

func main() {

	// Мы будем использовать `panic` на всем сайте для проверки
	// на неожиданные ошибки. Это единственная программа на сайте,
	// которая должна вызывать панику.
	panic("a problem")

	// Часто `panic` используется для аварийного завершения программы,
	// если функция возвращает ошибочное значение, которое мы не знаем,
	// как (или хотим) обработать. Вот пример вызова `panic`, если
	// при создании нового файла возникает непредвиденная ошибка.
	_, err := os.Create("/tmp/file")
	if err!= nil {
		panic(err)
	}
}

```
