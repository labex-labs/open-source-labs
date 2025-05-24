# Epoch

이 랩에서 해결해야 할 문제는 Unix epoch 이후의 초, 밀리초 또는 나노초 수를 계산할 수 있는 Golang 프로그램을 작성하는 것입니다.

이 랩을 완료하려면 Golang 에 대한 기본적인 이해와 다음 요구 사항이 필요합니다.

- Golang 의 `time` 패키지에 대한 숙지.
- `time` 패키지에서 `Unix`, `UnixMilli`, 및 `UnixNano` 함수를 사용하는 방법에 대한 지식.

```sh
$ go run epoch.go
2012-10-31 16:13:58.292387 +0000 UTC
1351700038
1351700038292
1351700038292387000
2012-10-31 16:13:58 +0000 UTC
2012-10-31 16:13:58.292387 +0000 UTC

# Next we'll look at another time-related task: time
# parsing and formatting.
```

전체 코드는 다음과 같습니다.

```go
// A common requirement in programs is getting the number
// of seconds, milliseconds, or nanoseconds since the
// [Unix epoch](https://en.wikipedia.org/wiki/Unix_time).
// Here's how to do it in Go.

package main

import (
	"fmt"
	"time"
)

func main() {

	// Use `time.Now` with `Unix`, `UnixMilli` or `UnixNano`
	// to get elapsed time since the Unix epoch in seconds,
	// milliseconds or nanoseconds, respectively.
	now := time.Now()
	fmt.Println(now)

	fmt.Println(now.Unix())
	fmt.Println(now.UnixMilli())
	fmt.Println(now.UnixNano())

	// You can also convert integer seconds or nanoseconds
	// since the epoch into the corresponding `time`.
	fmt.Println(time.Unix(now.Unix(), 0))
	fmt.Println(time.Unix(0, now.UnixNano()))
}
```
