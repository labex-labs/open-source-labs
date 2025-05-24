# 目录

创建一个 Go 程序，该程序在当前工作目录中创建一个新的子目录，创建一个包含父目录的目录层次结构，列出目录内容，更改当前工作目录，并递归访问一个目录。

- 在当前工作目录中创建一个新的子目录。
- 创建临时目录时，最好使用`defer`来删除它们。`os.RemoveAll`将删除整个目录树（类似于`rm -rf`）。
- 使用`MkdirAll`创建一个包含父目录的目录层次结构。这类似于命令行中的`mkdir -p`。
- `ReadDir`列出目录内容，返回一个`os.DirEntry`对象的切片。
- `Chdir`允许我们更改当前工作目录，类似于`cd`。
- 递归访问一个目录，包括其所有子目录。`Walk`接受一个回调函数来处理访问的每个文件或目录。

```sh
$ go run directories.go
列出 subdir/parent
child true
file2 false
file3 false
列出 subdir/parent/child
file4 false
访问 subdir
subdir true
subdir/file1 false
subdir/parent true
subdir/parent/child true
subdir/parent/child/file4 false
subdir/parent/file2 false
subdir/parent/file3 false
```

以下是完整代码：

```go
// Go 有几个用于处理文件系统中*目录*的实用函数。

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

	// 在当前工作目录中创建一个新的子目录。
	err := os.Mkdir("subdir", 0755)
	check(err)

	// 创建临时目录时，最好使用 `defer` 来删除它们。`os.RemoveAll`
	// 将删除整个目录树（类似于`rm -rf`）。
	defer os.RemoveAll("subdir")

	// 创建一个新的空文件的辅助函数。
	createEmptyFile := func(name string) {
		d := []byte("")
		check(os.WriteFile(name, d, 0644))
	}

	createEmptyFile("subdir/file1")

	// 我们可以使用 `MkdirAll` 创建一个包含父目录的目录层次结构。这类似于
	// 命令行中的`mkdir -p`。
	err = os.MkdirAll("subdir/parent/child", 0755)
	check(err)

	createEmptyFile("subdir/parent/file2")
	createEmptyFile("subdir/parent/file3")
	createEmptyFile("subdir/parent/child/file4")

	// `ReadDir` 列出目录内容，返回一个 `os.DirEntry` 对象的切片。
	c, err := os.ReadDir("subdir/parent")
	check(err)

	fmt.Println("列出 subdir/parent")
	for _, entry := range c {
		fmt.Println(" ", entry.Name(), entry.IsDir())
	}

	// `Chdir` 允许我们更改当前工作目录，类似于 `cd`。
	err = os.Chdir("subdir/parent/child")
	check(err)

	// 现在，当列出*当前*目录时，我们将看到 `subdir/parent/child` 的内容。
	c, err = os.ReadDir(".")
	check(err)

	fmt.Println("列出 subdir/parent/child")
	for _, entry := range c {
		fmt.Println(" ", entry.Name(), entry.IsDir())
	}

	// `cd` 回到我们开始的地方。
	err = os.Chdir("../../..")
	check(err)

	// 我们还可以递归访问一个目录，包括其所有子目录。`Walk` 接受
	// 一个回调函数来处理访问的每个文件或目录。
	fmt.Println("访问 subdir")
	err = filepath.Walk("subdir", visit)
}

// `visit` 由 `filepath.Walk` 递归找到的每个文件或目录调用。
func visit(p string, info os.FileInfo, err error) error {
	if err!= nil {
		return err
	}
	fmt.Println(" ", p, info.IsDir())
	return nil
}

```
