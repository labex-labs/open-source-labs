# 재귀 (Recursion)

`sum` 함수는 정수 슬라이스를 입력받아 슬라이스 내 모든 정수의 합을 반환합니다. 하지만 이 함수는 불완전하며 재귀를 사용하여 구현해야 합니다.

- `sum` 함수는 재귀를 사용하여 구현해야 합니다.
- 함수는 정수 슬라이스를 입력으로 받아야 합니다.
- 함수는 슬라이스 내 모든 정수의 합을 반환해야 합니다.

```sh
$ go run recursion.go
5040
13
```

전체 코드는 다음과 같습니다.

```go
// Go 는
// <a href="https://en.wikipedia.org/wiki/Recursion_(computer_science)"><em>재귀 함수</em></a>를 지원합니다.
// 다음은 전형적인 예시입니다.

package main

import "fmt"

// 이 `fact` 함수는 `fact(0)` 의 기본 사례에 도달할 때까지 자신을 호출합니다.
func fact(n int) int {
	if n == 0 {
		return 1
	}
	return n * fact(n-1)
}

func main() {
	fmt.Println(fact(7))

	// 클로저 (Closures) 도 재귀적일 수 있지만, 이는
	// 클로저가 정의되기 전에 명시적으로 타입이 지정된 `var` 로 선언되어야 합니다.
	var fib func(n int) int

	fib = func(n int) int {
		if n < 2 {
			return n
		}

		// `fib` 가 이전에 `main` 에서 선언되었으므로 Go 는
		// 여기서 `fib` 를 사용하여 어떤 함수를 호출해야 하는지 알고 있습니다.
		return fib(n-1) + fib(n-2)
	}

	fmt.Println(fib(7))
}
```
