# 写入文件

你需要编写一个 Go 程序，将字符串和字节写入文件，并使用带缓冲的写入器。

- 程序应将字符串和字节写入文件。
- 程序应使用带缓冲的写入器。

```sh
# 尝试运行写入文件的代码。
$ go run writing-files.go
写入了5个字节
写入了7个字节
写入了9个字节

# 然后检查写入文件的内容。
$ cat /tmp/dat1
hello
go
$ cat /tmp/dat2
some
writes
buffered

# 接下来，我们将看看如何将我们刚刚看到的一些文件 I/O 概念
# 应用到 `stdin` 和 `stdout` 流上。
```

以下是完整代码：

```go
// 在 Go 中写入文件遵循与我们之前看到的读取文件类似的模式。

package main

import (
	"bufio"
	"fmt"
	"os"
)

func check(e error) {
	if e!= nil {
		panic(e)
	}
}

func main() {

	// 首先，这是将字符串（或只是字节）
	// 写入文件的方法。
	d1 := []byte("hello\ngo\n")
	err := os.WriteFile("/tmp/dat1", d1, 0644)
	check(err)

	// 对于更精细的写入，打开一个文件进行写入。
	f, err := os.Create("/tmp/dat2")
	check(err)

	// 打开文件后立即延迟调用 `Close` 是一种惯用做法。
	defer f.Close()

	// 正如你所期望的，你可以写入字节切片。
	d2 := []byte{115, 111, 109, 101, 10}
	n2, err := f.Write(d2)
	check(err)
	fmt.Printf("写入了 %d 个字节\n", n2)

	// 也可以使用 `WriteString`。
	n3, err := f.WriteString("writes\n")
	check(err)
	fmt.Printf("写入了 %d 个字节\n", n3)

	// 发出 `Sync` 以将写入刷新到稳定存储。
	f.Sync()

	// `bufio` 除了我们之前看到的带缓冲的读取器之外，
	// 还提供带缓冲的写入器。
	w := bufio.NewWriter(f)
	n4, err := w.WriteString("buffered\n")
	check(err)
	fmt.Printf("写入了 %d 个字节\n", n4)

	// 使用 `Flush` 确保所有缓冲操作都已
	// 应用到底层写入器。
	w.Flush()

}

```
