# 채널 닫기

이 랩에서는 작업자에게 더 이상 작업이 없을 때 주어진 코드를 수정하여 `jobs` 채널을 닫아야 합니다. 또한 모든 작업이 완료되었을 때 알림을 보내기 위해 `done` 채널을 사용해야 합니다.

- `main()` 고루틴에서 작업자 고루틴으로 수행할 작업을 전달하기 위해 버퍼링된 채널 `jobs`를 사용합니다.
- 모든 작업이 완료되었을 때 알림을 보내기 위해 채널 `done`을 사용합니다.
- `j, more := <-jobs`를 사용하여 `jobs`에서 반복적으로 값을 수신하는 작업자 고루틴을 사용합니다.
- 모든 작업이 완료되었을 때 `done`에 알림을 보내기 위해 수신의 특수한 2-값 형식을 사용합니다.
- `jobs` 채널을 통해 작업자에게 3 개의 작업을 보내고, 채널을 닫습니다.
- [동기화](channel-synchronization) 방식을 사용하여 작업자를 기다립니다.

```sh
$ go run closing-channels.go
sent job 1
received job 1
sent job 2
received job 2
sent job 3
received job 3
sent all jobs
received all jobs

# The idea of closed channels leads naturally to our next
# example: `range` over channels.
```

전체 코드는 다음과 같습니다.

```go
// _Closing_ a channel indicates that no more values
// will be sent on it. This can be useful to communicate
// completion to the channel's receivers.

package main

import "fmt"

// In this example we'll use a `jobs` channel to
// communicate work to be done from the `main()` goroutine
// to a worker goroutine. When we have no more jobs for
// the worker we'll `close` the `jobs` channel.
func main() {
	jobs := make(chan int, 5)
	done := make(chan bool)

	// Here's the worker goroutine. It repeatedly receives
	// from `jobs` with `j, more := <-jobs`. In this
	// special 2-value form of receive, the `more` value
	// will be `false` if `jobs` has been `close`d and all
	// values in the channel have already been received.
	// We use this to notify on `done` when we've worked
	// all our jobs.
	go func() {
		for {
			j, more := <-jobs
			if more {
				fmt.Println("received job", j)
			} else {
				fmt.Println("received all jobs")
				done <- true
				return
			}
		}
	}()

	// This sends 3 jobs to the worker over the `jobs`
	// channel, then closes it.
	for j := 1; j <= 3; j++ {
		jobs <- j
		fmt.Println("sent job", j)
	}
	close(jobs)
	fmt.Println("sent all jobs")

	// We await the worker using the
	// [synchronization](channel-synchronization) approach
	// we saw earlier.
	<-done
}
```
