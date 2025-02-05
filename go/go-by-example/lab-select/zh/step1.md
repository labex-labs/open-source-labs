# 选择语句（Select）

在本实验中，给你两个通道 `c1` 和 `c2`，它们会在一段时间后接收一个值。你的任务是使用 `select` 语句同时等待这两个值，并在每个值到达时打印出来。

- 你应该使用 `select` 语句来等待这两个通道。
- 你应该在每个通道接收到值时打印该值。

```sh
# 我们按预期先后接收到值 "one" 和 "two"。
$ time go run select.go
接收到 one
接收到 two

# 注意，总执行时间仅约为2秒，因为1秒和2秒的 `Sleep` 操作是并发执行的。
实际时间 0m2.245s
```

以下是完整代码：

```go
// Go语言的 _select_ 语句可让你等待多个通道操作。将goroutine和通道与select结合使用是Go语言的一项强大功能。

package main

import (
	"fmt"
	"time"
)

func main() {

	// 在我们的示例中，我们将通过两个通道进行选择。
	c1 := make(chan string)
	c2 := make(chan string)

	// 每个通道会在一段时间后接收一个值，以模拟例如在并发goroutine中执行的阻塞式RPC操作。
	go func() {
		time.Sleep(1 * time.Second)
		c1 <- "one"
	}()
	go func() {
		time.Sleep(2 * time.Second)
		c2 <- "two"
	}()

	// 我们将使用 `select` 语句同时等待这两个值，并在每个值到达时打印出来。
	for i := 0; i < 2; i++ {
		select {
		case msg1 := <-c1:
			fmt.Println("接收到", msg1)
		case msg2 := <-c2:
			fmt.Println("接收到", msg2)
		}
	}
}

```
