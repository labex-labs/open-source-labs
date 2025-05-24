# 뮤텍스 (Mutex)

이 랩에서 해결해야 할 문제는 여러 고루틴 (goroutine) 을 사용하여 루프 내에서 명명된 카운터를 증가시키고, 카운터에 대한 접근이 동기화되도록 보장하는 것입니다.

- 카운터 맵을 저장하기 위해 `Container` 구조체를 사용합니다.
- `counters` 맵에 대한 접근을 동기화하기 위해 `Mutex`를 사용합니다.
- `Container` 구조체는 `name` 문자열을 인수로 받아 `counters` 맵에서 해당 카운터를 증가시키는 `inc` 메서드를 가져야 합니다.
- `inc` 메서드는 `counters` 맵에 접근하기 전에 뮤텍스를 잠그고, `defer` 문을 사용하여 함수가 종료될 때 뮤텍스를 해제해야 합니다.
- 고루틴이 완료될 때까지 기다리기 위해 `sync.WaitGroup` 구조체를 사용합니다.
- `counters` 맵을 출력하기 위해 `fmt.Println` 함수를 사용합니다.

```sh
# Running the program shows that the counters
# updated as expected.

# Next we'll look at implementing this same state
# management task using only goroutines and channels.
```

전체 코드는 다음과 같습니다.

```go
// In the previous example we saw how to manage simple
// counter state using [atomic operations](atomic-counters).
// For more complex state we can use a [_mutex_](https://en.wikipedia.org/wiki/Mutual_exclusion)
// to safely access data across multiple goroutines.

package main

import (
	"fmt"
	"sync"
)

// Container 는 카운터 맵을 저장합니다; 여러 고루틴에서 동시에 업데이트하려는 경우,
// 접근을 동기화하기 위해 `Mutex` 를 추가합니다.
// 뮤텍스는 복사할 수 없으므로, 이 `struct` 가 전달될 때는
// 포인터로 전달해야 합니다.
type Container struct {
	mu       sync.Mutex
	counters map[string]int
}

func (c *Container) inc(name string) {
	// `counters` 에 접근하기 전에 뮤텍스를 잠급니다; [defer](defer)
	// 문을 사용하여 함수가 종료될 때 뮤텍스를 해제합니다.
	c.mu.Lock()
	defer c.mu.Unlock()
	c.counters[name]++
}

func main() {
	c := Container{
		// 뮤텍스의 제로 값은 그대로 사용할 수 있으므로,
		// 여기서는 초기화가 필요하지 않습니다.
		counters: map[string]int{"a": 0, "b": 0},
	}

	var wg sync.WaitGroup

	// 이 함수는 루프 내에서 명명된 카운터를 증가시킵니다.
	doIncrement := func(name string, n int) {
		for i := 0; i < n; i++ {
			c.inc(name)
		}
		wg.Done()
	}

	// 여러 고루틴을 동시에 실행합니다; 모두 동일한 `Container` 에 접근하고,
	// 그 중 두 개는 동일한 카운터에 접근합니다.
	wg.Add(3)
	go doIncrement("a", 10000)
	go doIncrement("a", 10000)
	go doIncrement("b", 10000)

	// 고루틴이 완료될 때까지 기다립니다.
	wg.Wait()
	fmt.Println(c.counters)
}
```
