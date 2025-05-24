# 논블로킹 채널 연산

이 랩에서 해결해야 할 문제는 `default` 절과 함께 `select` 문을 사용하여 논블로킹 채널 연산을 구현하는 것입니다.

- `default` 절과 함께 `select` 문을 사용하여 채널에서 논블로킹 수신을 구현합니다.
- `default` 절과 함께 `select` 문을 사용하여 채널에서 논블로킹 전송을 구현합니다.
- 여러 `case` 절과 `default` 절을 사용하여 `select` 문을 통해 다중 방식 논블로킹 선택을 구현합니다.

```sh
$ go run non-blocking-channel-operations.go
no message received
no message sent
no activity
```

전체 코드는 다음과 같습니다.

```go
// 채널에서의 기본 전송 및 수신은 블로킹됩니다.
// 그러나 `default` 절과 함께 `select` 를 사용하여
// _논블로킹_ 전송, 수신, 그리고 심지어
// 논블로킹 다중 방식 `select` 를 구현할 수 있습니다.

package main

import "fmt"

func main() {
	messages := make(chan string)
	signals := make(chan bool)

	// 다음은 논블로킹 수신입니다. `messages` 에서
	// 값을 사용할 수 있으면 `select` 는 해당 값으로
	// `<-messages` `case` 를 선택합니다. 그렇지 않으면
	// 즉시 `default` case 를 선택합니다.
	select {
	case msg := <-messages:
		fmt.Println("received message", msg)
	default:
		fmt.Println("no message received")
	}

	// 논블로킹 전송도 유사하게 작동합니다. 여기에서 `msg` 는
	// `messages` 채널로 전송될 수 없습니다. 왜냐하면
	// 채널에 버퍼가 없고 수신자가 없기 때문입니다.
	// 따라서 `default` case 가 선택됩니다.
	msg := "hi"
	select {
	case messages <- msg:
		fmt.Println("sent message", msg)
	default:
		fmt.Println("no message sent")
	}

	// `default` 절 위에 여러 `case` 를 사용하여
	// 다중 방식 논블로킹 `select` 를 구현할 수 있습니다.
	// 여기서는 `messages` 와 `signals` 모두에서 논블로킹 수신을 시도합니다.
	select {
	case msg := <-messages:
		fmt.Println("received message", msg)
	case sig := <-signals:
		fmt.Println("received signal", sig)
	default:
		fmt.Println("no activity")
	}
}
```
