# 타이머 (Timers) 와 티커 (Tickers)

이 랩에서는 멈출 때까지 500ms 마다 틱 (tick) 하는 티커를 생성해야 합니다. 값을 받을 때 채널 (channel) 을 사용하여 대기합니다.

- `time` 패키지를 사용하여 티커를 생성합니다.
- 값을 받을 때 채널을 사용하여 대기합니다.
- `select` 문을 사용하여 채널에서 값을 수신합니다.
- 1600ms 후에 티커를 중지합니다.

```sh
# 이 프로그램을 실행하면 티커가 멈추기 전에 3 번 틱해야 합니다.
$ go run tickers.go
Tick at 2012-09-23 11:29:56.487625 -0700 PDT
Tick at 2012-09-23 11:29:56.988063 -0700 PDT
Tick at 2012-09-23 11:29:57.488076 -0700 PDT
Ticker stopped
```

전체 코드는 다음과 같습니다.

```go
// [타이머](timers) 는 미래에 한 번 무언가를 수행하려는 경우에 사용됩니다. _티커_는 정기적인 간격으로 무언가를 반복적으로 수행하려는 경우에 사용됩니다. 다음은 멈출 때까지 주기적으로 틱하는 티커의 예입니다.

package main

import (
	"fmt"
	"time"
)

func main() {

	// 티커는 타이머와 유사한 메커니즘을 사용합니다: 값을 전송하는 채널입니다. 여기서는 채널에서 `select` 내장 함수를 사용하여 500ms 마다 값이 도착할 때까지 대기합니다.
	ticker := time.NewTicker(500 * time.Millisecond)
	done := make(chan bool)

	go func() {
		for {
			select {
			case <-done:
				return
			case t := <-ticker.C:
				fmt.Println("Tick at", t)
			}
		}
	}()

	// 티커는 타이머처럼 중지될 수 있습니다. 티커가 중지되면 더 이상 채널에서 값을 수신하지 않습니다. 1600ms 후에 티커를 중지합니다.
	time.Sleep(1600 * time.Millisecond)
	ticker.Stop()
	done <- true
	fmt.Println("Ticker stopped")
}
```
