# 使用 `defer`

在这个实验中，你需要使用 `defer` 来创建一个文件，向其中写入内容，完成后关闭该文件。

- `createFile` 函数应使用给定路径创建一个文件，并返回指向该文件的指针。
- `writeFile` 函数应将字符串 "data" 写入文件。
- `closeFile` 函数应关闭文件并检查是否有错误。

```sh
# 运行该程序可确认文件在写入后会被关闭。
$ go run defer.go
创建中
写入中
关闭中
```

以下是完整代码：

```go
// `defer` 用于确保函数调用在程序执行的稍后阶段进行，通常用于清理目的。在其他语言中，`defer` 常被用于类似 `ensure` 和 `finally` 的场景。

package main

import (
	"fmt"
	"os"
)

// 假设我们要创建一个文件，写入内容，完成后关闭它。以下是使用 `defer` 实现的方法。
func main() {

	// 使用 `createFile` 获取文件对象后，立即使用 `closeFile` 延迟关闭该文件。这将在包含该函数的 `main` 函数结束时执行，即在 `writeFile` 完成之后。
	f := createFile("/tmp/defer.txt")
	defer closeFile(f)
	writeFile(f)
}

func createFile(p string) *os.File {
	fmt.Println("创建中")
	f, err := os.Create(p)
	if err!= nil {
		panic(err)
	}
	return f
}

func writeFile(f *os.File) {
	fmt.Println("写入中")
	fmt.Fprintln(f, "data")

}

func closeFile(f *os.File) {
	fmt.Println("关闭中")
	err := f.Close()
	// 即使在延迟函数中，关闭文件时检查错误也很重要。
	if err!= nil {
		fmt.Fprintf(os.Stderr, "错误: %v\n", err)
		os.Exit(1)
	}
}

```
