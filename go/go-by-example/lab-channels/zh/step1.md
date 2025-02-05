# 通道

在这个实验中，你需要创建一个新的通道，并从一个新的 goroutine 向其中发送一个值。然后，你将从通道接收该值并打印出来。

- 你必须使用 `make(chan val-type)` 语法来创建一个新的通道。
- 通道必须由它所传递的值进行类型化。
- 你必须使用 `channel <-` 语法向通道发送一个值。
- 你必须使用 `<-channel` 语法从通道接收一个值。
- 你必须使用一个新的 goroutine 向通道发送值。

```sh
# 当我们运行程序时，"ping" 消息通过我们的通道成功地从一个 goroutine 传递到另一个 goroutine。
$ go run channels.go
ping

# 默认情况下，发送和接收会阻塞，直到发送方和接收方都准备好。这个特性使我们能够在程序结束时等待 "ping" 消息，而无需使用任何其他同步机制。
```

下面是完整的代码：

```go
// 通道是连接并发 goroutine 的管道。你可以从一个 goroutine 向通道发送值，并从另一个 goroutine 接收这些值。

package main

import "fmt"

func main() {

	// 使用 `make(chan val-type)` 创建一个新的通道。通道由它们所传递的值进行类型化。
	messages := make(chan string)

	// 使用 `channel <-` 语法向通道发送一个值。在这里，我们从一个新的 goroutine 向上面创建的 `messages` 通道发送 "ping"。
	go func() { messages <- "ping" }()

	// `<-channel` 语法从通道接收一个值。在这里，我们将接收上面发送的 "ping" 消息并打印出来。
	msg := <-messages
	fmt.Println(msg)
}

```
