# 채널 버퍼링 (Channel Buffering)

기본적으로 Golang 의 채널은 언버퍼 (unbuffered) 됩니다. 즉, 전송된 값을 수신할 준비가 된 해당 수신자가 있는 경우에만 전송 (`chan <-`) 을 허용합니다. 그러나 버퍼 채널 (buffered channels) 은 해당 값에 대한 해당 수신자 없이 제한된 수의 값을 허용합니다. 이 랩에서는 버퍼 채널을 생성하고 동시 수신 없이 채널에 값을 전송해야 합니다.

- Golang 채널에 대한 기본적인 지식
- 버퍼 채널에 대한 이해

```sh
$ go run channel-buffering.go
buffered
channel
```

전체 코드는 다음과 같습니다.

```go
// 기본적으로 채널은 _unbuffered_입니다. 즉,
// 전송된 값을 수신할 준비가 된
// 해당 수신자 (`<- chan`) 가 있는 경우에만 전송 (`chan <-`) 을 허용합니다.
// _Buffered channels_는 해당 값에 대한 해당 수신자 없이
// 제한된 수의 값을 허용합니다.

package main

import "fmt"

func main() {

	// 여기에서 최대 2 개의 값을 버퍼링하는 문자열 채널을 `make` 합니다.
	messages := make(chan string, 2)

	// 이 채널은 버퍼링되므로
	// 해당 동시 수신 없이 이 값들을 채널로 보낼 수 있습니다.
	messages <- "buffered"
	messages <- "channel"

	// 나중에 이 두 값을 평소처럼 수신할 수 있습니다.
	fmt.Println(<-messages)
	fmt.Println(<-messages)
}
```
