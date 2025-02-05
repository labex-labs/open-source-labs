# waitgroups

本实验要解决的问题是启动几个 goroutine，并为每个 goroutine 增加 WaitGroup 计数器。然后，我们需要等待所有启动的 goroutine 完成。

- 具备 Go 语言的基础知识。
- 理解 Go 语言中的并发。
- 熟悉 `sync` 包。

```sh
$ go run waitgroups.go
Worker 5 starting
Worker 3 starting
Worker 4 starting
Worker 1 starting
Worker 2 starting
Worker 4 done
Worker 1 done
Worker 2 done
Worker 5 done
Worker 3 done

# 每次调用时，工作线程启动和完成的顺序
# 可能会有所不同。
```

以下是完整代码：

```go
// 要等待多个 goroutine 完成，我们可以
// 使用一个 *等待组*。

package main

import (
	"fmt"
	"sync"
	"time"
)

// 这是我们将在每个 goroutine 中运行的函数。
func worker(id int) {
	fmt.Printf("Worker %d starting\n", id)

	// 休眠以模拟耗时任务。
	time.Sleep(time.Second)
	fmt.Printf("Worker %d done\n", id)
}

func main() {

	// 这个 WaitGroup 用于等待在此启动的所有
	// goroutine 完成。注意：如果将 WaitGroup 显式传递给函数，
	// 应该通过 *指针* 传递。
	var wg sync.WaitGroup

	// 启动几个 goroutine 并为每个 goroutine 增加
	// WaitGroup 计数器。
	for i := 1; i <= 5; i++ {
		wg.Add(1)
		// 避免在每个 goroutine 闭包中重用相同的 `i` 值。
		// 有关更多详细信息，请参阅 [常见问题解答](https://golang.org/doc/faq#closures_and_goroutines)。
		i := i

		// 将 worker 调用包装在一个闭包中，确保告诉
		// WaitGroup 这个 worker 已完成。这样，worker 本身
		// 就不必了解其执行过程中涉及的并发原语。
		go func() {
			defer wg.Done()
			worker(i)
		}()
	}

	// 阻塞直到 WaitGroup 计数器归零；
	// 所有工作线程都通知已完成。
	wg.Wait()

	// 请注意，这种方法没有直接的方式
	// 来传播工作线程中的错误。对于更
	// 高级的用例，请考虑使用
	// [errgroup 包](https://pkg.go.dev/golang.org/x/sync/errgroup)。
}

```
