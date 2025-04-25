# 协程

本实验要解决的问题是创建并运行协程来并发执行函数。

- `f` 函数应将其输入字符串和一个计数器变量打印三次。
- `main` 函数应同步调用 `f` 函数，并将“direct”和一个计数器变量打印三次。
- `main` 函数应使用协程异步调用 `f` 函数，并将“goroutine”和一个计数器变量打印三次。
- `main` 函数应启动一个协程来执行一个打印消息的匿名函数。
- `main` 函数应在打印出“done”之前等待协程完成执行。

```sh
# 当我们运行这个程序时，我们首先会看到阻塞调用的输出，然后是两个协程的输出。协程的输出可能会交错，因为 Go 运行时会并发运行协程。

# 接下来我们将看看并发 Go 程序中协程的一个补充：通道。
```

下面是完整代码：

```go
// 协程是轻量级的执行线程。

package main

import (
	"fmt"
	"time"
)

func f(from string) {
	for i := 0; i < 3; i++ {
		fmt.Println(from, ":", i)
	}
}

func main() {

	// 假设我们有一个函数调用 `f(s)`。以下是我们通常调用它的方式，同步运行它。
	f("direct")

	// 要在协程中调用这个函数，使用 `go f(s)`。这个新的协程将与调用它的协程并发执行。
	go f("goroutine")

	// 你也可以为一个匿名函数调用启动一个协程。
	go func(msg string) {
		fmt.Println(msg)
	}("going")

	// 我们的两个函数调用现在在不同的协程中异步运行。等待它们完成（对于更健壮的方法，使用 [WaitGroup](waitgroups)）。
	time.Sleep(time.Second)
	fmt.Println("done")
}

```
