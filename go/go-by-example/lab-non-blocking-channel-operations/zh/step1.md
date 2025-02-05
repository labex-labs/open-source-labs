# 非阻塞通道操作

本实验要解决的问题是使用带有 `default` 子句的 `select` 语句来实现非阻塞通道操作。

- 使用带有 `default` 子句的 `select` 语句在通道上实现非阻塞接收。
- 使用带有 `default` 子句的 `select` 语句在通道上实现非阻塞发送。
- 使用带有多个 `case` 子句和一个 `default` 子句的 `select` 语句实现多路非阻塞选择。

```sh
$ go run non-blocking-channel-operations.go
未接收到消息
未发送消息
无活动
```

以下是完整代码：

```go
// 通道上的基本发送和接收是阻塞的。
// 但是，我们可以使用带有 `default` 子句的 `select` 来
// 实现非阻塞发送、接收，甚至非阻塞多路 `select`。

package main

import "fmt"

func main() {
	messages := make(chan string)
	signals := make(chan bool)

	// 这是一个非阻塞接收。如果 `messages` 上有值可用，那么 `select` 将
	// 选择带有该值的 `<-messages` `case`。如果没有，则会立即选择 `default` 情况。
	select {
	case msg := <-messages:
		fmt.Println("接收到消息", msg)
	default:
		fmt.Println("未接收到消息")
	}

	// 非阻塞发送的工作方式类似。这里 `msg` 无法发送到 `messages` 通道，因为
	// 该通道没有缓冲区且没有接收者。因此选择 `default` 情况。
	msg := "hi"
	select {
	case messages <- msg:
		fmt.Println("发送消息", msg)
	default:
		fmt.Println("未发送消息")
	}

	// 我们可以在 `default` 子句上方使用多个 `case` 来实现多路非阻塞
	// 选择。这里我们尝试对 `messages` 和 `signals` 进行非阻塞接收。
	select {
	case msg := <-messages:
		fmt.Println("接收到消息", msg)
	case sig := <-signals:
		fmt.Println("接收到信号", sig)
	default:
		fmt.Println("无活动")
	}
}

```
