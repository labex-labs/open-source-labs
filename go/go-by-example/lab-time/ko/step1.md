# 시간 (Time)

아래 코드는 Go 에서 시간과 지속 시간을 다루는 방법에 대한 예제를 담고 있습니다. 하지만 코드의 일부가 누락되었습니다. 예상대로 작동하도록 코드를 완성하는 것이 당신의 과제입니다.

- Go 프로그래밍 언어에 대한 기본적인 지식.
- Go 의 시간 및 지속 시간 지원에 대한 숙지.

```sh
$ go run time.go
2012-10-31 15:50:13.793654 +0000 UTC
2009-11-17 20:34:58.651387237 +0000 UTC
2009
November
17
20
34
58
651387237
UTC
Tuesday
true
false
false
25891h15m15.142266763s
25891.25420618521
1.5534752523711128e+06
9.320851514226677e+07
93208515142266763
2012-10-31 15:50:13.793654 +0000 UTC
2006-12-05 01:19:43.509120474 +0000 UTC

# 다음으로 유닉스 에포크 (Unix epoch) 와 관련된 시간 개념을 살펴보겠습니다.
```

전체 코드는 다음과 같습니다.

```go
// Go 는 시간과 지속 시간에 대한 광범위한 지원을 제공합니다;
// 다음은 몇 가지 예입니다.

package main

import (
	"fmt"
	"time"
)

func main() {
	p := fmt.Println

	// 먼저 현재 시간을 얻는 것으로 시작합니다.
	now := time.Now()
	p(now)

	// 연도, 월, 일 등을 제공하여 `time` 구조체를 구성할 수 있습니다. 시간은 항상 `Location`, 즉, 시간대와 연결됩니다.
	then := time.Date(
		2009, 11, 17, 20, 34, 58, 651387237, time.UTC)
	p(then)

	// 예상대로 시간 값의 다양한 구성 요소를 추출할 수 있습니다.
	p(then.Year())
	p(then.Month())
	p(then.Day())
	p(then.Hour())
	p(then.Minute())
	p(then.Second())
	p(then.Nanosecond())
	p(then.Location())

	// 월요일부터 일요일까지의 `Weekday` 도 사용할 수 있습니다.
	p(then.Weekday())

	// 이 메서드는 두 시간을 비교하여 첫 번째 시간이 두 번째 시간보다 먼저, 나중 또는 같은 시간에 발생하는지 테스트합니다.
	p(then.Before(now))
	p(then.After(now))
	p(then.Equal(now))

	// `Sub` 메서드는 두 시간 사이의 간격을 나타내는 `Duration` 을 반환합니다.
	diff := now.Sub(then)
	p(diff)

	// 다양한 단위로 지속 시간의 길이를 계산할 수 있습니다.
	p(diff.Hours())
	p(diff.Minutes())
	p(diff.Seconds())
	p(diff.Nanoseconds())

	// `Add` 를 사용하여 주어진 지속 시간만큼 시간을 앞으로 이동하거나, `-` 를 사용하여 지속 시간만큼 뒤로 이동할 수 있습니다.
	p(then.Add(diff))
	p(then.Add(-diff))
}
```
