# 오류

이 랩에서는 입력 인수가 42 일 경우 오류를 반환하는 두 가지 함수를 제공합니다. 첫 번째 함수는 기본 오류 값을 반환하고, 두 번째 함수는 사용자 정의 타입을 사용하여 오류를 나타냅니다.

- `errors` 패키지를 임포트해야 합니다.
- 입력 인수가 42 일 경우 `f1` 함수는 오류를 반환해야 합니다.
- 입력 인수가 42 일 경우 `f2` 함수는 `argError` 타입의 오류를 반환해야 합니다.
- `argError` 타입은 `arg`와 `prob`의 두 필드를 가져야 합니다.
- `argError` 타입은 `Error()` 메서드를 구현해야 합니다.
- `main` 함수는 입력 인수로 7 과 42 를 사용하여 `f1`과 `f2`를 모두 호출해야 합니다.
- `main` 함수는 각 함수 호출의 결과와 함께 반환된 모든 오류를 출력해야 합니다.
- `main` 함수는 사용자 정의 오류의 데이터를 프로그래밍 방식으로 사용하는 방법을 보여주어야 합니다.

```sh
# Go 블로그에서 오류 처리에 대한 자세한 내용은 이 [훌륭한 게시물](https://go.dev/blog/error-handling-and-go) 을 참조하십시오.
```

전체 코드는 다음과 같습니다.

```go
// Go 에서는 명시적이고 별도의 반환 값을 통해 오류를 전달하는 것이 관례입니다. 이는 Java 및 Ruby 와 같은 언어에서 사용되는 예외와 C 에서 가끔 사용되는 오버로드된 단일 결과/오류 값과 대조됩니다. Go 의 접근 방식은 어떤 함수가 오류를 반환하는지 쉽게 확인하고 다른 비 오류 작업에 사용되는 것과 동일한 언어 구문을 사용하여 처리할 수 있도록 합니다.

package main

import (
	"errors"
	"fmt"
)

// 관례에 따라 오류는 마지막 반환 값이며 내장 인터페이스인 `error` 타입입니다.
func f1(arg int) (int, error) {
	if arg == 42 {

		// `errors.New` 는 주어진 오류 메시지로 기본 `error` 값을 구성합니다.
		return -1, errors.New("can't work with 42")

	}

	// 오류 위치의 `nil` 값은 오류가 없음을 나타냅니다.
	return arg + 3, nil
}

// `Error()` 메서드를 구현하여 사용자 정의 타입을 `error` 로 사용할 수 있습니다. 다음은 인수 오류를 명시적으로 나타내기 위해 사용자 정의 타입을 사용하는 위의 예제의 변형입니다.
type argError struct {
	arg  int
	prob string
}

func (e *argError) Error() string {
	return fmt.Sprintf("%d - %s", e.arg, e.prob)
}

func f2(arg int) (int, error) {
	if arg == 42 {

		// 이 경우 `&argError` 구문을 사용하여 두 필드 `arg` 와 `prob` 의 값을 제공하는 새로운 구조체를 만듭니다.
		return -1, &argError{arg, "can't work with it"}
	}
	return arg + 3, nil
}

func main() {

	// 아래 두 루프는 각 오류 반환 함수를 테스트합니다. `if` 줄에서 인라인 오류 검사를 사용하는 것은 Go 코드에서 일반적인 관용구입니다.
	for _, i := range []int{7, 42} {
		if r, e := f1(i); e != nil {
			fmt.Println("f1 failed:", e)
		} else {
			fmt.Println("f1 worked:", r)
		}
	}
	for _, i := range []int{7, 42} {
		if r, e := f2(i); e != nil {
			fmt.Println("f2 failed:", e)
		} else {
			fmt.Println("f2 worked:", r)
		}
	}

	// 사용자 정의 오류의 데이터를 프로그래밍 방식으로 사용하려면 타입 어설션을 통해 사용자 정의 오류 타입의 인스턴스로 오류를 가져와야 합니다.
	_, e := f2(42)
	if ae, ok := e.(*argError); ok {
		fmt.Println(ae.arg)
		fmt.Println(ae.prob)
	}
}
```
