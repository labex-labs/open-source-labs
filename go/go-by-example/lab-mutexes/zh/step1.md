# 互斥锁

本实验要解决的问题是，使用多个 goroutine 在循环中递增一个命名计数器，并确保对计数器的访问是同步的。

- 使用一个 `Container` 结构体来保存计数器的映射。
- 使用一个 `Mutex` 来同步对 `counters` 映射的访问。
- `Container` 结构体应该有一个 `inc` 方法，该方法接受一个 `name` 字符串，并递增 `counters` 映射中相应的计数器。
- `inc` 方法在访问 `counters` 映射之前应该锁定互斥锁，并在函数结束时使用 `defer` 语句解锁。
- 使用 `sync.WaitGroup` 结构体来等待 goroutine 完成。
- 使用 `fmt.Println` 函数来打印 `counters` 映射。

```sh
# 运行程序会显示计数器
# 按预期更新。

# 接下来我们将看看如何仅使用 goroutine 和通道来实现相同的状态
# 管理任务。
```

以下是完整代码：

```go
// 在前面的示例中，我们看到了如何使用 [原子操作](atomic-counters) 来管理简单的
// 计数器状态。对于更复杂的状态，我们可以使用 [_互斥锁_](https://en.wikipedia.org/wiki/Mutual_exclusion)
// 来在多个 goroutine 之间安全地访问数据。

package main

import (
	"fmt"
	"sync"
)

// Container 保存一个计数器的映射；由于我们希望
// 从多个 goroutine 并发更新它，所以我们
// 添加一个 `Mutex` 来同步访问。
// 请注意，互斥锁不能被复制，所以如果这个
// `struct` 被传递，应该通过指针来传递。
type Container struct {
	mu       sync.Mutex
	counters map[string]int
}

func (c *Container) inc(name string) {
	// 在访问 `counters` 之前锁定互斥锁；在函数结束时使用 [defer](defer)
	// 语句解锁。
	c.mu.Lock()
	defer c.mu.Unlock()
	c.counters[name]++
}

func main() {
	c := Container{
		// 请注意，互斥锁的零值可以直接使用，所以这里不需要
		// 初始化。
		counters: map[string]int{"a": 0, "b": 0},
	}

	var wg sync.WaitGroup

	// 这个函数在循环中递增一个命名计数器
	// 。
	doIncrement := func(name string, n int) {
		for i := 0; i < n; i++ {
			c.inc(name)
		}
		wg.Done()
	}

	// 并发运行几个 goroutine；请注意
	// 它们都访问同一个 `Container`，并且其中两个访问同一个计数器。
	wg.Add(3)
	go doIncrement("a", 10000)
	go doIncrement("a", 10000)
	go doIncrement("b", 10000)

	// 等待 goroutine 完成
	wg.Wait()
	fmt.Println(c.counters)
}

```
