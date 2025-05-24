# 함수 (Functions)

제공된 코드에는 `plus`와 `plusPlus` 두 개의 함수가 있습니다. `plus` 함수는 두 개의 정수를 인수로 받아 합계를 반환합니다. `plusPlus` 함수는 세 개의 정수를 인수로 받아 합계를 반환합니다. 여러분의 과제는 세 번째 정수를 처음 두 정수의 합에 더하여 `plusPlus` 함수를 완성하는 것입니다.

- `plus` 함수는 두 개의 정수를 인수로 받아 합계를 정수로 반환해야 합니다.
- `plusPlus` 함수는 세 개의 정수를 인수로 받아 합계를 정수로 반환해야 합니다.
- `plusPlus` 함수는 처음 두 정수의 합을 계산하기 위해 `plus` 함수를 사용해야 합니다.

```sh
$ go run functions.go
1+2 = 3
1+2+3 = 6

# Go 함수에는 몇 가지 다른 기능이 있습니다. 그 중 하나는
# 여러 반환 값이며, 다음에서 살펴보겠습니다.
```

전체 코드는 다음과 같습니다.

```go
// _Functions_는 Go 에서 핵심입니다. 몇 가지 예제를 통해
// 함수에 대해 배우겠습니다.

package main

import "fmt"

// 다음은 두 개의 `int` 를 받아
// 합계를 `int` 로 반환하는 함수입니다.
func plus(a int, b int) int {

	// Go 는 명시적인 반환을 요구합니다. 즉, 마지막
	// 표현식의 값을 자동으로 반환하지 않습니다.
	return a + b
}

// 동일한 유형의 여러 연속 매개변수가 있는 경우,
// 유형을 선언하는 마지막 매개변수까지
// 동일한 유형의 매개변수에 대한 유형 이름을 생략할 수 있습니다.
func plusPlus(a, b, c int) int {
	return a + b + c
}

func main() {

	// 예상대로 `name(args)` 를 사용하여 함수를 호출합니다.
	res := plus(1, 2)
	fmt.Println("1+2 =", res)

	res = plusPlus(1, 2, 3)
	fmt.Println("1+2+3 =", res)
}
```
