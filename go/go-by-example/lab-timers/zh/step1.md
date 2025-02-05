# 定时器

本实验要求实现一个定时器，它能等待指定的持续时间，然后触发。此外，该定时器应在触发前可取消。

- 应导入 `time` 包。
- 应创建两个定时器，一个等待2秒，另一个等待1秒。
- 第一个定时器触发时应打印 “Timer 1 fired”。
- 第二个定时器触发时应打印 “Timer 2 fired”。
- 第二个定时器应在触发前取消。
- 程序应等待2秒，以表明第二个定时器未触发。

```sh
// 第一个定时器将在我们启动程序后约2秒触发，但第二个定时器应在有机会触发之前停止。
$ go run timers.go
Timer 1 fired
Timer 2 stopped
```

以下是完整代码：

```go
// 我们常常希望在未来的某个时刻执行Go代码，或者以一定的间隔重复执行。Go语言内置的
// _定时器_ 和 _定时触发_ 功能使这两项任务都变得轻松。我们先来看定时器，然后再看
// [定时触发](tickers)。

package main

import (
	"fmt"
	"time"
)

func main() {

	// 定时器表示未来的一个单一事件。你告诉定时器你要等待多长时间，它会提供一个通道，
	// 在那个时候会收到通知。这个定时器将等待2秒。
	timer1 := time.NewTimer(2 * time.Second)

	// `<-timer1.C` 会阻塞在定时器的通道 `C` 上，直到它发送一个值，表示定时器已触发。
	<-timer1.C
	fmt.Println("Timer 1 fired")

	// 如果你只是想等待，你可以使用 `time.Sleep`。定时器可能有用的一个原因是，你可以
	// 在定时器触发前取消它。下面是一个例子。
	timer2 := time.NewTimer(time.Second)
	go func() {
		<-timer2.C
		fmt.Println("Timer 2 fired")
	}()
	stop2 := timer2.Stop()
	if stop2 {
		fmt.Println("Timer 2 stopped")
	}

	// 给 `timer2` 足够的时间来触发（如果它本来会触发的话），以表明它实际上已停止。
	time.Sleep(2 * time.Second)
}

```
