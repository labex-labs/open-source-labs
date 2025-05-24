# 가변 인자 함수 (Variadic Functions)

이 랩에서는 임의의 정수 개수를 인수로 받아 최대값을 반환하는 `max`라는 함수를 구현해야 합니다.

- 함수 `max`는 임의의 정수 개수를 인수로 받아야 합니다.
- 함수 `max`는 인수로 전달된 정수들의 최대값을 반환해야 합니다.

```sh
$ go run variadic-functions.go
[1 2] 3
[1 2 3] 6
[1 2 3 4] 10

# Go 의 함수의 또 다른 핵심적인 측면은
# 클로저 (closures) 를 형성하는 능력이며,
# 다음에서 살펴보겠습니다.
```

전체 코드는 다음과 같습니다.

```go
// [_가변 인자 함수_](https://en.wikipedia.org/wiki/Variadic_function)
// 는 임의의 개수의 후행 인수로 호출될 수 있습니다.
// 예를 들어, `fmt.Println` 은 일반적인 가변 인자 함수입니다.

package main

import "fmt"

// 여기는 임의의 개수의 `int` 를 인수로 받는 함수입니다.
func sum(nums ...int) {
	fmt.Print(nums, " ")
	total := 0
	// 함수 내에서 `nums` 의 타입은
	// `[]int` 와 같습니다. `len(nums)` 를 호출하고,
	// `range` 를 사용하여 반복할 수 있습니다.
	for _, num := range nums {
		total += num
	}
	fmt.Println(total)
}

func main() {

	// 가변 인자 함수는 일반적인 방식으로
	// 개별 인수를 사용하여 호출할 수 있습니다.
	sum(1, 2)
	sum(1, 2, 3)

	// 이미 슬라이스에 여러 인수가 있는 경우,
	// `func(slice...)` 를 사용하여 가변 인자 함수에 적용합니다.
	nums := []int{1, 2, 3, 4}
	sum(nums...)
}
```
