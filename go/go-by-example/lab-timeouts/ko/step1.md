# 타임아웃 (Timeouts)

프로그램이 외부 리소스에 연결하거나 실행 시간을 제한해야 할 때 타임아웃은 중요합니다. 이 랩은 채널과 `select`를 사용하여 Go 에서 타임아웃을 구현하는 것입니다.

- 채널과 `select`를 사용하여 Go 에서 타임아웃을 구현합니다.
- 채널이 읽히지 않는 경우 고루틴 누수를 방지하기 위해 버퍼링된 채널을 사용합니다.
- 타임아웃 후 값을 기다리기 위해 `time.After`를 사용합니다.
- 준비된 첫 번째 수신을 진행하기 위해 `select`를 사용합니다.

```sh
# 이 프로그램을 실행하면 첫 번째 작업이 타임아웃되고
# 두 번째 작업이 성공하는 것을 보여줍니다.
$ go run timeouts.go
timeout 1
result 2
```

전체 코드는 다음과 같습니다.

```go
// _Timeouts_는 외부 리소스에 연결하거나
// 그렇지 않으면 실행 시간을 제한해야 하는 프로그램에 중요합니다.
// Go 에서 타임아웃을 구현하는 것은 채널과 `select` 덕분에 쉽고
// 우아합니다.

package main

import (
	"fmt"
	"time"
)

func main() {

	// 예시를 위해, 2 초 후에 채널 `c1` 에서 결과를 반환하는
	// 외부 호출을 실행한다고 가정해 보겠습니다. 채널이 버퍼링되므로
	// 고루틴에서의 전송은 논블로킹 (nonblocking) 입니다. 이것은
	// 채널이 절대 읽히지 않는 경우 고루틴 누수를 방지하는
	// 일반적인 패턴입니다.
	c1 := make(chan string, 1)
	go func() {
		time.Sleep(2 * time.Second)
		c1 <- "result 1"
	}()

	// 다음은 타임아웃을 구현하는 `select` 입니다.
	// `res := <-c1`은 결과를 기다리고 `<-time.After` 는
	// 1 초의 타임아웃 후에 전송될 값을 기다립니다. `select` 는
	// 준비된 첫 번째 수신을 진행하므로, 작업이 허용된 1 초보다
	// 오래 걸리면 타임아웃 케이스를 취하게 됩니다.
	select {
	case res := <-c1:
		fmt.Println(res)
	case <-time.After(1 * time.Second):
		fmt.Println("timeout 1")
	}

	// 3 초의 더 긴 타임아웃을 허용하면 `c2` 에서 수신이 성공하고
	// 결과를 출력합니다.
	c2 := make(chan string, 1)
	go func() {
		time.Sleep(2 * time.Second)
		c2 <- "result 2"
	}()
	select {
	case res := <-c2:
		fmt.Println(res)
	case <-time.After(3 * time.Second):
		fmt.Println("timeout 2")
	}
}
```
