# 상태를 가진 고루틴 (Stateful Goroutines)

동시 프로그래밍에서 경쟁 조건 (race conditions) 과 데이터 손상을 방지하기 위해 공유 상태에 대한 접근을 동기화하는 것은 필수적입니다. 이 랩에서는 단일 고루틴이 상태를 소유하고, 다른 고루틴이 상태를 읽거나 쓰기 위해 메시지를 보내는 시나리오를 제시합니다.

- 채널 (channels) 을 사용하여 상태를 소유한 고루틴에 읽기 및 쓰기 요청을 발행합니다.
- `readOp` 및 `writeOp` 구조체를 사용하여 요청과 응답을 캡슐화합니다.
- 맵 (map) 을 사용하여 상태를 저장합니다.
- `resp` 채널을 사용하여 성공 여부를 나타내고 값을 반환합니다.
- `atomic` 패키지를 사용하여 읽기 및 쓰기 연산 횟수를 계산합니다.
- `time` 패키지를 사용하여 연산 사이에 지연을 추가합니다.

```sh
# 프로그램을 실행하면 고루틴 기반의
# 상태 관리 예제가 약 80,000 번의
# 총 연산을 완료하는 것을 보여줍니다.
$ go run stateful-goroutines.go
readOps: 71708
writeOps: 7177

# 이 특정 경우, 고루틴 기반 접근 방식은
# 뮤텍스 (mutex)-기반 접근 방식보다 약간 더 복잡했습니다.
# 하지만 다른 채널이 관련되어 있거나
# 여러 뮤텍스를 관리하는 것이 오류가 발생하기 쉬운 경우와 같이
# 특정 경우에 유용할 수 있습니다.
# 특히 프로그램의 정확성을 이해하는 것과 관련하여
# 가장 자연스럽게 느껴지는 접근 방식을 사용해야 합니다.
```

전체 코드는 다음과 같습니다.

```go
// 이전 예제에서는 여러 고루틴 간의 공유 상태에 대한 접근을 동기화하기 위해
// [뮤텍스](mutexes) 를 사용하여 명시적인 잠금을 사용했습니다.
// 또 다른 옵션은 고루틴과 채널의 내장된 동기화 기능을 사용하여
// 동일한 결과를 얻는 것입니다. 이 채널 기반 접근 방식은
// 통신을 통해 메모리를 공유하고 각 데이터 조각이
// 정확히 1 개의 고루틴에 의해 소유되도록 하는 Go 의 아이디어와 일치합니다.

package main

import (
	"fmt"
	"math/rand"
	"sync/atomic"
	"time"
)

// 이 예제에서 우리의 상태는 단일
// 고루틴에 의해 소유됩니다. 이것은 데이터가
// 동시 접근으로 인해 손상되지 않도록 보장합니다.
// 해당 상태를 읽거나 쓰기 위해 다른 고루틴은 메시지를
// 소유 고루틴으로 보내고 해당
// 응답을 받습니다. 이러한 `readOp` 및 `writeOp` `struct` 는
// 해당 요청과 소유 고루틴이 응답할 수 있는 방법을 캡슐화합니다.
type readOp struct {
	key  int
	resp chan int
}
type writeOp struct {
	key  int
	val  int
	resp chan bool
}

func main() {

	// 이전과 마찬가지로 수행하는 연산의 수를 계산합니다.
	var readOps uint64
	var writeOps uint64

	// `reads` 및 `writes` 채널은
	// 다른 고루틴에서 읽기 및 쓰기 요청을 발행하는 데 사용됩니다.
	// 각각.
	reads := make(chan readOp)
	writes := make(chan writeOp)

	// 다음은 `state` 를 소유하는 고루틴입니다.
	// 이전 예제와 마찬가지로 맵이지만 이제
	// 상태를 가진 고루틴에 프라이빗합니다. 이 고루틴은 반복적으로
	// `reads` 및 `writes` 채널을 선택하여
	// 요청이 도착하면 응답합니다. 응답은
	// 먼저 요청된 연산을 수행한 다음 응답
	// 채널 `resp` 에서 값을 보내 성공을 나타냅니다 (및 원하는
	// `reads` 의 경우 값).
	go func() {
		var state = make(map[int]int)
		for {
			select {
			case read := <-reads:
				read.resp <- state[read.key]
			case write := <-writes:
				state[write.key] = write.val
				write.resp <- true
			}
		}
	}()

	// 이것은 `reads` 채널을 통해 상태를 소유한 고루틴에 읽기를 발행하기 위해
	// 100 개의 고루틴을 시작합니다.
	// 각 읽기는 `readOp` 를 구성하고, `reads` 채널을 통해 전송한 다음
	// 제공된 `resp` 채널을 통해 결과를 수신해야 합니다.
	for r := 0; r < 100; r++ {
		go func() {
			for {
				read := readOp{
					key:  rand.Intn(5),
					resp: make(chan int)}
				reads <- read
				<-read.resp
				atomic.AddUint64(&readOps, 1)
				time.Sleep(time.Millisecond)
			}
		}()
	}

	// 유사한 접근 방식을 사용하여
	// 10 개의 쓰기도 시작합니다.
	for w := 0; w < 10; w++ {
		go func() {
			for {
				write := writeOp{
					key:  rand.Intn(5),
					val:  rand.Intn(100),
					resp: make(chan bool)}
				writes <- write
				<-write.resp
				atomic.AddUint64(&writeOps, 1)
				time.Sleep(time.Millisecond)
			}
		}()
	}

	// 고루틴이 1 초 동안 작동하도록 합니다.
	time.Sleep(time.Second)

	// 마지막으로 연산 횟수를 캡처하고 보고합니다.
	readOpsFinal := atomic.LoadUint64(&readOps)
	fmt.Println("readOps:", readOpsFinal)
	writeOpsFinal := atomic.LoadUint64(&writeOps)
	fmt.Println("writeOps:", writeOpsFinal)
}
```
