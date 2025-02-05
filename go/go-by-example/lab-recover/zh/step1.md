# 恢复

提供的代码中的 `mayPanic` 函数在被调用时会引发恐慌（panic）。你的任务是修改 `main` 函数，从恐慌中恢复并打印错误信息。

- 使用 `recover` 函数处理 `mayPanic` 函数中的恐慌。
- 当恐慌发生时打印错误信息。

```sh
$ go run recover.go
Recovered. Error:
a problem
```

以下是完整代码：

```go
// Go 语言通过使用内置函数 `recover`，使得从恐慌（panic）中“恢复”成为可能。一个 `recover` 可以阻止 `panic` 中止程序，并让程序继续执行。

// 一个这种情况可能有用的例子：如果一个客户端连接出现严重错误，服务器不希望崩溃。相反，服务器希望关闭该连接并继续为其他客户端提供服务。实际上，这就是 Go 语言的 `net/http` 包为 HTTP 服务器默认所做的事情。

package main

import "fmt"

// 这个函数会引发恐慌。
func mayPanic() {
	panic("a problem")
}

func main() {
	// `recover` 必须在延迟函数（deferred function）中调用。
	// 当封闭函数发生恐慌时，延迟函数将被激活，并且其中的 `recover` 调用将捕获恐慌。
	defer func() {
		if r := recover(); r!= nil {
			// `recover` 的返回值是在调用 `panic` 时引发的错误。
			fmt.Println("Recovered. Error:\n", r)
		}
	}()

	mayPanic()

	// 这段代码不会运行，因为 `mayPanic` 会引发恐慌。
	// `main` 函数的执行在恐慌发生时停止，并在延迟闭包中恢复。
	fmt.Println("After mayPanic()")
}

```
