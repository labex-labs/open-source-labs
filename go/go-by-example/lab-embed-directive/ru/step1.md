# Директива embed

Ваша задача - модифицировать заданный код для встраивания файлов и папок в Go-бинарник и вывода их содержимого.

- Вы должны использовать пакет `embed` для встраивания файлов и папок.
- Вы должны использовать типы `string` и `[]byte` для хранения содержимого встроенных файлов.
- Вы должны использовать тип `embed.FS` для встраивания нескольких файлов или папок с использованием подстановочных знаков.
- Вы должны вывести содержимое встроенных файлов.

```sh
# Используйте эти команды для запуска примера.
# (Примечание: из-за ограничений в Go Playground,
# этот пример можно запустить только на локальной машине.)
$ mkdir -p folder
$ echo "hello go" > folder/single_file.txt
$ echo "123" > folder/file1.hash
$ echo "456" > folder/file2.hash

$ go run embed-directive.go
hello go
hello go
123
456
```

Ниже представлен полный код:

```go
// `//go:embed` - это [директива компилятора](https://pkg.go.dev/cmd/compile#hdr-Compiler_Directives),
// которая позволяет программам включать произвольные файлы и папки в Go-бинарник
// во время сборки. Подробнее о директиве embed можно прочитать
// [здесь](https://pkg.go.dev/embed).
package main

// Импортируем пакет `embed`; если вы не используете никаких экспортированных
// идентификаторов из этого пакета, вы можете сделать пустой импорт с `_ "embed"`.
import (
	"embed"
)

// Директива `embed` принимает пути относительно директории, содержащей
// исходный файл Go. Эта директив встраивает содержимое файла в переменную
// `string`, которая непосредственно следует за ней.
//
//go:embed folder/single_file.txt
var fileString string

// Или вставьте содержимое файла в `[]byte`.
//
//go:embed folder/single_file.txt
var fileByte []byte

// Мы также можем встроить несколько файлов или даже папки с использованием
// подстановочных знаков. Для этого используется переменная типа [embed.FS](https://pkg.go.dev/embed#FS),
// которая реализует простую виртуальную файловую систему.
//
//go:embed folder/single_file.txt
//go:embed folder/*.hash
var folder embed.FS

func main() {

	// Выведите содержимое `single_file.txt`.
	print(fileString)
	print(string(fileByte))

	// Извлеките некоторые файлы из встроенной папки.
	content1, _ := folder.ReadFile("folder/file1.hash")
	print(string(content1))

	content2, _ := folder.ReadFile("folder/file2.hash")
	print(string(content2))
}

```
