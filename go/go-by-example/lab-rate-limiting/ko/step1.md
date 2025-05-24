# 속도 제한 (Rate Limiting)

문제는 서비스 품질을 유지하고 리소스 사용률을 제어하기 위해 들어오는 요청 처리를 제한하는 것입니다.

- Go 프로그래밍 언어
- 고루틴 (goroutine), 채널 (channel) 및 티커 (ticker) 에 대한 기본적인 이해

```sh
# 프로그램을 실행하면 원하는 대로 첫 번째 요청 배치가
# 약 200 밀리초마다 한 번씩 처리되는 것을 볼 수 있습니다.
$ go run rate-limiting.go
request 1 2012-10-19 00:38:18.687438 +0000 UTC
request 2 2012-10-19 00:38:18.887471 +0000 UTC
request 3 2012-10-19 00:38:19.087238 +0000 UTC
request 4 2012-10-19 00:38:19.287338 +0000 UTC
request 5 2012-10-19 00:38:19.487331 +0000 UTC

# 두 번째 요청 배치에 대해 버스트 가능한 속도 제한으로 인해
# 처음 3 개를 즉시 처리한 다음, 나머지 2 개는 각각 약 200ms 지연으로 처리합니다.
request 1 2012-10-19 00:38:20.487578 +0000 UTC
request 2 2012-10-19 00:38:20.487645 +0000 UTC
request 3 2012-10-19 00:38:20.487676 +0000 UTC
request 4 2012-10-19 00:38:20.687483 +0000 UTC
request 5 2012-10-19 00:38:20.887542 +0000 UTC
```

전체 코드는 다음과 같습니다.

```go
// [_속도 제한_](https://en.wikipedia.org/wiki/Rate_limiting)
// 은 리소스 사용률을 제어하고
// 서비스 품질을 유지하는 중요한 메커니즘입니다. Go 는
// 고루틴 (goroutine), 채널 (channel) 및 [티커 (tickers)] 를 사용하여
// 속도 제한을 우아하게 지원합니다.

package main

import (
	"fmt"
	"time"
)

func main() {

	// 먼저 기본적인 속도 제한을 살펴보겠습니다. 들어오는 요청 처리를
	// 제한하려는 경우를 가정해 보겠습니다.
	// 동일한 이름의 채널에서 이러한 요청을 처리합니다.
	requests := make(chan int, 5)
	for i := 1; i <= 5; i++ {
		requests <- i
	}
	close(requests)

	// 이 `limiter` 채널은 200 밀리초마다 값을 받습니다.
	// 이것이 속도 제한 체계의 조절기입니다.
	limiter := time.Tick(200 * time.Millisecond)

	// 각 요청을 처리하기 전에 `limiter` 채널에서 수신을 차단하여
	// 200 밀리초마다 1 개의 요청으로 제한합니다.
	for req := range requests {
		<-limiter
		fmt.Println("request", req, time.Now())
	}

	// 전체 속도 제한을 유지하면서 속도 제한 체계에서
	// 짧은 요청 버스트를 허용할 수 있습니다.
	// 채널을 버퍼링하여 이를 수행할 수 있습니다. 이 `burstyLimiter`
	// 채널은 최대 3 개의 이벤트를 버스트할 수 있습니다.
	burstyLimiter := make(chan time.Time, 3)

	// 허용된 버스팅을 나타내기 위해 채널을 채웁니다.
	for i := 0; i < 3; i++ {
		burstyLimiter <- time.Now()
	}

	// 200 밀리초마다 최대 3 개까지 `burstyLimiter` 에
	// 새 값을 추가하려고 시도합니다.
	go func() {
		for t := range time.Tick(200 * time.Millisecond) {
			burstyLimiter <- t
		}
	}()

	// 이제 5 개의 추가 들어오는 요청을 시뮬레이션합니다. 처음
	// 3 개는 `burstyLimiter` 의 버스트 기능을 활용합니다.
	burstyRequests := make(chan int, 5)
	for i := 1; i <= 5; i++ {
		burstyRequests <- i
	}
	close(burstyRequests)
	for req := range burstyRequests {
		<-burstyLimiter
		fmt.Println("request", req, time.Now())
	}
}
```
