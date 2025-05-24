# 타이머 (Timers)

이 랩에서는 지정된 시간 동안 대기한 후 실행되는 타이머를 구현해야 합니다. 또한, 타이머는 실행되기 전에 취소할 수 있어야 합니다.

- `time` 패키지를 임포트 (import) 해야 합니다.
- 2 초 동안 대기하는 타이머와 1 초 동안 대기하는 타이머, 두 개의 타이머를 생성해야 합니다.
- 첫 번째 타이머는 실행될 때 "Timer 1 fired"를 출력해야 합니다.
- 두 번째 타이머는 실행될 때 "Timer 2 fired"를 출력해야 합니다.
- 두 번째 타이머는 실행되기 전에 취소되어야 합니다.
- 프로그램은 두 번째 타이머가 실행되지 않았음을 보여주기 위해 2 초 동안 대기해야 합니다.

```sh
// The first timer will fire ~2s after we start the
// program, but the second should be stopped before it has
// a chance to fire.
$ go run timers.go
Timer 1 fired
Timer 2 stopped
```

전체 코드는 다음과 같습니다.

```go
// We often want to execute Go code at some point in the
// future, or repeatedly at some interval. Go's built-in
// _timer_ and _ticker_ features make both of these tasks
// easy. We'll look first at timers and then
// at [tickers](tickers).

package main

import (
	"fmt"
	"time"
)

func main() {

	// Timers represent a single event in the future. You
	// tell the timer how long you want to wait, and it
	// provides a channel that will be notified at that
	// time. This timer will wait 2 seconds.
	timer1 := time.NewTimer(2 * time.Second)

	// The `<-timer1.C` blocks on the timer's channel `C`
	// until it sends a value indicating that the timer
	// fired.
	<-timer1.C
	fmt.Println("Timer 1 fired")

	// If you just wanted to wait, you could have used
	// `time.Sleep`. One reason a timer may be useful is
	// that you can cancel the timer before it fires.
	// Here's an example of that.
	timer2 := time.NewTimer(time.Second)
	go func() {
		<-timer2.C
		fmt.Println("Timer 2 fired")
	}()
	stop2 := timer2.Stop()
	if stop2 {
		fmt.Println("Timer 2 stopped")
	}

	// Give the `timer2` enough time to fire, if it ever
	// was going to, to show it is in fact stopped.
	time.Sleep(2 * time.Second)
}

```
