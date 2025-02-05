# 临时文件和目录

在这个实验中，你需要在Go语言中创建临时文件和目录。

- 使用 `os.CreateTemp` 创建临时文件。
- 使用 `os.MkdirTemp` 创建临时目录。
- 使用 `os.RemoveAll` 删除临时目录。
- 使用 `os.WriteFile` 向文件写入数据。

```sh
$ go run temporary-files-and-directories.go
临时文件名: /tmp/sample610887201
临时目录名: /tmp/sampledir898854668
```

以下是完整代码：

```go
// 在整个程序执行过程中，我们经常希望创建程序退出后就不再需要的数据。
// *临时文件和目录* 在这方面很有用，因为它们不会随着时间的推移而污染文件系统。

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

	// 创建临时文件最简单的方法是调用 `os.CreateTemp`。它会创建一个文件并打开它用于读写。
	// 我们将 `""` 作为第一个参数，这样 `os.CreateTemp` 会在我们操作系统的默认位置创建文件。
	f, err := os.CreateTemp("", "sample")
	check(err)

	// 显示临时文件的名称。在基于Unix的操作系统上，目录可能是 `/tmp`。
	// 文件名以作为 `os.CreateTemp` 第二个参数给出的前缀开头，其余部分会自动选择以确保并发调用总是创建不同的文件名。
	fmt.Println("临时文件名:", f.Name())

	// 完成后清理文件。操作系统可能会在一段时间后自行清理临时文件，但显式地这样做是个好习惯。
	defer os.Remove(f.Name())

	// 我们可以向文件写入一些数据。
	_, err = f.Write([]byte{1, 2, 3, 4})
	check(err)

	// 如果我们打算写入多个临时文件，可能更喜欢创建一个临时 *目录*。
	// `os.MkdirTemp` 的参数与 `CreateTemp` 的相同，但它返回一个目录 *名称* 而不是一个打开的文件。
	dname, err := os.MkdirTemp("", "sampledir")
	check(err)
	fmt.Println("临时目录名:", dname)

	defer os.RemoveAll(dname)

	// 现在我们可以通过在临时目录名前加上前缀来合成临时文件名。
	fname := filepath.Join(dname, "file1")
	err = os.WriteFile(fname, []byte{1, 2}, 0666)
	check(err)
}

```
