# `for`

아래 코드는 다양한 유형의 `for` 루프를 포함하고 있습니다. 하지만 코드의 일부는 불완전하며, 코드가 올바르게 작동하도록 빈칸을 채워야 합니다.

- Golang 구문에 대한 기본적인 지식
- Golang 의 `for` 루프에 대한 숙련도

```sh
$ go run for.go
1
2
3
7
8
9
loop
1
3
5

# We'll see some other `for` forms later when we look at
# `range` statements, channels, and other data
# structures.
```

전체 코드는 다음과 같습니다.

```go
// `for` 는 Go 의 유일한 루핑 구문입니다. 다음은
// 몇 가지 기본적인 유형의 `for` 루프입니다.

package main

import "fmt"

func main() {

	// 가장 기본적인 유형으로, 단일 조건을 사용합니다.
	i := 1
	for i <= 3 {
		fmt.Println(i)
		i = i + 1
	}

	// 고전적인 초기화/조건/후처리 `for` 루프입니다.
	for j := 7; j <= 9; j++ {
		fmt.Println(j)
	}

	// 조건이 없는 `for` 는 루프에서 `break` 하거나
	// 둘러싸는 함수에서 `return` 할 때까지 반복적으로 실행됩니다.
	for {
		fmt.Println("loop")
		break
	}

	// 루프의 다음 반복으로 `continue` 할 수도 있습니다.
	for n := 0; n <= 5; n++ {
		if n%2 == 0 {
			continue
		}
		fmt.Println(n)
	}
}
```
