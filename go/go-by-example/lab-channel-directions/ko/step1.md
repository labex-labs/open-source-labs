# 채널 방향 (Channel Directions)

이 랩에서 해결해야 할 문제는 함수 매개변수로 사용되는 채널이 값의 송신 또는 수신만 하도록 지정되도록 주어진 코드를 수정하는 것입니다.

- Golang 의 기본 지식
- Golang 에서 채널과 채널 사용법에 대한 이해

```sh
$ go run channel-directions.go
passed message
```

전체 코드는 다음과 같습니다:

```go
// 채널을 함수 매개변수로 사용할 때,
// 채널이 값의 송신 또는 수신만 하도록 지정할 수 있습니다.
// 이러한 구체성은 프로그램의 타입 안전성을 높입니다.

package main

import "fmt"

// 이 `ping` 함수는 값을 보내기 위한 채널만 허용합니다.
// 이 채널에서 값을 수신하려고 시도하면 컴파일 시 오류가 발생합니다.
func ping(pings chan<- string, msg string) {
	pings <- msg
}

// `pong` 함수는 수신용 채널 (`pings`) 과 송신용 채널 (`pongs`) 을 허용합니다.
func pong(pings <-chan string, pongs chan<- string) {
	msg := <-pings
	pongs <- msg
}

func main() {
	pings := make(chan string, 1)
	pongs := make(chan string, 1)
	ping(pings, "passed message")
	pong(pings, pongs)
	fmt.Println(<-pongs)
}
```
