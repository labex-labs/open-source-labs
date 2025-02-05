# 工作池

实现一个工作池，它通过 `jobs` 通道接收任务，并通过 `results` 通道发送相应的结果。工作池应该有多个并发实例，并且每个工作线程应该为每个任务休眠一秒，以模拟耗时的任务。

- 使用Go语言的goroutine和通道来实现工作池。
- 工作池应该有多个并发实例。
- 每个工作线程应该为每个任务休眠一秒，以模拟耗时的任务。
- 工作池应该通过 `jobs` 通道接收任务，并通过 `results` 通道发送相应的结果。

```sh
# 我们运行的程序展示了5个任务由不同的工作线程执行。尽管总工作量约为5秒，但程序仅耗时约2秒，因为有3个工作线程并发运行。
$ time go run worker-pools.go
worker 1 started job 1
worker 2 started job 2
worker 3 started job 3
worker 1 finished job 1
worker 1 started job 4
worker 2 finished job 2
worker 2 started job 5
worker 3 finished job 3
worker 1 finished job 4
worker 2 finished job 5

real 0m2.358s
```

以下是完整代码：

```go
// 在这个示例中，我们将研究如何使用Go语言的goroutine和通道来实现一个 _工作池_。

package main

import (
	"fmt"
	"time"
)

// 这是工作线程，我们将运行多个并发实例。这些工作线程将通过 `jobs` 通道接收任务，并通过 `results` 通道发送相应的结果。我们将为每个任务休眠一秒，以模拟耗时的任务。
func worker(id int, jobs <-chan int, results chan<- int) {
	for j := range jobs {
		fmt.Println("worker", id, "started  job", j)
		time.Sleep(time.Second)
		fmt.Println("worker", id, "finished job", j)
		results <- j * 2
	}
}

func main() {

	// 为了使用我们的工作线程池，我们需要向它们发送任务并收集结果。为此我们创建2个通道。
	const numJobs = 5
	jobs := make(chan int, numJobs)
	results := make(chan int, numJobs)

	// 启动3个工作线程，最初它们会被阻塞，因为还没有任务。
	for w := 1; w <= 3; w++ {
		go worker(w, jobs, results)
	}

	// 这里我们发送5个 `jobs`，然后 `关闭` 该通道，以表明这就是我们所有的任务。
	for j := 1; j <= numJobs; j++ {
		jobs <- j
	}
	close(jobs)

	// 最后我们收集所有任务的结果。这也确保了工作线程的goroutine已经完成。另一种等待多个goroutine完成的方法是使用 [WaitGroup](waitgroups)。
	for a := 1; a <= numJobs; a++ {
		<-results
	}
}

```
