# 有状态的 Goroutine

在并发编程中，同步对共享状态的访问以避免竞态条件和数据损坏至关重要。本实验展示了一种场景：一个 goroutine 拥有状态，其他 goroutine 发送消息来读取或写入该状态。

- 使用通道向拥有状态的 goroutine 发出读取和写入请求。
- 使用 `readOp` 和 `writeOp` 结构体封装请求和响应。
- 使用映射来存储状态。
- 使用 `resp` 通道指示成功并返回值。
- 使用 `atomic` 包统计读取和写入操作。
- 使用 `time` 包在操作之间添加延迟。

```sh
# 运行我们的程序会显示，基于 goroutine 的
# 状态管理示例总共完成了约 80,000 次
# 操作。
$ go run stateful-goroutines.go
readOps: 71708
writeOps: 7177

# 对于这种特定情况，基于 goroutine 的方法
# 比基于互斥锁的方法稍微复杂一些。不过
# 在某些情况下它可能会很有用，例如
# 当你涉及其他通道时，或者当管理多个
# 这样的互斥锁容易出错时。你应该使用
# 感觉最自然的方法，特别是在理解程序
# 的正确性方面。
```

以下是完整代码：

```go
// 在上一个示例中，我们使用显式锁定
// [互斥锁](mutexes) 来同步多个 goroutine
// 对共享状态的访问。另一种选择是使用
// goroutine 和通道的内置同步功能来
// 实现相同的结果。这种基于通道的方法
// 符合 Go 通过通信共享内存以及让每个
// 数据片段恰好由一个 goroutine 拥有的
// 理念。

package main

import (
	"fmt"
	"math/rand"
	"sync/atomic"
	"time"
)

// 在这个示例中，我们的状态将由单个
// goroutine 拥有。这将保证数据在并发
// 访问时永远不会被损坏。为了读取或
// 写入该状态，其他 goroutine 将向拥有
// 状态的 goroutine 发送消息并接收相应
// 的回复。这些 `readOp` 和 `writeOp` 结构
// 体封装了那些请求以及拥有状态的
// goroutine 进行响应的方式。
type readOp struct {
	key  int
	resp chan int
}
type writeOp struct {
	key  int
	val  int
	resp chan bool
}

func main() {

	// 与之前一样，我们将统计执行的操作数量。
	var readOps uint64
	var writeOps uint64

	// `reads` 和 `writes` 通道将分别被其他
	// goroutine 用于发出读取和写入请求。
	reads := make(chan readOp)
	writes := make(chan writeOp)

	// 这是拥有 `state` 的 goroutine，`state`
	// 是一个映射，与上一个示例相同，但现在
	// 是有状态 goroutine 私有的。这个
	// goroutine 反复在 `reads` 和 `writes`
	// 通道上进行选择，在请求到达时进行响应。
	// 响应是通过首先执行请求的操作，然后
	// 在响应通道 `resp` 上发送一个值来指示
	// 成功（在 `reads` 的情况下是期望的值）。
	go func() {
		var state = make(map[int]int)
		for {
			select {
			case read := <-reads:
				read.resp <- state[read.key]
			case write := <-writes:
				state[write.key] = write.val
				write.resp <- true
			}
		}
	}()

	// 这启动了 100 个 goroutine，通过 `reads`
	// 通道向拥有状态的 goroutine 发出读取请求。
	// 每次读取都需要构造一个 `readOp`，通过
	// `reads` 通道发送它，然后通过提供的
	// `resp` 通道接收结果。
	for r := 0; r < 100; r++ {
		go func() {
			for {
				read := readOp{
					key:  rand.Intn(5),
					resp: make(chan int)}
				reads <- read
				<-read.resp
				atomic.AddUint64(&readOps, 1)
				time.Sleep(time.Millisecond)
			}
		}()
	}

	// 我们也启动 10 个写入操作，使用类似的
	// 方法。
	for w := 0; w < 10; w++ {
		go func() {
			for {
				write := writeOp{
					key:  rand.Intn(5),
					val:  rand.Intn(100),
					resp: make(chan bool)}
				writes <- write
				<-write.resp
				atomic.AddUint64(&writeOps, 1)
				time.Sleep(time.Millisecond)
			}
		}()
	}

	// 让 goroutine 工作一秒钟。
	time.Sleep(time.Second)

	// 最后，捕获并报告操作计数。
	readOpsFinal := atomic.LoadUint64(&readOps)
	fmt.Println("readOps:", readOpsFinal)
	writeOpsFinal := atomic.LoadUint64(&writeOps)
	fmt.Println("writeOps:", writeOpsFinal)
}

```
