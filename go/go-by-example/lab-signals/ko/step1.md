# Signals (시그널)

경우에 따라 Go 프로그램이 Unix 시그널을 지능적으로 처리하도록 하고 싶을 수 있습니다. 예를 들어, 서버가 `SIGTERM`을 수신하면 정상적으로 종료되도록 하거나, 명령줄 도구가 `SIGINT`를 수신하면 입력을 중지하도록 할 수 있습니다.

- `os.Signal` 알림을 수신하기 위해 버퍼링된 채널을 생성합니다.
- `signal.Notify`를 사용하여 지정된 시그널의 알림을 수신하도록 채널을 등록합니다.
- 시그널에 대한 블로킹 수신을 실행하는 고루틴을 생성합니다.
- 수신된 시그널을 출력하고 프로그램이 종료될 수 있음을 알립니다.
- 예상된 시그널을 기다린 다음 종료합니다.

```sh
# 이 프로그램을 실행하면 시그널을 기다리면서 블록됩니다.
# `ctrl-C` (터미널에 `^C` 로 표시됨) 를 입력하여
# `SIGINT` 시그널을 보낼 수 있습니다.
# 그러면 프로그램이 `interrupt` 를 출력한 다음 종료됩니다.
$ go run signals.go
awaiting signal
^C
interrupt
exiting
```

전체 코드는 다음과 같습니다.

```go
// 때때로 Go 프로그램이 [Unix signals](https://en.wikipedia.org/wiki/Unix_signal) 을 지능적으로 처리하기를 원합니다.
// 예를 들어, 서버가 `SIGTERM` 을 수신하면 정상적으로
// 종료되도록 하거나, 명령줄 도구가 `SIGINT` 를 수신하면
// 입력을 중지하도록 할 수 있습니다.
// 다음은 채널을 사용하여 Go 에서 시그널을 처리하는 방법입니다.

package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
)

func main() {

	// Go 시그널 알림은 채널에서 `os.Signal`
	// 값을 전송하여 작동합니다. 이러한 알림을
	// 수신하기 위해 채널을 생성합니다. 이 채널은
	// 버퍼링되어야 합니다.
	sigs := make(chan os.Signal, 1)

	// `signal.Notify` 는 지정된 시그널의 알림을
	// 수신하도록 주어진 채널을 등록합니다.
	signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM)

	// `sigs` 에서 메인 함수에서 수신할 수 있지만,
	// 정상적인 종료의 보다 현실적인 시나리오를
	// 보여주기 위해 별도의 고루틴에서 어떻게
	// 수행할 수 있는지 살펴보겠습니다.
	done := make(chan bool, 1)

	go func() {
		// 이 고루틴은 시그널에 대한 블로킹 수신을 실행합니다.
		// 시그널을 받으면 출력한 다음 프로그램이
		// 종료될 수 있음을 알립니다.
		sig := <-sigs
		fmt.Println()
		fmt.Println(sig)
		done <- true
	}()

	// 프로그램은 예상된 시그널을 받을 때까지
	// (위의 고루틴이 `done` 에서 값을 전송하여 표시됨)
	// 여기서 기다린 다음 종료합니다.
	fmt.Println("awaiting signal")
	<-done
	fmt.Println("exiting")
}
```
