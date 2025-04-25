# 信号

在某些情况下，我们希望我们的 Go 程序能够智能地处理 Unix 信号。例如，我们可能希望服务器在接收到 `SIGTERM` 时优雅地关闭，或者命令行工具在接收到 `SIGINT` 时停止处理输入。

- 创建一个带缓冲的通道来接收 `os.Signal` 通知。
- 使用 `signal.Notify` 注册该通道以接收指定信号的通知。
- 创建一个 goroutine 来执行对信号的阻塞接收。
- 打印接收到的信号并通知程序可以结束。
- 等待预期的信号，然后退出。

```sh
# 当我们运行这个程序时，它将阻塞并等待信号。通过输入 `ctrl-C`（终端显示为 `^C`），我们可以发送一个 `SIGINT` 信号，使程序打印 `interrupt` 然后退出。
$ go run signals.go
awaiting signal
^C
interrupt
exiting
```

以下是完整代码：

```go
// 有时我们希望我们的 Go 程序能够智能地处理 [Unix 信号](https://en.wikipedia.org/wiki/Unix_signal)。
// 例如，我们可能希望服务器在接收到 `SIGTERM` 时优雅地关闭，或者命令行工具在接收到 `SIGINT` 时停止处理输入。
// 以下是如何使用通道在 Go 中处理信号。

package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
)

func main() {

	// Go 信号通知通过在通道上发送 `os.Signal` 值来工作。我们将创建一个通道来接收这些通知。请注意，这个通道应该是带缓冲的。
	sigs := make(chan os.Signal, 1)

	// `signal.Notify` 注册给定的通道以接收指定信号的通知。
	signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM)

	// 我们可以在主函数中从 `sigs` 接收，但让我们看看如何也可以在一个单独的 goroutine 中完成，以演示更实际的优雅关闭场景。
	done := make(chan bool, 1)

	go func() {
		// 这个 goroutine 执行对信号的阻塞接收。当它收到一个信号时，它会将其打印出来，然后通知程序可以结束。
		sig := <-sigs
		fmt.Println()
		fmt.Println(sig)
		done <- true
	}()

	// 程序将在这里等待，直到它收到预期的信号（如上面的 goroutine 在 `done` 上发送一个值所指示的），然后退出。
	fmt.Println("awaiting signal")
	<-done
	fmt.Println("exiting")
}

```
