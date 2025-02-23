# Директории

Создайте Go-программу, которая создает новую поддиректорию в текущей рабочей директории, создает иерархию директорий, включая родительские, перечисляет содержимое директории, изменяет текущую рабочую директорию и рекурсивно обходит директорию.

- Создайте новую поддиректорию в текущей рабочей директории.
- При создании временных директорий хорошей практикой является использование `defer` для их удаления. `os.RemoveAll` удалит всю деревушку директорий (аналог `rm -rf`).
- Создайте иерархию директорий, включая родительские, с использованием `MkdirAll`. Это аналогично команде `mkdir -p` в командной строке.
- `ReadDir` перечисляет содержимое директории, возвращая срез объектов `os.DirEntry`.
- `Chdir` позволяет изменить текущую рабочую директорию, аналогично команде `cd`.
- Рекурсивно обойдите директорию, включая все ее поддиректории. `Walk` принимает обратную функцию для обработки каждого посещенного файла или директории.

```sh
$ go run directories.go
Listing subdir/parent
child true
file2 false
file3 false
Listing subdir/parent/child
file4 false
Visiting subdir
subdir true
subdir/file1 false
subdir/parent true
subdir/parent/child true
subdir/parent/child/file4 false
subdir/parent/file2 false
subdir/parent/file3 false
```

Ниже представлен полный код:

```go
// Go имеет несколько полезных функций для работы с
// *директориями* в файловой системе.

package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func check(e error) {
	if e!= nil {
		panic(e)
	}
}

func main() {

	// Создайте новую поддиректорию в текущей рабочей
	// директории.
	err := os.Mkdir("subdir", 0755)
	check(err)

	// При создании временных директорий хорошей практикой является использование `defer` для их удаления. `os.RemoveAll` удалит всю деревушку директорий (аналог `rm -rf`).
	defer os.RemoveAll("subdir")

	// Вспомогательная функция для создания нового пустого файла.
	createEmptyFile := func(name string) {
		d := []byte("")
		check(os.WriteFile(name, d, 0644))
	}

	createEmptyFile("subdir/file1")

	// Мы можем создать иерархию директорий, включая
	// родительские, с использованием `MkdirAll`. Это аналогично команде `mkdir -p` в командной строке.
	err = os.MkdirAll("subdir/parent/child", 0755)
	check(err)

	createEmptyFile("subdir/parent/file2")
	createEmptyFile("subdir/parent/file3")
	createEmptyFile("subdir/parent/child/file4")

	// `ReadDir` перечисляет содержимое директории, возвращая срез объектов `os.DirEntry`.
	c, err := os.ReadDir("subdir/parent")
	check(err)

	fmt.Println("Listing subdir/parent")
	for _, entry := range c {
		fmt.Println(" ", entry.Name(), entry.IsDir())
	}

	// `Chdir` позволяет изменить текущую рабочую директорию, аналогично команде `cd`.
	err = os.Chdir("subdir/parent/child")
	check(err)

	// Теперь мы увидим содержимое `subdir/parent/child` при перечислении *текущей* директории.
	c, err = os.ReadDir(".")
	check(err)

	fmt.Println("Listing subdir/parent/child")
	for _, entry := range c {
		fmt.Println(" ", entry.Name(), entry.IsDir())
	}

	// `cd` назад, где мы начали.
	err = os.Chdir("../../..")
	check(err)

	// Мы также можем рекурсивно обойти директорию, включая все ее поддиректории. `Walk` принимает обратную функцию для обработки каждого посещенного файла или директории.
	fmt.Println("Visiting subdir")
	err = filepath.Walk("subdir", visit)
}

// `visit` вызывается для каждого найденного файла или директории при рекурсивном обходе с использованием `filepath.Walk`.
func visit(p string, info os.FileInfo, err error) error {
	if err!= nil {
		return err
	}
	fmt.Println(" ", p, info.IsDir())
	return nil
}

```
