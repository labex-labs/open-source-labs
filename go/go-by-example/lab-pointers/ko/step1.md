# 포인터 (Pointers)

문제는 `zeroval`과 `zeroptr` 두 함수를 사용하여 포인터가 값과 어떻게 다른지 이해하는 것입니다. `zeroval`은 `int` 매개변수를 가지므로 인수는 값으로 전달됩니다. `zeroval`은 호출 함수에 있는 `ival`과는 별개의 `ival`의 복사본을 얻습니다. 반면에 `zeroptr`은 `*int` 매개변수를 가지므로 `int` 포인터를 받습니다. 함수 본문의 `*iptr` 코드는 메모리 주소에서 해당 주소의 현재 값으로 포인터를 *역참조 (dereferences)*합니다. 역참조된 포인터에 값을 할당하면 참조된 주소의 값이 변경됩니다.

- Golang 에 대한 기본적인 이해가 있어야 합니다.
- Golang 에서 함수를 정의하고 사용하는 방법을 알아야 합니다.
- Golang 에서 포인터를 사용하는 방법을 알아야 합니다.

```sh
# `zeroval` 은 `main` 의 `i` 를 변경하지 않지만,
# `zeroptr` 은 해당 변수의 메모리 주소에 대한 참조를 가지고 있기 때문에 변경합니다.
$ go run pointers.go
initial: 1
zeroval: 1
zeroptr: 0
pointer: 0x42131100
```

전체 코드는 다음과 같습니다.

```go
// Go 는 <em><a href="https://en.wikipedia.org/wiki/Pointer_(computer_programming)">포인터</a></em>를 지원하여,
// 프로그램 내에서 값과 레코드에 대한 참조를 전달할 수 있습니다.

package main

import "fmt"

// 우리는 2 개의 함수: `zeroval` 과 `zeroptr` 을 사용하여 포인터가 값과 어떻게 다른지 보여줄 것입니다. `zeroval` 은
// `int` 매개변수를 가지므로 인수는 값으로 전달됩니다. `zeroval` 은 호출 함수에 있는
// `ival` 과는 별개의 `ival` 의 복사본을 얻습니다.
func zeroval(ival int) {
	ival = 0
}

// 반면에 `zeroptr` 은 `*int` 매개변수를 가지므로
// `int` 포인터를 받습니다. 함수 본문의 `*iptr` 코드는 메모리 주소에서
// 해당 주소의 현재 값으로 포인터를 _역참조_합니다.
// 역참조된 포인터에 값을 할당하면 참조된 주소의 값이 변경됩니다.
func zeroptr(iptr *int) {
	*iptr = 0
}

func main() {
	i := 1
	fmt.Println("initial:", i)

	zeroval(i)
	fmt.Println("zeroval:", i)

	// `&i` 구문은 `i` 의 메모리 주소를 제공합니다.
	// 즉, `i` 에 대한 포인터입니다.
	zeroptr(&i)
	fmt.Println("zeroptr:", i)

	// 포인터도 출력할 수 있습니다.
	fmt.Println("pointer:", &i)
}
```
