# 退出

本实验要解决的问题是使用 `os.Exit` 函数以特定状态码退出 Go 程序。

要完成本实验，你需要对 Go 编程和 `os` 包有基本的了解。

```sh
# 如果你使用 `go run` 运行 `exit.go`，退出状态将被 `go` 捕获并打印出来。
$ go run exit.go
exit status 3

# 通过构建并执行二进制文件，你可以在终端中看到状态。
$ go build exit.go
$./exit
$ echo $?
3

# 请注意，我们程序中的 `!` 永远不会被打印出来。
```

以下是完整代码：

```go
// 使用 `os.Exit` 以给定状态立即退出。

package main

import (
	"fmt"
	"os"
)

func main() {

	// 使用 `os.Exit` 时，`defer` 语句不会被执行，所以这个 `fmt.Println` 永远不会被调用。
	defer fmt.Println("!")

	// 以状态码 3 退出。
	os.Exit(3)
}

// 请注意，与例如 C 语言不同，Go 语言不会使用 `main` 函数的整数返回值来指示退出状态。如果你想以非零状态退出，应该使用 `os.Exit`。

```
