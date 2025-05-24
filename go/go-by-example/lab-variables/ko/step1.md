# 변수 (Variables)

Golang 에서 다양한 타입의 변수를 선언하고 초기화하는 코드를 완성해야 합니다.

- Golang 문법에 대한 기본적인 지식
- Golang 에서 변수 선언 및 초기화에 대한 익숙함

```sh
$ go run variables.go
initial
1 2
true
0
apple
```

전체 코드는 다음과 같습니다.

```go
// Go 에서 _변수_는 명시적으로 선언되며,
// 컴파일러는 함수 호출의 타입 정확성 (type-correctness) 을 검사하는 데 사용됩니다.

package main

import "fmt"

func main() {

	// `var` 는 하나 이상의 변수를 선언합니다.
	var a = "initial"
	fmt.Println(a)

	// 한 번에 여러 변수를 선언할 수 있습니다.
	var b, c int = 1, 2
	fmt.Println(b, c)

	// Go 는 초기화된 변수의 타입을 추론합니다.
	var d = true
	fmt.Println(d)

	// 해당 초기화 없이 선언된 변수는 _제로 값 (zero-valued)_을 갖습니다. 예를 들어,
	// `int` 의 제로 값은 `0` 입니다.
	var e int
	fmt.Println(e)

	// `:=` 구문은 변수를 선언하고 초기화하는 축약형입니다. 예를 들어,
	// 이 경우 `var f string = "apple"`과 같습니다.
	// 이 구문은 함수 내부에서만 사용할 수 있습니다.
	f := "apple"
	fmt.Println(f)
}
```
