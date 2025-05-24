# 다중 반환 값 (Multiple Return Values)

`swap` 함수를 완성하여 두 개의 입력 매개변수를 반대 순서로 반환하십시오.

- `swap` 함수는 두 개의 정수를 입력 매개변수로 받아야 합니다.
- `swap` 함수는 두 개의 정수를 반대 순서로 반환해야 합니다.

```sh
$ go run multiple-return-values.go
3
7
7

# Accepting a variable number of arguments is another nice
# feature of Go functions; we'll look at this next.
```

전체 코드는 다음과 같습니다.

```go
// Go 는 _다중 반환 값_을 기본적으로 지원합니다.
// 이 기능은 관용적인 Go 에서 자주 사용되며, 예를 들어
// 함수에서 결과와 오류 값을 모두 반환하는 데 사용됩니다.

package main

import "fmt"

// 이 함수 시그니처의 `(int, int)`는
// 함수가 2 개의 `int` 를 반환함을 보여줍니다.
func vals() (int, int) {
	return 3, 7
}

func main() {

	// 여기서는 _다중 할당_을 사용하여
	// 호출에서 반환된 2 개의 서로 다른 값을 사용합니다.
	a, b := vals()
	fmt.Println(a)
	fmt.Println(b)

	// 반환된 값의 하위 집합만 원하는 경우,
	// 빈 식별자 `_` 를 사용하십시오.
	_, c := vals()
	fmt.Println(c)
}
```
