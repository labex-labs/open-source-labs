# 关闭通道

在本实验中，你需要修改给定的代码，以便在工作协程没有更多任务时关闭 `jobs` 通道。你还需要使用 `done` 通道来通知所有任务已完成。

- 使用一个带缓冲的通道 `jobs`，将 `main()` 协程中待完成的工作传达给一个工作协程。
- 使用通道 `done` 来通知所有任务已完成。
- 使用一个工作协程，通过 `j, more := <-jobs` 从 `jobs` 通道中反复接收数据。
- 使用接收的特殊双值形式，在所有任务完成时通过 `done` 通道进行通知。
- 通过 `jobs` 通道向工作协程发送 3 个任务，然后关闭该通道。
- 使用 [同步](channel-synchronization) 方法等待工作协程完成。

```sh
$ go run closing-channels.go
发送任务 1
接收任务 1
发送任务 2
接收任务 2
发送任务 3
接收任务 3
发送所有任务
接收所有任务

# 关闭通道的概念自然地引出了我们的下一个
# 示例：对通道使用 `range`。
```

以下是完整代码：

```go
// 关闭一个通道表示不会再向其上发送更多值。
// 这对于向通道的接收者传达完成信息很有用。

package main

import "fmt"

// 在这个示例中，我们将使用一个 `jobs` 通道
// 来将 `main()` 协程中待完成的工作传达给一个工作协程。
// 当我们没有更多任务给工作协程时，我们将 `关闭` `jobs` 通道。
func main() {
	jobs := make(chan int, 5)
	done := make(chan bool)

	// 这是工作协程。它通过 `j, more := <-jobs` 从 `jobs` 通道中反复接收数据。
	// 在这种接收的特殊双值形式中，如果 `jobs` 已被 `关闭` 且通道中的所有值都已被接收，
	// 则 `more` 值将为 `false`。我们使用此来在完成所有任务时通过 `done` 通道进行通知。
	go func() {
		for {
			j, more := <-jobs
			if more {
				fmt.Println("接收任务", j)
			} else {
				fmt.Println("接收所有任务")
				done <- true
				return
			}
		}
	}()

	// 这通过 `jobs` 通道向工作协程发送 3 个任务，然后关闭该通道。
	for j := 1; j <= 3; j++ {
		jobs <- j
		fmt.Println("发送任务", j)
	}
	close(jobs)
	fmt.Println("发送所有任务")

	// 我们使用之前看到的 [同步](channel-synchronization) 方法等待工作协程完成。
	<-done
}

```
