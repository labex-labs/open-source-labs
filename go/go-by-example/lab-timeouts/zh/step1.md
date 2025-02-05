# 超时处理

当程序连接到外部资源或需要限制执行时间时，超时处理非常重要。本实验将使用通道（channels）和 `select` 在 Go 语言中实现超时处理。

- 使用通道（channels）和 `select` 在 Go 语言中实现超时处理。
- 使用带缓冲的通道（buffered channel），以防通道从未被读取，从而防止 goroutine 泄漏。
- 使用 `time.After` 在超时时等待一个值被发送。
- 使用 `select` 处理第一个准备好的接收操作。

```sh
# 运行此程序会显示第一个操作超时，第二个操作成功。
$ go run timeouts.go
timeout 1
result 2
```

以下是完整代码：

```go
// 对于连接到外部资源或需要限制执行时间的程序，“超时处理”非常重要。由于有了通道（channels）和 `select`，在 Go 语言中实现超时处理既简单又优雅。

package main

import (
	"fmt"
	"time"
)

func main() {

	// 在我们的示例中，假设我们正在执行一个外部调用，该调用在 2 秒后通过通道 `c1` 返回其结果。请注意，该通道是带缓冲的，因此 goroutine 中的发送操作是非阻塞的。这是一种常见的模式，用于防止在通道从未被读取的情况下发生 goroutine 泄漏。
	c1 := make(chan string, 1)
	go func() {
		time.Sleep(2 * time.Second)
		c1 <- "result 1"
	}()

	// 这是实现超时处理的 `select`。`res := <-c1` 等待结果，`<-time.After` 等待在 1 秒超时后发送的值。由于 `select` 会处理第一个准备好的接收操作，如果操作耗时超过允许的 1 秒，我们将采用超时情况。
	select {
	case res := <-c1:
		fmt.Println(res)
	case <-time.After(1 * time.Second):
		fmt.Println("timeout 1")
	}

	// 如果我们将超时时间延长到 3 秒，那么从 `c2` 的接收操作将成功，我们将打印结果。
	c2 := make(chan string, 1)
	go func() {
		time.Sleep(2 * time.Second)
		c2 <- "result 2"
	}()
	select {
	case res := <-c2:
		fmt.Println(res)
	case <-time.After(3 * time.Second):
		fmt.Println("timeout 2")
	}
}

```
