# 채널 동기화 (Channel Synchronization)

이 랩에서 해결해야 할 문제는 어떤 작업을 수행하고 채널을 사용하여 작업이 완료되었음을 다른 고루틴에 알리는 고루틴을 생성하는 것입니다.

이 랩을 완료하려면 다음을 수행해야 합니다.

- `bool` 타입의 채널을 매개변수로 받는 `worker`라는 함수를 생성합니다.
- `worker` 함수 내부에서 어떤 작업을 수행한 다음, 작업이 완료되었음을 알리기 위해 채널에 값을 보냅니다.
- `main` 함수에서 버퍼 크기가 1 인 `bool` 타입의 채널을 생성합니다.
- `worker` 함수를 호출하고 채널을 매개변수로 전달하는 고루틴을 시작합니다.
- 채널에서 값을 받을 때까지 `main` 함수를 블록합니다.

```sh
$ go run channel-synchronization.go
working...done

# If you removed the `<- done` line from this program, the
# program would exit before the `worker` even
# started.
```

전체 코드는 다음과 같습니다.

```go
// We can use channels to synchronize execution
// across goroutines. Here's an example of using a
// blocking receive to wait for a goroutine to finish.
// When waiting for multiple goroutines to finish,
// you may prefer to use a [WaitGroup](waitgroups).

package main

import (
	"fmt"
	"time"
)

// This is the function we'll run in a goroutine. The
// `done` channel will be used to notify another
// goroutine that this function's work is done.
func worker(done chan bool) {
	fmt.Print("working...")
	time.Sleep(time.Second)
	fmt.Println("done")

	// Send a value to notify that we're done.
	done <- true
}

func main() {

	// Start a worker goroutine, giving it the channel to
	// notify on.
	done := make(chan bool, 1)
	go worker(done)

	// Block until we receive a notification from the
	// worker on the channel.
	<-done
}
```
