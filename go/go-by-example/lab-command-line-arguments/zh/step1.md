# 命令行参数

该程序目前会打印出传递给它的原始命令行参数。不过，需要对其进行修改，以便根据参数的索引打印出特定的参数。

- 具备 Go 语言的基础知识
- 熟悉命令行参数

```sh
# 要试验命令行参数，最好先使用 `go build` 构建一个二进制文件。
$ go build command-line-arguments.go
$./command-line-arguments a b c d
[./command-line-arguments a b c d]
[a b c d]
c

# 接下来，我们将研究使用标志进行更高级的命令行处理。
```

以下是完整代码：

```go
// [_命令行参数_](https://en.wikipedia.org/wiki/Command-line_interface#Arguments)
// 是对程序执行进行参数化的常用方式。
// 例如，`go run hello.go` 使用 `run` 和
// `hello.go` 作为 `go` 程序的参数。

package main

import (
	"fmt"
	"os"
)

func main() {

	// `os.Args` 提供对原始命令行
	// 参数的访问。请注意，此切片中的第一个值
	// 是程序的路径，而 `os.Args[1:]`
	// 包含传递给程序的参数。
	argsWithProg := os.Args
	argsWithoutProg := os.Args[1:]

	// 你可以使用普通索引获取单个参数。
	arg := os.Args[3]

	fmt.Println(argsWithProg)
	fmt.Println(argsWithoutProg)
	fmt.Println(arg)
}

```
