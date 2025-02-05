# 通道同步

本实验要解决的问题是创建一个 goroutine，它执行一些工作，并在工作完成时通过一个通道通知另一个 goroutine。

要完成本实验，你需要：

- 创建一个名为 `worker` 的函数，它接受一个 `bool` 类型的通道作为参数。
- 在 `worker` 函数内部，执行一些工作，然后向通道发送一个值，以通知工作已完成。
- 在 `main` 函数中，创建一个缓冲区大小为 1 的 `bool` 类型通道。
- 启动一个调用 `worker` 函数并将通道作为参数传递的 goroutine。
- 阻塞 `main` 函数，直到从通道接收到一个值。

```sh
$ go run channel-synchronization.go
working...done

# 如果你从这个程序中删除了 `<- done` 这一行，
# 程序会在 `worker` 甚至还未启动之前就退出。
```

以下是完整代码：

```go
// 我们可以使用通道在多个 goroutine 之间同步执行。
// 这是一个使用阻塞接收来等待 goroutine 完成的示例。
// 当等待多个 goroutine 完成时，你可能更倾向于使用 [WaitGroup](waitgroups)。

package main

import (
	"fmt"
	"time"
)

// 这是我们将在 goroutine 中运行的函数。
// `done` 通道将用于通知另一个 goroutine 此函数的工作已完成。
func worker(done chan bool) {
	fmt.Print("working...")
	time.Sleep(time.Second)
	fmt.Println("done")

	// 发送一个值以通知我们已完成。
	done <- true
}

func main() {

	// 启动一个 worker goroutine，给它用于通知的通道。
	done := make(chan bool, 1)
	go worker(done)

	// 阻塞，直到我们从通道接收到来自 worker 的通知。
	<-done
}

```
