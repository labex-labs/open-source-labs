# Select (선택)

이 랩에서는 `c1`과 `c2`라는 두 개의 채널이 주어지며, 이 채널들은 일정 시간이 지난 후에 값을 수신합니다. 여러분의 과제는 `select`를 사용하여 이 두 값을 동시에 대기하고, 각 값이 도착하는 대로 출력하는 것입니다.

- `select` 문을 사용하여 두 채널을 모두 대기해야 합니다.
- 각 채널에서 수신된 값을 도착하는 대로 출력해야 합니다.

```sh
# 예상대로 `"one"` 과 `"two"` 값을 받습니다.
$ time go run select.go
received one
received two

# 총 실행 시간은 ~2 초입니다.
# 1 초 및 2 초 `Sleep` 이
# 동시에 실행되기 때문입니다.
real 0m2.245s
```

전체 코드는 다음과 같습니다.

```go
// Go 의 _select_는 여러 채널
// 연산을 대기할 수 있게 해줍니다. 고루틴과 채널을
// select 와 결합하는 것은 Go 의 강력한 기능입니다.

package main

import (
	"fmt"
	"time"
)

func main() {

	// 예시를 위해 두 채널을 선택합니다.
	c1 := make(chan string)
	c2 := make(chan string)

	// 각 채널은 일정 시간이 지난 후 값을 수신합니다.
	// 예를 들어, 동시 고루틴에서 실행되는
	// 블로킹 RPC 연산을 시뮬레이션합니다.
	go func() {
		time.Sleep(1 * time.Second)
		c1 <- "one"
	}()
	go func() {
		time.Sleep(2 * time.Second)
		c2 <- "two"
	}()

	// `select` 를 사용하여 이 두 값을
	// 동시에 대기하고, 각 값이 도착하는 대로 출력합니다.
	for i := 0; i < 2; i++ {
		select {
		case msg1 := <-c1:
			fmt.Println("received", msg1)
		case msg2 := <-c2:
			fmt.Println("received", msg2)
		}
	}
}
```
