# 速率限制

问题在于限制对传入请求的处理，以维持服务质量并控制资源利用。

- Go编程语言
- 对goroutine、通道和定时器有基本了解

```sh
# 运行我们的程序，我们会看到第一批请求
# 如预期那样每约200毫秒处理一次。
$ go run rate-limiting.go
request 1 2012-10-19 00:38:18.687438 +0000 UTC
request 2 2012-10-19 00:38:18.887471 +0000 UTC
request 3 2012-10-19 00:38:19.087238 +0000 UTC
request 4 2012-10-19 00:38:19.287338 +0000 UTC
request 5 2012-10-19 00:38:19.487331 +0000 UTC

# 对于第二批请求，由于可突发的速率限制，我们会立即处理前
# 3个请求，然后以约200毫秒的延迟处理剩余2个请求。
request 1 2012-10-19 00:38:20.487578 +0000 UTC
request 2 2012-10-19 00:38:20.487645 +0000 UTC
request 3 2012-10-19 00:38:20.487676 +0000 UTC
request 4 2012-10-19 00:38:20.687483 +0000 UTC
request 5 2012-10-19 00:38:20.887542 +0000 UTC
```

以下是完整代码：

```go
// [_速率限制_](https://en.wikipedia.org/wiki/Rate_limiting)
// 是控制资源利用和维持服务质量的重要机制。Go
// 语言通过goroutine、通道和[定时器](tickers)优雅地支持速率限制。

package main

import (
	"fmt"
	"time"
)

func main() {

	// 首先我们来看基本的速率限制。假设
	// 我们要限制对传入请求的处理。
	// 我们将通过同名通道来处理这些请求。
	requests := make(chan int, 5)
	for i := 1; i <= 5; i++ {
		requests <- i
	}
	close(requests)

	// 这个`limiter`通道每200毫秒会接收一个值。
	// 这是我们速率限制方案中的调节器。
	limiter := time.Tick(200 * time.Millisecond)

	// 通过在处理每个请求之前阻塞从`limiter`通道接收值，
	// 我们将自己限制为每200毫秒处理1个请求。
	for req := range requests {
		<-limiter
		fmt.Println("request", req, time.Now())
	}

	// 在我们的速率限制方案中，我们可能希望允许短时间的请求突发，
	// 同时保持总体速率限制。我们可以通过缓冲我们的限制器通道来实现这一点。
	// 这个`burstyLimiter`通道将允许最多3个事件的突发。
	burstyLimiter := make(chan time.Time, 3)

	// 填充通道以表示允许的突发。
	for i := 0; i < 3; i++ {
		burstyLimiter <- time.Now()
	}

	// 每200毫秒我们会尝试向`burstyLimiter`添加一个新值，
	// 直到其限制为3。
	go func() {
		for t := range time.Tick(200 * time.Millisecond) {
			burstyLimiter <- t
		}
	}()

	// 现在模拟另外5个传入请求。其中前3个
	// 将受益于`burstyLimiter`的突发能力。
	burstyRequests := make(chan int, 5)
	for i := 1; i <= 5; i++ {
		burstyRequests <- i
	}
	close(burstyRequests)
	for req := range burstyRequests {
		<-burstyLimiter
		fmt.Println("request", req, time.Now())
	}
}

```
