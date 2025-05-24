# 채널 범위 (Range Over Channels)

정수 채널을 입력으로 받아 채널에서 수신된 모든 정수의 합을 반환하는 함수를 작성해야 합니다.

- 함수 이름은 `sumInts`여야 합니다.
- 함수는 `chan int` 타입의 단일 매개변수를 받아야 합니다.
- 함수는 단일 정수 값을 반환해야 합니다.
- 함수 본문 내에서 어떤 루프나 재귀도 사용할 수 없습니다.
- 외부 패키지를 사용할 수 없습니다.

```sh
$ go run range-over-channels.go
one
two

# 이 예제는 또한 비어 있지 않은 채널을 닫아도
# 나머지 값을 계속 수신할 수 있음을 보여줍니다.
```

전체 코드는 다음과 같습니다.

```go
// [이전](range) 예제에서 `for` 와
// `range` 가 기본 데이터 구조에 대한 반복을 제공하는 방법을 보았습니다.
// 이 구문을 사용하여 채널에서 수신된 값을 반복할 수도 있습니다.

package main

import "fmt"

func main() {

	// `queue` 채널에서 2 개의 값을 반복합니다.
	queue := make(chan string, 2)
	queue <- "one"
	queue <- "two"
	close(queue)

	// 이 `range` 는 `queue` 에서 수신되는 각 요소를 반복합니다.
	// 위에서 채널을 `close` 했기 때문에, 반복은
	// 2 개의 요소를 수신한 후 종료됩니다.
	for elem := range queue {
		fmt.Println(elem)
	}
}
```
