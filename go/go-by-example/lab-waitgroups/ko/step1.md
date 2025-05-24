# waitgroups

이 랩에서 해결해야 할 문제는 여러 고루틴 (goroutine) 을 시작하고 각 고루틴에 대해 WaitGroup 카운터를 증가시키는 것입니다. 그런 다음, 시작된 모든 고루틴이 완료될 때까지 기다려야 합니다.

- Golang 에 대한 기본적인 지식.
- Golang 에서의 동시성 (concurrency) 이해.
- `sync` 패키지에 대한 숙지.

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

# The order of workers starting up and finishing
# is likely to be different for each invocation.
```

전체 코드는 다음과 같습니다.

```go
// To wait for multiple goroutines to finish, we can
// use a *wait group*.

package main

import (
	"fmt"
	"sync"
	"time"
)

// This is the function we'll run in every goroutine.
func worker(id int) {
	fmt.Printf("Worker %d starting\n", id)

	// Sleep to simulate an expensive task.
	time.Sleep(time.Second)
	fmt.Printf("Worker %d done\n", id)
}

func main() {

	// This WaitGroup is used to wait for all the
	// goroutines launched here to finish. Note: if a WaitGroup is
	// explicitly passed into functions, it should be done *by pointer*.
	var wg sync.WaitGroup

	// Launch several goroutines and increment the WaitGroup
	// counter for each.
	for i := 1; i <= 5; i++ {
		wg.Add(1)
		// Avoid re-use of the same `i` value in each goroutine closure.
		// See [the FAQ](https://golang.org/doc/faq#closures_and_goroutines)
		// for more details.
		i := i

		// Wrap the worker call in a closure that makes sure to tell
		// the WaitGroup that this worker is done. This way the worker
		// itself does not have to be aware of the concurrency primitives
		// involved in its execution.
		go func() {
			defer wg.Done()
			worker(i)
		}()
	}

	// Block until the WaitGroup counter goes back to 0;
	// all the workers notified they're done.
	wg.Wait()

	// Note that this approach has no straightforward way
	// to propagate errors from workers. For more
	// advanced use cases, consider using the
	// [errgroup package](https://pkg.go.dev/golang.org/x/sync/errgroup).
}
```
