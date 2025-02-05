# 定时器与定时器通道（Tickers）

在本实验中，你需要创建一个每500毫秒触发一次的定时器通道（ticker），直到我们停止它。你将使用一个通道来等待值的到来。

- 使用`time`包创建一个定时器通道（ticker）。
- 使用一个通道来等待值的到来。
- 使用`select`语句从通道接收值。
- 在1600毫秒后停止定时器通道（ticker）。

```sh
# 当我们运行这个程序时，定时器通道（ticker）应该在我们停止它之前触发3次。
$ go run tickers.go
Tick at 2012-09-23 11:29:56.487625 -0700 PDT
Tick at 2012-09-23 11:29:56.988063 -0700 PDT
Tick at 2012-09-23 11:29:57.488076 -0700 PDT
Ticker stopped
```

以下是完整代码：

```go
// [定时器](timers) 用于在未来某个时间点执行一次操作，而 _定时器通道（tickers）_ 用于定期重复执行操作。这是一个定时器通道（ticker）的示例，它会定期触发，直到我们停止它。

package main

import (
	"fmt"
	"time"
)

func main() {

	// 定时器通道（Tickers）使用与定时器类似的机制：一个会发送值的通道。在这里，我们将使用通道上的 `select` 内置函数来等待每500毫秒到达的值。
	ticker := time.NewTicker(500 * time.Millisecond)
	done := make(chan bool)

	go func() {
		for {
			select {
			case <-done:
				return
			case t := <-ticker.C:
				fmt.Println("Tick at", t)
			}
		}
	}()

	// 定时器通道（Tickers）可以像定时器一样停止。一旦定时器通道（ticker）停止，它将不会再从其通道接收任何值。我们将在1600毫秒后停止我们的定时器通道（ticker）。
	time.Sleep(1600 * time.Millisecond)
	ticker.Stop()
	done <- true
	fmt.Println("Ticker stopped")
}

```
