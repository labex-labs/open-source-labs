# 原子计数器

问题是使用50个goroutine和`sync/atomic`包将一个计数器精确递增1000次。

- 使用`sync/atomic`包来递增计数器。
- 使用WaitGroup等待所有goroutine完成它们的工作。

```sh
# 我们期望得到恰好50000次操作。如果我们使用非原子的`ops++`来递增计数器，
# 我们可能会得到不同的数字，并且每次运行时都会变化，因为goroutine会相互干扰。
# 此外，当使用`-race`标志运行时，我们会得到数据竞争失败。
$ go run atomic-counters.go
ops: 50000

# 接下来我们将看看互斥锁，这是另一种管理状态的工具。
```

以下是完整代码：

```go
// 在Go语言中管理状态的主要机制是通过通道进行通信。例如，我们在[工作池](worker-pools)中看到了这一点。不过，还有其他一些管理状态的选项。在这里，我们将看看如何使用`sync/atomic`包来处理由多个goroutine访问的_原子计数器_。

package main

import (
	"fmt"
	"sync"
	"sync/atomic"
)

func main() {

	// 我们将使用一个无符号整数来表示我们的（始终为正的）计数器。
	var ops uint64

	// 一个WaitGroup将帮助我们等待所有goroutine完成它们的工作。
	var wg sync.WaitGroup

	// 我们将启动50个goroutine，每个goroutine将计数器精确递增1000次。
	for i := 0; i < 50; i++ {
		wg.Add(1)

		go func() {
			for c := 0; c < 1000; c++ {
				// 为了原子地递增计数器，我们使用`AddUint64`，通过`&`语法将其传递给我们的`ops`计数器的内存地址。
				atomic.AddUint64(&ops, 1)
			}
			wg.Done()
		}()
	}

	// 等待直到所有goroutine完成。
	wg.Wait()

	// 现在访问`ops`是安全的，因为我们知道没有其他goroutine正在写入它。在原子变量更新时安全地读取它也是可能的，使用像`atomic.LoadUint64`这样的函数。
	fmt.Println("ops:", ops)
}

```
